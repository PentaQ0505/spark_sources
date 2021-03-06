/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.spark.sql

import org.apache.spark.sql.catalyst.TableIdentifier
import org.apache.spark.sql.catalyst.catalog.CatalogTable
import org.apache.spark.sql.sources.SimpleInsertSource
import org.apache.spark.sql.test.{SharedSparkSession, SQLTestUtils}
import org.apache.spark.util.Utils

class SimpleShowCreateTableSuite extends ShowCreateTableSuite with SharedSparkSession

abstract class ShowCreateTableSuite extends QueryTest with SQLTestUtils {
  import testImplicits._

  test("data source table with user specified schema") {
    withTable("ddl_test") {
      val jsonFilePath = Utils.getSparkClassLoader.getResource("sample.json").getFile

      sql(
        s"""CREATE TABLE ddl_test (
           |  a STRING,
           |  b STRING,
           |  `extra col` ARRAY<INT>,
           |  `<another>` STRUCT<x: INT, y: ARRAY<BOOLEAN>>
           |)
           |USING json
           |OPTIONS (
           | PATH '$jsonFilePath'
           |)
         """.stripMargin
      )

      checkCreateTable("ddl_test")
    }
  }

  test("data source table CTAS") {
    withTable("ddl_test") {
      sql(
        s"""CREATE TABLE ddl_test
           |USING json
           |AS SELECT 1 AS a, "foo" AS b
         """.stripMargin
      )

      checkCreateTable("ddl_test")
    }
  }

  test("partitioned data source table") {
    withTable("ddl_test") {
      sql(
        s"""CREATE TABLE ddl_test
           |USING json
           |PARTITIONED BY (b)
           |AS SELECT 1 AS a, "foo" AS b
         """.stripMargin
      )

      checkCreateTable("ddl_test")
    }
  }

  test("bucketed data source table") {
    withTable("ddl_test") {
      sql(
        s"""CREATE TABLE ddl_test
           |USING json
           |CLUSTERED BY (a) SORTED BY (b) INTO 2 BUCKETS
           |AS SELECT 1 AS a, "foo" AS b
         """.stripMargin
      )

      checkCreateTable("ddl_test")
    }
  }

  test("partitioned bucketed data source table") {
    withTable("ddl_test") {
      sql(
        s"""CREATE TABLE ddl_test
           |USING json
           |PARTITIONED BY (c)
           |CLUSTERED BY (a) SORTED BY (b) INTO 2 BUCKETS
           |AS SELECT 1 AS a, "foo" AS b, 2.5 AS c
         """.stripMargin
      )

      checkCreateTable("ddl_test")
    }
  }

  test("data source table with a comment") {
    withTable("ddl_test") {
      sql(
        s"""CREATE TABLE ddl_test
           |USING json
           |COMMENT 'This is a comment'
           |AS SELECT 1 AS a, "foo" AS b, 2.5 AS c
         """.stripMargin
      )

      checkCreateTable("ddl_test")
    }
  }

  test("data source table with table properties") {
    withTable("ddl_test") {
      sql(
        s"""CREATE TABLE ddl_test
           |USING json
           |TBLPROPERTIES ('a' = '1')
           |AS SELECT 1 AS a, "foo" AS b, 2.5 AS c
         """.stripMargin
      )

      checkCreateTable("ddl_test")
    }
  }

  test("data source table using Dataset API") {
    withTable("ddl_test") {
      spark
        .range(3)
        .select('id as 'a, 'id as 'b, 'id as 'c, 'id as 'd, 'id as 'e)
        .write
        .mode("overwrite")
        .partitionBy("a", "b")
        .bucketBy(2, "c", "d")
        .saveAsTable("ddl_test")

      checkCreateTable("ddl_test")
    }
  }

  test("temp view") {
    val viewName = "spark_28383"
    withTempView(viewName) {
      sql(s"CREATE TEMPORARY VIEW $viewName AS SELECT 1 AS a")
      val ex = intercept[AnalysisException] {
        sql(s"SHOW CREATE TABLE $viewName")
      }
      assert(ex.getMessage.contains(
        s"$viewName is a temp view. 'SHOW CREATE TABLE' expects a table or permanent view."))
    }

    withGlobalTempView(viewName) {
      sql(s"CREATE GLOBAL TEMPORARY VIEW $viewName AS SELECT 1 AS a")
      val globalTempViewDb = spark.sessionState.catalog.globalTempViewManager.database
      val ex = intercept[AnalysisException] {
        sql(s"SHOW CREATE TABLE $globalTempViewDb.$viewName")
      }
      assert(ex.getMessage.contains(
        s"$globalTempViewDb.$viewName is a temp view. " +
          "'SHOW CREATE TABLE' expects a table or permanent view."))
    }
  }

  test("SPARK-24911: keep quotes for nested fields") {
    withTable("t1") {
      val createTable = "CREATE TABLE `t1` (`a` STRUCT<`b`: STRING>)"
      sql(s"$createTable USING json")
      val shownDDL = getShowDDL("SHOW CREATE TABLE t1")
      assert(shownDDL == "CREATE TABLE `default`.`t1` ( `a` STRUCT<`b`: STRING>) USING json")

      checkCreateTable("t1")
    }
  }

  test("SPARK-36012: Add NULL flag when SHOW CREATE TABLE") {
    val t = "SPARK_36012"
    withTable(t) {
      sql(
        s"""
           |CREATE TABLE $t (
           |  a bigint NOT NULL,
           |  b bigint
           |)
           |USING ${classOf[SimpleInsertSource].getName}
        """.stripMargin)
      val showDDL = getShowDDL(s"SHOW CREATE TABLE $t")
      assert(showDDL == s"CREATE TABLE `default`.`$t` ( `a` BIGINT NOT NULL," +
        s" `b` BIGINT) USING ${classOf[SimpleInsertSource].getName}")
    }
  }

  test("SPARK-37494: Unify v1 and v2 option output") {
    withTable("ddl_test") {
      sql(
        s"""CREATE TABLE ddl_test (
           |  a STRING
           |)
           |USING json
           |TBLPROPERTIES (
           | 'b' = '1',
           | 'a' = '2')
           |OPTIONS (
           | k4 'v4',
           | `k3` 'v3',
           | 'k5' 'v5',
           | 'k1' = 'v1',
           | k2 = 'v2'
           |)
         """.stripMargin
      )
      val expected = "CREATE TABLE `default`.`ddl_test` ( `a` STRING) USING json" +
        " OPTIONS ( 'k1' = 'v1', 'k2' = 'v2', 'k3' = 'v3', 'k4' = 'v4', 'k5' = 'v5')" +
        " TBLPROPERTIES ( 'a' = '2', 'b' = '1')"
      assert(getShowDDL("SHOW CREATE TABLE ddl_test") == expected)
    }
  }

  protected def getShowDDL(showCreateTableSql: String): String = {
    sql(showCreateTableSql).head().getString(0).split("\n").map(_.trim).mkString(" ")
  }

  protected def checkCreateTable(table: String, serde: Boolean = false): Unit = {
    checkCreateTableOrView(TableIdentifier(table, Some("default")), "TABLE", serde)
  }

  protected def checkCreateView(table: String, serde: Boolean = false): Unit = {
    checkCreateTableOrView(TableIdentifier(table, Some("default")), "VIEW", serde)
  }

  protected def checkCreateTableOrView(
      table: TableIdentifier,
      checkType: String,
      serde: Boolean): Unit = {
    val db = table.database.getOrElse("default")
    val expected = spark.sharedState.externalCatalog.getTable(db, table.table)
    val shownDDL = if (serde) {
      sql(s"SHOW CREATE TABLE ${table.quotedString} AS SERDE").head().getString(0)
    } else {
      sql(s"SHOW CREATE TABLE ${table.quotedString}").head().getString(0)
    }

    sql(s"DROP $checkType ${table.quotedString}")

    try {
      sql(shownDDL)
      val actual = spark.sharedState.externalCatalog.getTable(db, table.table)
      checkCatalogTables(expected, actual)
    } finally {
      sql(s"DROP $checkType IF EXISTS ${table.table}")
    }
  }

  protected def checkCatalogTables(expected: CatalogTable, actual: CatalogTable): Unit = {
    assert(CatalogTable.normalize(actual) == CatalogTable.normalize(expected))
  }
}

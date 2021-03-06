#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import overload
from typing import Any, Dict, Generic, List, Optional, Tuple
from pyspark.ml._typing import JM, P

from pyspark.ml.param.shared import (
    HasFeaturesCol,
    HasHandleInvalid,
    HasInputCol,
    HasInputCols,
    HasLabelCol,
    HasMaxIter,
    HasNumFeatures,
    HasOutputCol,
    HasOutputCols,
    HasRelativeError,
    HasSeed,
    HasStepSize,
    HasThreshold,
    HasThresholds,
)
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaParams, JavaTransformer
from pyspark.ml.linalg import Vector, DenseVector, DenseMatrix
from pyspark.sql.dataframe import DataFrame
from pyspark.ml.param import Param

class Binarizer(
    JavaTransformer,
    HasThreshold,
    HasThresholds,
    HasInputCol,
    HasOutputCol,
    HasInputCols,
    HasOutputCols,
    JavaMLReadable[Binarizer],
    JavaMLWritable,
):
    threshold: Param[float]
    thresholds: Param[List[float]]
    @overload
    def __init__(
        self,
        *,
        threshold: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        thresholds: Optional[List[float]] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> None: ...
    @overload
    def setParams(
        self,
        *,
        threshold: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> Binarizer: ...
    @overload
    def setParams(
        self,
        *,
        thresholds: Optional[List[float]] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> Binarizer: ...
    def setThreshold(self, value: float) -> Binarizer: ...
    def setThresholds(self, value: List[float]) -> Binarizer: ...
    def setInputCol(self, value: str) -> Binarizer: ...
    def setInputCols(self, value: List[str]) -> Binarizer: ...
    def setOutputCol(self, value: str) -> Binarizer: ...
    def setOutputCols(self, value: List[str]) -> Binarizer: ...

class _LSHParams(HasInputCol, HasOutputCol):
    numHashTables: Param[int]
    def __init__(self, *args: Any): ...
    def getNumHashTables(self) -> int: ...

class _LSH(Generic[JM], JavaEstimator[JM], _LSHParams, JavaMLReadable, JavaMLWritable):
    def setNumHashTables(self: P, value: int) -> P: ...
    def setInputCol(self: P, value: str) -> P: ...
    def setOutputCol(self: P, value: str) -> P: ...

class _LSHModel(JavaModel, _LSHParams):
    def setInputCol(self: P, value: str) -> P: ...
    def setOutputCol(self: P, value: str) -> P: ...
    def approxNearestNeighbors(
        self,
        dataset: DataFrame,
        key: Vector,
        numNearestNeighbors: int,
        distCol: str = ...,
    ) -> DataFrame: ...
    def approxSimilarityJoin(
        self,
        datasetA: DataFrame,
        datasetB: DataFrame,
        threshold: float,
        distCol: str = ...,
    ) -> DataFrame: ...

class _BucketedRandomProjectionLSHParams:
    bucketLength: Param[float]
    def getBucketLength(self) -> float: ...

class BucketedRandomProjectionLSH(
    _LSH[BucketedRandomProjectionLSHModel],
    _LSHParams,
    HasSeed,
    JavaMLReadable[BucketedRandomProjectionLSH],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...,
        bucketLength: Optional[float] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...,
        bucketLength: Optional[float] = ...,
    ) -> BucketedRandomProjectionLSH: ...
    def setBucketLength(self, value: float) -> BucketedRandomProjectionLSH: ...
    def setSeed(self, value: int) -> BucketedRandomProjectionLSH: ...

class BucketedRandomProjectionLSHModel(
    _LSHModel,
    _BucketedRandomProjectionLSHParams,
    JavaMLReadable[BucketedRandomProjectionLSHModel],
    JavaMLWritable,
): ...

class Bucketizer(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    HasInputCols,
    HasOutputCols,
    HasHandleInvalid,
    JavaMLReadable[Bucketizer],
    JavaMLWritable,
):
    splits: Param[List[float]]
    handleInvalid: Param[str]
    splitsArray: Param[List[List[float]]]
    @overload
    def __init__(
        self,
        *,
        splits: Optional[List[float]] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        handleInvalid: str = ...,
        splitsArray: Optional[List[List[float]]] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> None: ...
    @overload
    def setParams(
        self,
        *,
        splits: Optional[List[float]] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
    ) -> Bucketizer: ...
    @overload
    def setParams(
        self,
        *,
        handleInvalid: str = ...,
        splitsArray: Optional[List[List[float]]] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> Bucketizer: ...
    def setSplits(self, value: List[float]) -> Bucketizer: ...
    def getSplits(self) -> List[float]: ...
    def setSplitsArray(self, value: List[List[float]]) -> Bucketizer: ...
    def getSplitsArray(self) -> List[List[float]]: ...
    def setInputCol(self, value: str) -> Bucketizer: ...
    def setInputCols(self, value: List[str]) -> Bucketizer: ...
    def setOutputCol(self, value: str) -> Bucketizer: ...
    def setOutputCols(self, value: List[str]) -> Bucketizer: ...
    def setHandleInvalid(self, value: str) -> Bucketizer: ...

class _CountVectorizerParams(JavaParams, HasInputCol, HasOutputCol):
    minTF: Param[float]
    minDF: Param[float]
    maxDF: Param[float]
    vocabSize: Param[int]
    binary: Param[bool]
    def __init__(self, *args: Any) -> None: ...
    def getMinTF(self) -> float: ...
    def getMinDF(self) -> float: ...
    def getMaxDF(self) -> float: ...
    def getVocabSize(self) -> int: ...
    def getBinary(self) -> bool: ...

class CountVectorizer(
    JavaEstimator[CountVectorizerModel],
    _CountVectorizerParams,
    JavaMLReadable[CountVectorizer],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        minTF: float = ...,
        minDF: float = ...,
        maxDF: float = ...,
        vocabSize: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        minTF: float = ...,
        minDF: float = ...,
        maxDF: float = ...,
        vocabSize: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> CountVectorizer: ...
    def setMinTF(self, value: float) -> CountVectorizer: ...
    def setMinDF(self, value: float) -> CountVectorizer: ...
    def setMaxDF(self, value: float) -> CountVectorizer: ...
    def setVocabSize(self, value: int) -> CountVectorizer: ...
    def setBinary(self, value: bool) -> CountVectorizer: ...
    def setInputCol(self, value: str) -> CountVectorizer: ...
    def setOutputCol(self, value: str) -> CountVectorizer: ...

class CountVectorizerModel(JavaModel, JavaMLReadable[CountVectorizerModel], JavaMLWritable):
    def setInputCol(self, value: str) -> CountVectorizerModel: ...
    def setOutputCol(self, value: str) -> CountVectorizerModel: ...
    def setMinTF(self, value: float) -> CountVectorizerModel: ...
    def setBinary(self, value: bool) -> CountVectorizerModel: ...
    @classmethod
    def from_vocabulary(
        cls,
        vocabulary: List[str],
        inputCol: str,
        outputCol: Optional[str] = ...,
        minTF: Optional[float] = ...,
        binary: Optional[bool] = ...,
    ) -> CountVectorizerModel: ...
    @property
    def vocabulary(self) -> List[str]: ...

class DCT(JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable[DCT], JavaMLWritable):
    inverse: Param[bool]
    def __init__(
        self, *, inverse: bool = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, inverse: bool = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> DCT: ...
    def setInverse(self, value: bool) -> DCT: ...
    def getInverse(self) -> bool: ...
    def setInputCol(self, value: str) -> DCT: ...
    def setOutputCol(self, value: str) -> DCT: ...

class ElementwiseProduct(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable[ElementwiseProduct],
    JavaMLWritable,
):
    scalingVec: Param[Vector]
    def __init__(
        self,
        *,
        scalingVec: Optional[Vector] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        scalingVec: Optional[Vector] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> ElementwiseProduct: ...
    def setScalingVec(self, value: Vector) -> ElementwiseProduct: ...
    def getScalingVec(self) -> Vector: ...
    def setInputCol(self, value: str) -> ElementwiseProduct: ...
    def setOutputCol(self, value: str) -> ElementwiseProduct: ...

class FeatureHasher(
    JavaTransformer,
    HasInputCols,
    HasOutputCol,
    HasNumFeatures,
    JavaMLReadable[FeatureHasher],
    JavaMLWritable,
):
    categoricalCols: Param[List[str]]
    def __init__(
        self,
        *,
        numFeatures: int = ...,
        inputCols: Optional[List[str]] = ...,
        outputCol: Optional[str] = ...,
        categoricalCols: Optional[List[str]] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        numFeatures: int = ...,
        inputCols: Optional[List[str]] = ...,
        outputCol: Optional[str] = ...,
        categoricalCols: Optional[List[str]] = ...,
    ) -> FeatureHasher: ...
    def setCategoricalCols(self, value: List[str]) -> FeatureHasher: ...
    def getCategoricalCols(self) -> List[str]: ...
    def setInputCols(self, value: List[str]) -> FeatureHasher: ...
    def setOutputCol(self, value: str) -> FeatureHasher: ...
    def setNumFeatures(self, value: int) -> FeatureHasher: ...

class HashingTF(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    HasNumFeatures,
    JavaMLReadable[HashingTF],
    JavaMLWritable,
):
    binary: Param[bool]
    def __init__(
        self,
        *,
        numFeatures: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        numFeatures: int = ...,
        binary: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> HashingTF: ...
    def setBinary(self, value: bool) -> HashingTF: ...
    def getBinary(self) -> bool: ...
    def setInputCol(self, value: str) -> HashingTF: ...
    def setOutputCol(self, value: str) -> HashingTF: ...
    def setNumFeatures(self, value: int) -> HashingTF: ...
    def indexOf(self, term: Any) -> int: ...

class _IDFParams(HasInputCol, HasOutputCol):
    minDocFreq: Param[int]
    def __init__(self, *args: Any): ...
    def getMinDocFreq(self) -> int: ...

class IDF(JavaEstimator[IDFModel], _IDFParams, JavaMLReadable[IDF], JavaMLWritable):
    def __init__(
        self,
        *,
        minDocFreq: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        minDocFreq: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> IDF: ...
    def setMinDocFreq(self, value: int) -> IDF: ...
    def setInputCol(self, value: str) -> IDF: ...
    def setOutputCol(self, value: str) -> IDF: ...

class IDFModel(JavaModel, _IDFParams, JavaMLReadable[IDFModel], JavaMLWritable):
    def setInputCol(self, value: str) -> IDFModel: ...
    def setOutputCol(self, value: str) -> IDFModel: ...
    @property
    def idf(self) -> Vector: ...
    @property
    def docFreq(self) -> List[int]: ...
    @property
    def numDocs(self) -> int: ...

class _ImputerParams(HasInputCol, HasInputCols, HasOutputCol, HasOutputCols, HasRelativeError):
    strategy: Param[str]
    missingValue: Param[float]
    def getStrategy(self) -> str: ...
    def getMissingValue(self) -> float: ...

class Imputer(JavaEstimator[ImputerModel], _ImputerParams, JavaMLReadable[Imputer], JavaMLWritable):
    @overload
    def __init__(
        self,
        *,
        strategy: str = ...,
        missingValue: float = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        relativeError: float = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        strategy: str = ...,
        missingValue: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        relativeError: float = ...,
    ) -> None: ...
    @overload
    def setParams(
        self,
        *,
        strategy: str = ...,
        missingValue: float = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        relativeError: float = ...,
    ) -> Imputer: ...
    @overload
    def setParams(
        self,
        *,
        strategy: str = ...,
        missingValue: float = ...,
        inputCol: Optional[str] = ...,
        outputCols: Optional[str] = ...,
        relativeError: float = ...,
    ) -> Imputer: ...
    def setStrategy(self, value: str) -> Imputer: ...
    def setMissingValue(self, value: float) -> Imputer: ...
    def setInputCols(self, value: List[str]) -> Imputer: ...
    def setOutputCols(self, value: List[str]) -> Imputer: ...
    def setInputCol(self, value: str) -> Imputer: ...
    def setOutputCol(self, value: str) -> Imputer: ...
    def setRelativeError(self, value: float) -> Imputer: ...

class ImputerModel(JavaModel, _ImputerParams, JavaMLReadable[ImputerModel], JavaMLWritable):
    def setInputCols(self, value: List[str]) -> ImputerModel: ...
    def setOutputCols(self, value: List[str]) -> ImputerModel: ...
    def setInputCol(self, value: str) -> ImputerModel: ...
    def setOutputCol(self, value: str) -> ImputerModel: ...
    @property
    def surrogateDF(self) -> DataFrame: ...

class Interaction(
    JavaTransformer,
    HasInputCols,
    HasOutputCol,
    JavaMLReadable[Interaction],
    JavaMLWritable,
):
    def __init__(
        self, *, inputCols: Optional[List[str]] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, inputCols: Optional[List[str]] = ..., outputCol: Optional[str] = ...
    ) -> Interaction: ...
    def setInputCols(self, value: List[str]) -> Interaction: ...
    def setOutputCol(self, value: str) -> Interaction: ...

class _MaxAbsScalerParams(HasInputCol, HasOutputCol): ...

class MaxAbsScaler(
    JavaEstimator[MaxAbsScalerModel],
    _MaxAbsScalerParams,
    JavaMLReadable[MaxAbsScaler],
    JavaMLWritable,
):
    def __init__(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> MaxAbsScaler: ...
    def setInputCol(self, value: str) -> MaxAbsScaler: ...
    def setOutputCol(self, value: str) -> MaxAbsScaler: ...

class MaxAbsScalerModel(
    JavaModel, _MaxAbsScalerParams, JavaMLReadable[MaxAbsScalerModel], JavaMLWritable
):
    def setInputCol(self, value: str) -> MaxAbsScalerModel: ...
    def setOutputCol(self, value: str) -> MaxAbsScalerModel: ...
    @property
    def maxAbs(self) -> Vector: ...

class MinHashLSH(
    _LSH[MinHashLSHModel],
    HasInputCol,
    HasOutputCol,
    HasSeed,
    JavaMLReadable[MinHashLSH],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        seed: Optional[int] = ...,
        numHashTables: int = ...,
    ) -> MinHashLSH: ...
    def setSeed(self, value: int) -> MinHashLSH: ...

class MinHashLSHModel(_LSHModel, JavaMLReadable[MinHashLSHModel], JavaMLWritable): ...

class _MinMaxScalerParams(HasInputCol, HasOutputCol):
    min: Param[float]
    max: Param[float]
    def __init__(self, *args: Any): ...
    def getMin(self) -> float: ...
    def getMax(self) -> float: ...

class MinMaxScaler(
    JavaEstimator[MinMaxScalerModel],
    _MinMaxScalerParams,
    JavaMLReadable[MinMaxScaler],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        min: float = ...,
        max: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        min: float = ...,
        max: float = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> MinMaxScaler: ...
    def setMin(self, value: float) -> MinMaxScaler: ...
    def setMax(self, value: float) -> MinMaxScaler: ...
    def setInputCol(self, value: str) -> MinMaxScaler: ...
    def setOutputCol(self, value: str) -> MinMaxScaler: ...

class MinMaxScalerModel(
    JavaModel, _MinMaxScalerParams, JavaMLReadable[MinMaxScalerModel], JavaMLWritable
):
    def setInputCol(self, value: str) -> MinMaxScalerModel: ...
    def setOutputCol(self, value: str) -> MinMaxScalerModel: ...
    def setMin(self, value: float) -> MinMaxScalerModel: ...
    def setMax(self, value: float) -> MinMaxScalerModel: ...
    @property
    def originalMin(self) -> Vector: ...
    @property
    def originalMax(self) -> Vector: ...

class NGram(JavaTransformer, HasInputCol, HasOutputCol, JavaMLReadable[NGram], JavaMLWritable):
    n: Param[int]
    def __init__(
        self, *, n: int = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, n: int = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> NGram: ...
    def setN(self, value: int) -> NGram: ...
    def getN(self) -> int: ...
    def setInputCol(self, value: str) -> NGram: ...
    def setOutputCol(self, value: str) -> NGram: ...

class Normalizer(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable[Normalizer],
    JavaMLWritable,
):
    p: Param[float]
    def __init__(
        self, *, p: float = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, p: float = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> Normalizer: ...
    def setP(self, value: float) -> Normalizer: ...
    def getP(self) -> float: ...
    def setInputCol(self, value: str) -> Normalizer: ...
    def setOutputCol(self, value: str) -> Normalizer: ...

class _OneHotEncoderParams(HasInputCols, HasOutputCols, HasHandleInvalid):
    handleInvalid: Param[str]
    dropLast: Param[bool]
    def __init__(self, *args: Any): ...
    def getDropLast(self) -> bool: ...

class OneHotEncoder(
    JavaEstimator[OneHotEncoderModel],
    _OneHotEncoderParams,
    JavaMLReadable[OneHotEncoder],
    JavaMLWritable,
):
    @overload
    def __init__(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        handleInvalid: str = ...,
        dropLast: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        handleInvalid: str = ...,
        dropLast: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    @overload
    def setParams(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        handleInvalid: str = ...,
        dropLast: bool = ...,
    ) -> OneHotEncoder: ...
    @overload
    def setParams(
        self,
        *,
        handleInvalid: str = ...,
        dropLast: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> OneHotEncoder: ...
    def setDropLast(self, value: bool) -> OneHotEncoder: ...
    def setInputCols(self, value: List[str]) -> OneHotEncoder: ...
    def setOutputCols(self, value: List[str]) -> OneHotEncoder: ...
    def setHandleInvalid(self, value: str) -> OneHotEncoder: ...
    def setInputCol(self, value: str) -> OneHotEncoder: ...
    def setOutputCol(self, value: str) -> OneHotEncoder: ...

class OneHotEncoderModel(
    JavaModel, _OneHotEncoderParams, JavaMLReadable[OneHotEncoderModel], JavaMLWritable
):
    def setDropLast(self, value: bool) -> OneHotEncoderModel: ...
    def setInputCols(self, value: List[str]) -> OneHotEncoderModel: ...
    def setOutputCols(self, value: List[str]) -> OneHotEncoderModel: ...
    def setInputCol(self, value: str) -> OneHotEncoderModel: ...
    def setOutputCol(self, value: str) -> OneHotEncoderModel: ...
    def setHandleInvalid(self, value: str) -> OneHotEncoderModel: ...
    @property
    def categorySizes(self) -> List[int]: ...

class PolynomialExpansion(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable[PolynomialExpansion],
    JavaMLWritable,
):
    degree: Param[int]
    def __init__(
        self, *, degree: int = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, degree: int = ..., inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> PolynomialExpansion: ...
    def setDegree(self, value: int) -> PolynomialExpansion: ...
    def getDegree(self) -> int: ...
    def setInputCol(self, value: str) -> PolynomialExpansion: ...
    def setOutputCol(self, value: str) -> PolynomialExpansion: ...

class QuantileDiscretizer(
    JavaEstimator[Bucketizer],
    HasInputCol,
    HasOutputCol,
    HasInputCols,
    HasOutputCols,
    HasHandleInvalid,
    HasRelativeError,
    JavaMLReadable[QuantileDiscretizer],
    JavaMLWritable,
):
    numBuckets: Param[int]
    handleInvalid: Param[str]
    numBucketsArray: Param[List[int]]
    @overload
    def __init__(
        self,
        *,
        numBuckets: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        relativeError: float = ...,
        handleInvalid: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        relativeError: float = ...,
        handleInvalid: str = ...,
        numBucketsArray: Optional[List[int]] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> None: ...
    @overload
    def setParams(
        self,
        *,
        numBuckets: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        relativeError: float = ...,
        handleInvalid: str = ...,
    ) -> QuantileDiscretizer: ...
    @overload
    def setParams(
        self,
        *,
        relativeError: float = ...,
        handleInvalid: str = ...,
        numBucketsArray: Optional[List[int]] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> QuantileDiscretizer: ...
    def setNumBuckets(self, value: int) -> QuantileDiscretizer: ...
    def getNumBuckets(self) -> int: ...
    def setNumBucketsArray(self, value: List[int]) -> QuantileDiscretizer: ...
    def getNumBucketsArray(self) -> List[int]: ...
    def setRelativeError(self, value: float) -> QuantileDiscretizer: ...
    def setInputCol(self, value: str) -> QuantileDiscretizer: ...
    def setInputCols(self, value: List[str]) -> QuantileDiscretizer: ...
    def setOutputCol(self, value: str) -> QuantileDiscretizer: ...
    def setOutputCols(self, value: List[str]) -> QuantileDiscretizer: ...
    def setHandleInvalid(self, value: str) -> QuantileDiscretizer: ...

class _RobustScalerParams(HasInputCol, HasOutputCol, HasRelativeError):
    lower: Param[float]
    upper: Param[float]
    withCentering: Param[bool]
    withScaling: Param[bool]
    def __init__(self, *args: Any): ...
    def getLower(self) -> float: ...
    def getUpper(self) -> float: ...
    def getWithCentering(self) -> bool: ...
    def getWithScaling(self) -> bool: ...

class RobustScaler(
    JavaEstimator, _RobustScalerParams, JavaMLReadable[RobustScaler], JavaMLWritable
):
    def __init__(
        self,
        *,
        lower: float = ...,
        upper: float = ...,
        withCentering: bool = ...,
        withScaling: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        relativeError: float = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        lower: float = ...,
        upper: float = ...,
        withCentering: bool = ...,
        withScaling: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        relativeError: float = ...,
    ) -> RobustScaler: ...
    def setLower(self, value: float) -> RobustScaler: ...
    def setUpper(self, value: float) -> RobustScaler: ...
    def setWithCentering(self, value: bool) -> RobustScaler: ...
    def setWithScaling(self, value: bool) -> RobustScaler: ...
    def setInputCol(self, value: str) -> RobustScaler: ...
    def setOutputCol(self, value: str) -> RobustScaler: ...
    def setRelativeError(self, value: float) -> RobustScaler: ...

class RobustScalerModel(
    JavaModel, _RobustScalerParams, JavaMLReadable[RobustScalerModel], JavaMLWritable
):
    def setInputCol(self, value: str) -> RobustScalerModel: ...
    def setOutputCol(self, value: str) -> RobustScalerModel: ...
    @property
    def median(self) -> Vector: ...
    @property
    def range(self) -> Vector: ...

class RegexTokenizer(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable[RegexTokenizer],
    JavaMLWritable,
):
    minTokenLength: Param[int]
    gaps: Param[bool]
    pattern: Param[str]
    toLowercase: Param[bool]
    def __init__(
        self,
        *,
        minTokenLength: int = ...,
        gaps: bool = ...,
        pattern: str = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        toLowercase: bool = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        minTokenLength: int = ...,
        gaps: bool = ...,
        pattern: str = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        toLowercase: bool = ...,
    ) -> RegexTokenizer: ...
    def setMinTokenLength(self, value: int) -> RegexTokenizer: ...
    def getMinTokenLength(self) -> int: ...
    def setGaps(self, value: bool) -> RegexTokenizer: ...
    def getGaps(self) -> bool: ...
    def setPattern(self, value: str) -> RegexTokenizer: ...
    def getPattern(self) -> str: ...
    def setToLowercase(self, value: bool) -> RegexTokenizer: ...
    def getToLowercase(self) -> bool: ...
    def setInputCol(self, value: str) -> RegexTokenizer: ...
    def setOutputCol(self, value: str) -> RegexTokenizer: ...

class SQLTransformer(JavaTransformer, JavaMLReadable[SQLTransformer], JavaMLWritable):
    statement: Param[str]
    def __init__(self, *, statement: Optional[str] = ...) -> None: ...
    def setParams(self, *, statement: Optional[str] = ...) -> SQLTransformer: ...
    def setStatement(self, value: str) -> SQLTransformer: ...
    def getStatement(self) -> str: ...

class _StandardScalerParams(HasInputCol, HasOutputCol):
    withMean: Param[bool]
    withStd: Param[bool]
    def __init__(self, *args: Any): ...
    def getWithMean(self) -> bool: ...
    def getWithStd(self) -> bool: ...

class StandardScaler(
    JavaEstimator[StandardScalerModel],
    _StandardScalerParams,
    JavaMLReadable[StandardScaler],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        withMean: bool = ...,
        withStd: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        withMean: bool = ...,
        withStd: bool = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> StandardScaler: ...
    def setWithMean(self, value: bool) -> StandardScaler: ...
    def setWithStd(self, value: bool) -> StandardScaler: ...
    def setInputCol(self, value: str) -> StandardScaler: ...
    def setOutputCol(self, value: str) -> StandardScaler: ...

class StandardScalerModel(
    JavaModel,
    _StandardScalerParams,
    JavaMLReadable[StandardScalerModel],
    JavaMLWritable,
):
    def setInputCol(self, value: str) -> StandardScalerModel: ...
    def setOutputCol(self, value: str) -> StandardScalerModel: ...
    @property
    def std(self) -> Vector: ...
    @property
    def mean(self) -> Vector: ...

class _StringIndexerParams(
    JavaParams, HasHandleInvalid, HasInputCol, HasOutputCol, HasInputCols, HasOutputCols
):
    stringOrderType: Param[str]
    handleInvalid: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getStringOrderType(self) -> str: ...

class StringIndexer(
    JavaEstimator[StringIndexerModel],
    _StringIndexerParams,
    JavaMLReadable[StringIndexer],
    JavaMLWritable,
):
    @overload
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
        stringOrderType: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        handleInvalid: str = ...,
        stringOrderType: str = ...,
    ) -> None: ...
    @overload
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
        stringOrderType: str = ...,
    ) -> StringIndexer: ...
    @overload
    def setParams(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
        handleInvalid: str = ...,
        stringOrderType: str = ...,
    ) -> StringIndexer: ...
    def setStringOrderType(self, value: str) -> StringIndexer: ...
    def setInputCol(self, value: str) -> StringIndexer: ...
    def setInputCols(self, value: List[str]) -> StringIndexer: ...
    def setOutputCol(self, value: str) -> StringIndexer: ...
    def setOutputCols(self, value: List[str]) -> StringIndexer: ...
    def setHandleInvalid(self, value: str) -> StringIndexer: ...

class StringIndexerModel(
    JavaModel, _StringIndexerParams, JavaMLReadable[StringIndexerModel], JavaMLWritable
):
    def setInputCol(self, value: str) -> StringIndexerModel: ...
    def setInputCols(self, value: List[str]) -> StringIndexerModel: ...
    def setOutputCol(self, value: str) -> StringIndexerModel: ...
    def setOutputCols(self, value: List[str]) -> StringIndexerModel: ...
    def setHandleInvalid(self, value: str) -> StringIndexerModel: ...
    @classmethod
    def from_labels(
        cls,
        labels: List[str],
        inputCol: str,
        outputCol: Optional[str] = ...,
        handleInvalid: Optional[str] = ...,
    ) -> StringIndexerModel: ...
    @classmethod
    def from_arrays_of_labels(
        cls,
        arrayOfLabels: List[List[str]],
        inputCols: List[str],
        outputCols: Optional[List[str]] = ...,
        handleInvalid: Optional[str] = ...,
    ) -> StringIndexerModel: ...
    @property
    def labels(self) -> List[str]: ...

class IndexToString(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable[IndexToString],
    JavaMLWritable,
):
    labels: Param[List[str]]
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        labels: Optional[List[str]] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        labels: Optional[List[str]] = ...,
    ) -> IndexToString: ...
    def setLabels(self, value: List[str]) -> IndexToString: ...
    def getLabels(self) -> List[str]: ...
    def setInputCol(self, value: str) -> IndexToString: ...
    def setOutputCol(self, value: str) -> IndexToString: ...

class StopWordsRemover(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    HasInputCols,
    HasOutputCols,
    JavaMLReadable[StopWordsRemover],
    JavaMLWritable,
):
    stopWords: Param[List[str]]
    caseSensitive: Param[bool]
    locale: Param[str]
    @overload
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        stopWords: Optional[List[str]] = ...,
        caseSensitive: bool = ...,
        locale: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        stopWords: Optional[List[str]] = ...,
        caseSensitive: bool = ...,
        locale: Optional[str] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> None: ...
    @overload
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        stopWords: Optional[List[str]] = ...,
        caseSensitive: bool = ...,
        locale: Optional[str] = ...,
    ) -> StopWordsRemover: ...
    @overload
    def setParams(
        self,
        *,
        stopWords: Optional[List[str]] = ...,
        caseSensitive: bool = ...,
        locale: Optional[str] = ...,
        inputCols: Optional[List[str]] = ...,
        outputCols: Optional[List[str]] = ...,
    ) -> StopWordsRemover: ...
    def setStopWords(self, value: List[str]) -> StopWordsRemover: ...
    def getStopWords(self) -> List[str]: ...
    def setCaseSensitive(self, value: bool) -> StopWordsRemover: ...
    def getCaseSensitive(self) -> bool: ...
    def setLocale(self, value: str) -> StopWordsRemover: ...
    def getLocale(self) -> str: ...
    def setInputCol(self, value: str) -> StopWordsRemover: ...
    def setOutputCol(self, value: str) -> StopWordsRemover: ...
    def setInputCols(self, value: List[str]) -> StopWordsRemover: ...
    def setOutputCols(self, value: List[str]) -> StopWordsRemover: ...
    @staticmethod
    def loadDefaultStopWords(language: str) -> List[str]: ...

class Tokenizer(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable[Tokenizer],
    JavaMLWritable,
):
    def __init__(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self, *, inputCol: Optional[str] = ..., outputCol: Optional[str] = ...
    ) -> Tokenizer: ...
    def setInputCol(self, value: str) -> Tokenizer: ...
    def setOutputCol(self, value: str) -> Tokenizer: ...

class VectorAssembler(
    JavaTransformer,
    HasInputCols,
    HasOutputCol,
    HasHandleInvalid,
    JavaMLReadable[VectorAssembler],
    JavaMLWritable,
):
    handleInvalid: Param[str]
    def __init__(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCols: Optional[List[str]] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
    ) -> VectorAssembler: ...
    def setInputCols(self, value: List[str]) -> VectorAssembler: ...
    def setOutputCol(self, value: str) -> VectorAssembler: ...
    def setHandleInvalid(self, value: str) -> VectorAssembler: ...

class _VectorIndexerParams(HasInputCol, HasOutputCol, HasHandleInvalid):
    maxCategories: Param[int]
    handleInvalid: Param[str]
    def __init__(self, *args: Any): ...
    def getMaxCategories(self) -> int: ...

class VectorIndexer(
    JavaEstimator[VectorIndexerModel],
    _VectorIndexerParams,
    HasHandleInvalid,
    JavaMLReadable[VectorIndexer],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        maxCategories: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        maxCategories: int = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        handleInvalid: str = ...,
    ) -> VectorIndexer: ...
    def setMaxCategories(self, value: int) -> VectorIndexer: ...
    def setInputCol(self, value: str) -> VectorIndexer: ...
    def setOutputCol(self, value: str) -> VectorIndexer: ...
    def setHandleInvalid(self, value: str) -> VectorIndexer: ...

class VectorIndexerModel(
    JavaModel, _VectorIndexerParams, JavaMLReadable[VectorIndexerModel], JavaMLWritable
):
    def setInputCol(self, value: str) -> VectorIndexerModel: ...
    def setOutputCol(self, value: str) -> VectorIndexerModel: ...
    @property
    def numFeatures(self) -> int: ...
    @property
    def categoryMaps(self) -> Dict[int, Tuple[float, int]]: ...

class VectorSlicer(
    JavaTransformer,
    HasInputCol,
    HasOutputCol,
    JavaMLReadable[VectorSlicer],
    JavaMLWritable,
):
    indices: Param[List[int]]
    names: Param[List[str]]
    def __init__(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        indices: Optional[List[int]] = ...,
        names: Optional[List[str]] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        indices: Optional[List[int]] = ...,
        names: Optional[List[str]] = ...,
    ) -> VectorSlicer: ...
    def setIndices(self, value: List[int]) -> VectorSlicer: ...
    def getIndices(self) -> List[int]: ...
    def setNames(self, value: List[str]) -> VectorSlicer: ...
    def getNames(self) -> List[str]: ...
    def setInputCol(self, value: str) -> VectorSlicer: ...
    def setOutputCol(self, value: str) -> VectorSlicer: ...

class _Word2VecParams(HasStepSize, HasMaxIter, HasSeed, HasInputCol, HasOutputCol):
    vectorSize: Param[int]
    numPartitions: Param[int]
    minCount: Param[int]
    windowSize: Param[int]
    maxSentenceLength: Param[int]
    def __init__(self, *args: Any): ...
    def getVectorSize(self) -> int: ...
    def getNumPartitions(self) -> int: ...
    def getMinCount(self) -> int: ...
    def getWindowSize(self) -> int: ...
    def getMaxSentenceLength(self) -> int: ...

class Word2Vec(
    JavaEstimator[Word2VecModel],
    _Word2VecParams,
    JavaMLReadable[Word2Vec],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        vectorSize: int = ...,
        minCount: int = ...,
        numPartitions: int = ...,
        stepSize: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        windowSize: int = ...,
        maxSentenceLength: int = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        vectorSize: int = ...,
        minCount: int = ...,
        numPartitions: int = ...,
        stepSize: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
        windowSize: int = ...,
        maxSentenceLength: int = ...,
    ) -> Word2Vec: ...
    def setVectorSize(self, value: int) -> Word2Vec: ...
    def setNumPartitions(self, value: int) -> Word2Vec: ...
    def setMinCount(self, value: int) -> Word2Vec: ...
    def setWindowSize(self, value: int) -> Word2Vec: ...
    def setMaxSentenceLength(self, value: int) -> Word2Vec: ...
    def setMaxIter(self, value: int) -> Word2Vec: ...
    def setInputCol(self, value: str) -> Word2Vec: ...
    def setOutputCol(self, value: str) -> Word2Vec: ...
    def setSeed(self, value: int) -> Word2Vec: ...
    def setStepSize(self, value: float) -> Word2Vec: ...

class Word2VecModel(JavaModel, _Word2VecParams, JavaMLReadable[Word2VecModel], JavaMLWritable):
    def getVectors(self) -> DataFrame: ...
    def setInputCol(self, value: str) -> Word2VecModel: ...
    def setOutputCol(self, value: str) -> Word2VecModel: ...
    @overload
    def findSynonyms(self, word: str, num: int) -> DataFrame: ...
    @overload
    def findSynonyms(self, word: Vector, num: int) -> DataFrame: ...
    @overload
    def findSynonymsArray(self, word: str, num: int) -> List[Tuple[str, float]]: ...
    @overload
    def findSynonymsArray(self, word: Vector, num: int) -> List[Tuple[str, float]]: ...

class _PCAParams(HasInputCol, HasOutputCol):
    k: Param[int]
    def getK(self) -> int: ...

class PCA(JavaEstimator[PCAModel], _PCAParams, JavaMLReadable[PCA], JavaMLWritable):
    def __init__(
        self,
        *,
        k: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        k: Optional[int] = ...,
        inputCol: Optional[str] = ...,
        outputCol: Optional[str] = ...,
    ) -> PCA: ...
    def setK(self, value: int) -> PCA: ...
    def setInputCol(self, value: str) -> PCA: ...
    def setOutputCol(self, value: str) -> PCA: ...

class PCAModel(JavaModel, _PCAParams, JavaMLReadable[PCAModel], JavaMLWritable):
    def setInputCol(self, value: str) -> PCAModel: ...
    def setOutputCol(self, value: str) -> PCAModel: ...
    @property
    def pc(self) -> DenseMatrix: ...
    @property
    def explainedVariance(self) -> DenseVector: ...

class _RFormulaParams(HasFeaturesCol, HasLabelCol, HasHandleInvalid):
    formula: Param[str]
    forceIndexLabel: Param[bool]
    stringIndexerOrderType: Param[str]
    handleInvalid: Param[str]
    def __init__(self, *args: Any): ...
    def getFormula(self) -> str: ...
    def getForceIndexLabel(self) -> bool: ...
    def getStringIndexerOrderType(self) -> str: ...

class RFormula(
    JavaEstimator[RFormulaModel],
    _RFormulaParams,
    JavaMLReadable[RFormula],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        formula: Optional[str] = ...,
        featuresCol: str = ...,
        labelCol: str = ...,
        forceIndexLabel: bool = ...,
        stringIndexerOrderType: str = ...,
        handleInvalid: str = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        formula: Optional[str] = ...,
        featuresCol: str = ...,
        labelCol: str = ...,
        forceIndexLabel: bool = ...,
        stringIndexerOrderType: str = ...,
        handleInvalid: str = ...,
    ) -> RFormula: ...
    def setFormula(self, value: str) -> RFormula: ...
    def setForceIndexLabel(self, value: bool) -> RFormula: ...
    def setStringIndexerOrderType(self, value: str) -> RFormula: ...
    def setFeaturesCol(self, value: str) -> RFormula: ...
    def setLabelCol(self, value: str) -> RFormula: ...
    def setHandleInvalid(self, value: str) -> RFormula: ...

class RFormulaModel(JavaModel, _RFormulaParams, JavaMLReadable[RFormulaModel], JavaMLWritable): ...

class _SelectorParams(HasFeaturesCol, HasOutputCol, HasLabelCol):
    selectorType: Param[str]
    numTopFeatures: Param[int]
    percentile: Param[float]
    fpr: Param[float]
    fdr: Param[float]
    fwe: Param[float]
    def __init__(self, *args: Any): ...
    def getSelectorType(self) -> str: ...
    def getNumTopFeatures(self) -> int: ...
    def getPercentile(self) -> float: ...
    def getFpr(self) -> float: ...
    def getFdr(self) -> float: ...
    def getFwe(self) -> float: ...

class _Selector(JavaEstimator[JM], _SelectorParams, JavaMLReadable, JavaMLWritable):
    def setSelectorType(self: P, value: str) -> P: ...
    def setNumTopFeatures(self: P, value: int) -> P: ...
    def setPercentile(self: P, value: float) -> P: ...
    def setFpr(self: P, value: float) -> P: ...
    def setFdr(self: P, value: float) -> P: ...
    def setFwe(self: P, value: float) -> P: ...
    def setFeaturesCol(self: P, value: str) -> P: ...
    def setOutputCol(self: P, value: str) -> P: ...
    def setLabelCol(self: P, value: str) -> P: ...

class _SelectorModel(JavaModel, _SelectorParams):
    def setFeaturesCol(self: P, value: str) -> P: ...
    def setOutputCol(self: P, value: str) -> P: ...
    @property
    def selectedFeatures(self) -> List[int]: ...

class ChiSqSelector(
    _Selector[ChiSqSelectorModel],
    JavaMLReadable[ChiSqSelector],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        numTopFeatures: int = ...,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        labelCol: str = ...,
        selectorType: str = ...,
        percentile: float = ...,
        fpr: float = ...,
        fdr: float = ...,
        fwe: float = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        numTopFeatures: int = ...,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        labelCol: str = ...,
        selectorType: str = ...,
        percentile: float = ...,
        fpr: float = ...,
        fdr: float = ...,
        fwe: float = ...,
    ) -> ChiSqSelector: ...
    def setSelectorType(self, value: str) -> ChiSqSelector: ...
    def setNumTopFeatures(self, value: int) -> ChiSqSelector: ...
    def setPercentile(self, value: float) -> ChiSqSelector: ...
    def setFpr(self, value: float) -> ChiSqSelector: ...
    def setFdr(self, value: float) -> ChiSqSelector: ...
    def setFwe(self, value: float) -> ChiSqSelector: ...
    def setFeaturesCol(self, value: str) -> ChiSqSelector: ...
    def setOutputCol(self, value: str) -> ChiSqSelector: ...
    def setLabelCol(self, value: str) -> ChiSqSelector: ...

class ChiSqSelectorModel(_SelectorModel, JavaMLReadable[ChiSqSelectorModel], JavaMLWritable):
    def setFeaturesCol(self, value: str) -> ChiSqSelectorModel: ...
    def setOutputCol(self, value: str) -> ChiSqSelectorModel: ...
    @property
    def selectedFeatures(self) -> List[int]: ...

class VectorSizeHint(
    JavaTransformer,
    HasInputCol,
    HasHandleInvalid,
    JavaMLReadable[VectorSizeHint],
    JavaMLWritable,
):
    size: Param[int]
    handleInvalid: Param[str]
    def __init__(
        self, *, inputCol: Optional[str] = ..., size: Optional[int] = ..., handleInvalid: str = ...
    ) -> None: ...
    def setParams(
        self, *, inputCol: Optional[str] = ..., size: Optional[int] = ..., handleInvalid: str = ...
    ) -> VectorSizeHint: ...
    def setSize(self, value: int) -> VectorSizeHint: ...
    def getSize(self) -> int: ...
    def setInputCol(self, value: str) -> VectorSizeHint: ...
    def setHandleInvalid(self, value: str) -> VectorSizeHint: ...

class _VarianceThresholdSelectorParams(HasFeaturesCol, HasOutputCol):
    varianceThreshold: Param[float] = ...
    def getVarianceThreshold(self) -> float: ...

class VarianceThresholdSelector(
    JavaEstimator[VarianceThresholdSelectorModel],
    _VarianceThresholdSelectorParams,
    JavaMLReadable[VarianceThresholdSelector],
    JavaMLWritable,
):
    def __init__(
        self,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        varianceThreshold: float = ...,
    ) -> None: ...
    def setParams(
        self,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        varianceThreshold: float = ...,
    ) -> VarianceThresholdSelector: ...
    def setVarianceThreshold(self, value: float) -> VarianceThresholdSelector: ...
    def setFeaturesCol(self, value: str) -> VarianceThresholdSelector: ...
    def setOutputCol(self, value: str) -> VarianceThresholdSelector: ...

class VarianceThresholdSelectorModel(
    JavaModel,
    _VarianceThresholdSelectorParams,
    JavaMLReadable[VarianceThresholdSelectorModel],
    JavaMLWritable,
):
    def setFeaturesCol(self, value: str) -> VarianceThresholdSelectorModel: ...
    def setOutputCol(self, value: str) -> VarianceThresholdSelectorModel: ...
    @property
    def selectedFeatures(self) -> List[int]: ...

class _UnivariateFeatureSelectorParams(HasFeaturesCol, HasOutputCol, HasLabelCol):
    featureType: Param[str] = ...
    labelType: Param[str] = ...
    selectionMode: Param[str] = ...
    selectionThreshold: Param[float] = ...
    def __init__(self, *args: Any): ...
    def getFeatureType(self) -> str: ...
    def getLabelType(self) -> str: ...
    def getSelectionMode(self) -> str: ...
    def getSelectionThreshold(self) -> float: ...

class UnivariateFeatureSelector(
    JavaEstimator[UnivariateFeatureSelectorModel],
    _UnivariateFeatureSelectorParams,
    JavaMLReadable[UnivariateFeatureSelector],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        labelCol: str = ...,
        selectionMode: str = ...,
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        outputCol: Optional[str] = ...,
        labelCol: str = ...,
        selectionMode: str = ...,
    ) -> UnivariateFeatureSelector: ...
    def setFeatureType(self, value: str) -> UnivariateFeatureSelector: ...
    def setLabelType(self, value: str) -> UnivariateFeatureSelector: ...
    def setSelectionMode(self, value: str) -> UnivariateFeatureSelector: ...
    def setSelectionThreshold(self, value: float) -> UnivariateFeatureSelector: ...
    def setFeaturesCol(self, value: str) -> UnivariateFeatureSelector: ...
    def setOutputCol(self, value: str) -> UnivariateFeatureSelector: ...
    def setLabelCol(self, value: str) -> UnivariateFeatureSelector: ...

class UnivariateFeatureSelectorModel(
    JavaModel,
    _UnivariateFeatureSelectorParams,
    JavaMLReadable[UnivariateFeatureSelectorModel],
    JavaMLWritable,
):
    def setFeaturesCol(self, value: str) -> UnivariateFeatureSelectorModel: ...
    def setOutputCol(self, value: str) -> UnivariateFeatureSelectorModel: ...
    @property
    def selectedFeatures(self) -> List[int]: ...

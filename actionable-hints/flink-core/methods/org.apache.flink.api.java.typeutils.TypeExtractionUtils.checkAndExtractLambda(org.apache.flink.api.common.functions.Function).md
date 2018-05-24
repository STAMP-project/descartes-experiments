# checkAndExtractLambda(org.apache.flink.api.common.functions.Function)

**Class:** org.apache.flink.api.java.typeutils.TypeExtractionUtils

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/java/typeutils/TypeExtractionUtils.java#L100)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 80 test method(s) with a minimum stack distance of 3.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return null;
```





## Observed test methods

* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithMissingGenerics() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnUnknownInput() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValueSupertypeException() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleSupertype() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMissingTupleGenerics() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTypeErasure() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionInputInOutputMultipleTimes() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBigBasicTypes() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy2() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInputWithTypeMismatch() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference6() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyOptionGenericType() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValueNested() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputAsSuperclass() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSuperclassInput() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchWithRawFuntion() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicType() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEnumType() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testExtractKeySelector() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithMissingInput() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference2() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleArray() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchExceptions() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArrayWithTypeVariable() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSubclassInput() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference7() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testResultTypeQueryable() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInferenceWithCustomTupleAndRichFunction() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInput() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray2() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput2() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testDualUseOfPojo() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference1() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionInputInOutputMultipleTimes2() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedArrays() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference4() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSameGenericVariable() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference4() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMissingTypeInfo() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithCustomTupleInput() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyEitherGenericType() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputFromInput() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInterface() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testPojo() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValue() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSqlTimeTypes() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputWithCustomTypeInfo() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference3() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArray() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTuple0() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSubclassOfTuple() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPrimitiveArray() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValue() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTuple() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference5() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedPojo() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunction() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics2() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEither() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithNoGenericSuperclass() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleOfValues() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMissingTypeInference() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMultiDimensionalArray() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference3() at distance(s): 4


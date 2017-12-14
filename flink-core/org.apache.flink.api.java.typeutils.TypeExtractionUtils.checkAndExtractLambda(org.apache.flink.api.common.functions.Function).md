# Summary
**org.apache.flink.api.java.typeutils.TypeExtractionUtils.checkAndExtractLambda(org.apache.flink.api.common.functions.Function)**

This method is **strong pseudo-tested**.
It is covered by 80 test(s). 


## Transformations applied

- null


The test suite was not able to detect any transformation applied.

More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 80 test(s).
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSqlTimeTypes()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionInputInOutputMultipleTimes()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValue()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInterface()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithMissingGenerics()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionInputInOutputMultipleTimes2()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference5()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testDualUseOfPojo()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBigBasicTypes()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTypeErasure()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithNoGenericSuperclass()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleSupertype()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSuperclassInput()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithCustomTupleInput()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput2()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValueNested()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference4()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSameGenericVariable()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithMissingInput()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleOfValues()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunction()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMultiDimensionalArray()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testExtractKeySelector()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPrimitiveArray()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSubclassOfTuple()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValueSupertypeException()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy2()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics2()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference3()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArray()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyEitherGenericType()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference7()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputWithCustomTypeInfo()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicType()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchWithRawFuntion()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValue()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTuple0()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInferenceWithCustomTupleAndRichFunction()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnUnknownInput()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchExceptions()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference1()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testPojo()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleArray()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyOptionGenericType()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMissingTypeInference()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference3()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedPojo()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEither()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference4()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInputWithTypeMismatch()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedArrays()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputFromInput()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArrayWithTypeVariable()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEnumType()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference6()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInput()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSubclassInput()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference2()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMissingTypeInfo()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMissingTupleGenerics()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputAsSuperclass()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTuple()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray2()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testResultTypeQueryable()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

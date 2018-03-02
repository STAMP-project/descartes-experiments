# equals(java.lang.Object)

**Class:** org.apache.flink.api.common.typeutils.base.TypeSerializerSingleton

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/TypeSerializerSingleton.java#L46)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 106 test method(s) with a minimum stack distance of 2.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return true;
```

The following transformations were also applied and they were detected by the test suite:

```Java
return false;
```





## Observed test methods

* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 2, 3, 4, 5, 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithComplexHierarchy() at distance(s): 2, 6
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible2() at distance(s): 3
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible9() at distance(s): 3
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible5() at distance(s): 3
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testTuplePojoTestEquality() at distance(s): 3
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible1() at distance(s): 3
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible2() at distance(s): 3
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible4() at distance(s): 3
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible3() at distance(s): 3
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible3() at distance(s): 3
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible8() at distance(s): 3
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoDirect() at distance(s): 3, 6, 9
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible1() at distance(s): 3
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible4() at distance(s): 3
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializabilityAndEquals() at distance(s): 4, 5, 6, 7, 8, 9
* org.apache.flink.api.common.typeutils.TypeSerializerSerializationUtilTest.testSerializerSerialization() at distance(s): 5
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 5
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 5, 6, 7, 8
* org.apache.flink.api.common.state.ListStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 5
* org.apache.flink.api.common.state.ReducingStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 5
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorAutoSerializer() at distance(s): 5
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionInputInOutputMultipleTimes() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBigBasicTypes() at distance(s): 6, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd() at distance(s): 6, 9, 10
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testExtractInputFormatType() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy2() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testMultiLevelDerivedInputFormatType() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicTypes() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference6() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyOptionGenericType() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValueNested() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericsSomeFieldsGeneric() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputAsSuperclass() at distance(s): 6, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchWithRawFuntion() at distance(s): 6
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testGetFlatFields() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicType() at distance(s): 6, 8
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testExtractKeySelector() at distance(s): 6, 7
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testFieldAtStringRef() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass() at distance(s): 6, 9, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference2() at distance(s): 6
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoOf() at distance(s): 6, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes() at distance(s): 6, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleArray() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics() at distance(s): 6, 10, 11
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference() at distance(s): 6, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArrayWithTypeVariable() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCreateTypeInfoFromInstance() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference7() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testResultTypeQueryable() at distance(s): 6, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInferenceWithCustomTupleAndRichFunction() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInput() at distance(s): 6, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray2() at distance(s): 6
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testCustomFieldNames() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference1() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionInputInOutputMultipleTimes2() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedArrays() at distance(s): 6, 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference4() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testSimpleType() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSameGenericVariable() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference4() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithCustomTupleInput() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyEitherGenericType() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputFromInput() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInterface() at distance(s): 6, 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValue() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicArrays() at distance(s): 6, 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSqlTimeTypes() at distance(s): 6, 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference3() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testExtractDerivedInputFormatType() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchy() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSubclassOfTuple() at distance(s): 6, 8, 9
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testTuples() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPrimitiveArray() at distance(s): 6, 7, 8
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTuple() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference5() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testQueryableFormatType() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunction() at distance(s): 6, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics2() at distance(s): 6, 10, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithNoGenericSuperclass() at distance(s): 6, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass() at distance(s): 6, 9, 10
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testGetTypeAt() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass() at distance(s): 6, 9, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference3() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleSupertype() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMissingTupleGenerics() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray() at distance(s): 7, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEither() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testPojo() at distance(s): 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoAllPublic() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testRow() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo() at distance(s): 9
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionTuple() at distance(s): 9
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionTupleAnonymous() at distance(s): 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMultiDimensionalArray() at distance(s): 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes() at distance(s): 13, 16


# canEqual(java.lang.Object)

**Class:** org.apache.flink.api.common.typeutils.base.StringSerializer

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/StringSerializer.java#L84)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 73 test method(s) with a minimum stack distance of 3.

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

* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 3, 4, 5, 6, 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithComplexHierarchy() at distance(s): 3
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible2() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible9() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible5() at distance(s): 4
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testTuplePojoTestEquality() at distance(s): 4
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible1() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible2() at distance(s): 4
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible4() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible3() at distance(s): 4
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible3() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible8() at distance(s): 4
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoDirect() at distance(s): 4, 7, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible1() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible4() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializabilityAndEquals() at distance(s): 5, 6, 7, 8, 9
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 6
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 6, 7
* org.apache.flink.api.common.state.ListStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 6
* org.apache.flink.api.common.state.ReducingStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 6
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorAutoSerializer() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy2() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testMultiLevelDerivedInputFormatType() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicTypes() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValueNested() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchWithRawFuntion() at distance(s): 7
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testGetFlatFields() at distance(s): 7
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() at distance(s): 7
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testFieldAtStringRef() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass() at distance(s): 7, 11
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoOf() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleArray() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy() at distance(s): 7
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testCustomFieldNames() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference1() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSameGenericVariable() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference4() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithCustomTupleInput() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyEitherGenericType() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValue() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testExtractDerivedInputFormatType() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchy() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSubclassOfTuple() at distance(s): 7, 9, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithNoGenericSuperclass() at distance(s): 7, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testGetTypeAt() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference3() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testExtractKeySelector() at distance(s): 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleSupertype() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMissingTupleGenerics() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray() at distance(s): 8, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInterface() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicArrays() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPrimitiveArray() at distance(s): 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEither() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes() at distance(s): 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testResultTypeQueryable() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoAllPublic() at distance(s): 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunction() at distance(s): 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testRow() at distance(s): 9
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference() at distance(s): 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInput() at distance(s): 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes() at distance(s): 14, 17


# hasHadoopWritableInterface(java.lang.Class,java.util.HashSet)

**Class:** org.apache.flink.api.java.typeutils.TypeExtractor

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/java/typeutils/TypeExtractor.java#L2117)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can not be accessed from other classes. 
It has been covered by 145 test method(s) with a minimum stack distance of 5.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return false;
```

The following transformations were also applied and they were detected by the test suite:

```Java
return true;
```





## Observed test methods

* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible2() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBigBasicTypes() at distance(s): 5, 6, 7, 8, 11, 12, 13, 14
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible9() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.common.operators.ExpressionKeysTest.testPojoKeys() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.java.typeutils.runtime.PojoComparatorTest.&lt;init&gt;() at distance(s): 5, 6, 9, 10, 11, 12, 13
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassComparatorTest.&lt;init&gt;() at distance(s): 5, 6, 9, 10, 11, 12, 13
* org.apache.flink.api.common.operators.ExpressionKeysTest.testTupleNonKeyField() at distance(s): 5, 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicType() at distance(s): 5, 6, 7, 10, 11
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible5() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes() at distance(s): 5, 6, 7, 8, 9, 12, 13, 14
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible1() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.common.operators.ExpressionKeysTest.testTupleWithNestedPojo() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.java.typeutils.runtime.SubclassFromInterfaceSerializerTest.&lt;init&gt;() at distance(s): 5
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible2() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testOriginalTypes2() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible6() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.common.serialization.TypeInformationSerializationSchemaTest.testDeSerialization() at distance(s): 5, 6
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassSerializerTest.&lt;init&gt;() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.java.typeutils.CompositeTypeTest.&lt;init&gt;() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible4() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.common.serialization.TypeInformationSerializationSchemaTest.testSerializability() at distance(s): 5, 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testPojo() at distance(s): 5, 6, 7, 9, 10, 11, 14, 15
* org.apache.flink.api.common.operators.ExpressionKeysTest.testNonKeyPojoField() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testRecursivePojoTypeExtraction() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithDifferentPojoType() at distance(s): 5, 6, 7, 9, 10, 11, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSqlTimeTypes() at distance(s): 5, 6, 7, 8, 11, 12, 13, 14
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.&lt;init&gt;() at distance(s): 5, 6, 9, 10, 13, 14
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible7() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible3() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible8() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValue() at distance(s): 5, 6, 7, 8, 9, 10, 11, 12, 13
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testSimplePojoTypeExtraction() at distance(s): 5, 6, 9, 10, 11
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testNestedPojoTypeExtraction() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible1() at distance(s): 5, 6, 9, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible4() at distance(s): 5, 6, 9, 10, 11, 13, 14
* org.apache.flink.api.common.operators.ExpressionKeysTest.testInvalidPojo() at distance(s): 5, 6, 8, 9, 10, 11, 12, 13
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC() at distance(s): 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoAllPublic() at distance(s): 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testRow() at distance(s): 6, 7, 8, 9, 10
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testRecursivePojoObjectTypeExtraction() at distance(s): 6, 7, 10, 11, 12, 14, 15
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testExtractInputFormatType() at distance(s): 7, 8, 9
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testString() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testNestedInterfaces() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testBeanStyleObjects() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testTuplePojoTestEquality() at distance(s): 7, 8, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo() at distance(s): 7, 8, 9, 11, 12, 13, 14, 16, 17
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 7, 8, 9, 11, 12, 13, 14, 15
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSubclassOfTuple() at distance(s): 7, 8, 9, 12, 13, 14
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 7, 8, 9, 11, 12, 13, 14, 15
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testNestedObjects() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testSimpleTypesObjects() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testCompositeObject() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleOfValues() at distance(s): 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo2() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple5CustomObjects() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericsSomeFieldsGeneric() at distance(s): 8, 9, 12
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSuperclassInput() at distance(s): 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericFields() at distance(s): 8, 9, 11, 12
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testDuplicateFieldException() at distance(s): 8, 9, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithRecursiveGenericField() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1() at distance(s): 8, 9, 12
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSubclassInput() at distance(s): 8, 9, 10
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionGeneric() at distance(s): 8, 9, 10, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCreateTypeInfoFromInstance() at distance(s): 8, 9, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo1() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testDualUseOfPojo() at distance(s): 8, 9, 11, 12, 15
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionGenericAnonymous() at distance(s): 8, 9, 10, 11
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojosWithMutualRecursion() at distance(s): 8, 9, 12, 13
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple2StringDouble() at distance(s): 8, 9, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testIncorrectPojos() at distance(s): 8, 9, 12
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple1Int() at distance(s): 8, 9, 10
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testExtractDerivedInputFormatType() at distance(s): 8, 9, 10, 11, 12
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics() at distance(s): 8, 9, 10, 12, 13, 14, 15
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo3() at distance(s): 8, 9, 12, 13
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testCorrectPojos() at distance(s): 8, 9, 10, 12, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedPojo() at distance(s): 8, 9, 10, 13, 14, 15
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple() at distance(s): 8, 9, 10, 11, 12, 13
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple1String() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples() at distance(s): 8, 9, 10, 14, 15, 16
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple2StringStringArray() at distance(s): 8, 9
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testRowSerializerWithComplexTypes() at distance(s): 8, 9, 12, 13
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithComplexHierarchy() at distance(s): 8, 9, 10, 11, 12, 15, 16, 17, 18
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojoWithTypeVariable() at distance(s): 8, 9, 10, 12, 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEnumType() at distance(s): 9, 10, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testExtractKeySelector() at distance(s): 9, 10, 11
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoOf() at distance(s): 9, 10, 11, 12, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValueSupertypeException() at distance(s): 9, 10, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInterface() at distance(s): 9, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy() at distance(s): 9, 10, 11, 12, 13, 14, 15, 16
* org.apache.flink.api.common.state.ReducingStateDescriptorTest.testValueStateDescriptorLazySerializer() at distance(s): 10, 11
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testMultiLevelDerivedInputFormatType() at distance(s): 10, 11, 12
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputAsSuperclass() at distance(s): 10, 11
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureRepopulateNonregisteredSubclassSerializerCache() at distance(s): 10, 11, 12, 14, 15, 16, 18, 19
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes() at distance(s): 10, 11, 14
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 10, 11
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureDifferentSubclassRegistrationOrder() at distance(s): 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoDirect() at distance(s): 10, 11, 12, 13, 14
* org.apache.flink.api.common.state.ReducingStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 10, 11
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSnapshotConfigurationAndReconfigure() at distance(s): 10, 11, 12, 14, 15, 16, 18, 19
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunction() at distance(s): 10, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithNoGenericSuperclass() at distance(s): 10, 11
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithPreviouslyNonregisteredSubclasses() at distance(s): 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testValueStateDescriptorLazySerializer() at distance(s): 10, 11
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2() at distance(s): 11, 12, 13, 14
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopy() at distance(s): 11, 12, 13, 14, 15, 16, 18, 19
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividuallyReusingValues() at distance(s): 11, 12, 13, 14, 15, 16, 18, 19
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyAsSequence() at distance(s): 11, 12, 13, 14, 15, 16, 18, 19
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference2() at distance(s): 11, 12, 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceNoReuse() at distance(s): 11, 12, 13, 14, 15, 16, 18, 19
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividually() at distance(s): 11, 12, 13, 14, 15, 16, 18, 19
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorLazySerializer() at distance(s): 11, 12
* org.apache.flink.api.common.state.ListStateDescriptorTest.testValueStateDescriptorLazySerializer() at distance(s): 11, 12
* org.apache.flink.api.common.state.ListStateDescriptorTest.testValueStateDescriptorAutoSerializer() at distance(s): 11, 12
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceReusingValues() at distance(s): 11, 12, 13, 14, 15, 16, 18, 19
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchy() at distance(s): 11, 12
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyIndividually() at distance(s): 11, 12, 13, 14, 15, 16, 18, 19
* org.apache.flink.api.java.typeutils.runtime.MultidimensionalArraySerializerTest.testObjectArrays() at distance(s): 11, 12, 15, 16
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorAutoSerializer() at distance(s): 11, 12, 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd() at distance(s): 12, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass() at distance(s): 12, 13, 14
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEqualityWithReference() at distance(s): 12, 13, 14, 16, 17, 18, 19, 20
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics() at distance(s): 12, 13, 14, 15, 16
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInferenceWithCustomTupleAndRichFunction() at distance(s): 12, 13, 14, 15, 16
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput2() at distance(s): 12, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedArrays() at distance(s): 12, 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSameGenericVariable() at distance(s): 12, 13
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyEitherGenericType() at distance(s): 12, 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput() at distance(s): 12, 13, 14, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoReusedElements() at distance(s): 12, 13, 14, 15, 16, 17, 18, 19
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics2() at distance(s): 12, 13, 16, 17, 18, 19
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEither() at distance(s): 12, 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass() at distance(s): 12, 13, 14
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass() at distance(s): 12, 13, 14
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoNewElements() at distance(s): 12, 13, 14, 15, 16, 17, 18, 19
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleArray() at distance(s): 13, 14
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testInequality() at distance(s): 13, 14, 15, 17, 18, 19, 20, 21
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArray() at distance(s): 13, 14
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEquality() at distance(s): 13, 14, 15, 17, 18, 19, 20, 21
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMultiDimensionalArray() at distance(s): 13, 14, 15, 18, 19, 22, 23
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializabilityAndEquals() at distance(s): 14, 15, 16, 18, 19
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference() at distance(s): 14, 15, 16, 17
* org.apache.flink.api.common.typeutils.SerializerTestBase.testConfigSnapshotInstantiation() at distance(s): 14, 15, 16, 18, 19
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTuple() at distance(s): 14, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testGetLength() at distance(s): 14, 15, 16, 18, 19


# hasSuperclass(java.lang.Class,java.lang.String)

**Class:** org.apache.flink.api.java.typeutils.TypeExtractionUtils

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/java/typeutils/TypeExtractionUtils.java#L318)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 95 test method(s) with a minimum stack distance of 3.

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

* org.apache.flink.api.java.typeutils.runtime.kryo.SerializersTest.testTypeRegistration() at distance(s): 3, 5, 6, 7, 9, 11
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible2() at distance(s): 4, 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible9() at distance(s): 4, 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testPojoKeys() at distance(s): 4, 8
* org.apache.flink.api.java.typeutils.runtime.PojoComparatorTest.&lt;init&gt;() at distance(s): 4
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassComparatorTest.&lt;init&gt;() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testTupleNonKeyField() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible5() at distance(s): 4, 8
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible1() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes() at distance(s): 4, 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testTupleWithNestedPojo() at distance(s): 4, 8
* org.apache.flink.api.java.typeutils.runtime.SubclassFromInterfaceSerializerTest.&lt;init&gt;() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible2() at distance(s): 4
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testOriginalTypes2() at distance(s): 4, 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible6() at distance(s): 4
* org.apache.flink.api.common.serialization.TypeInformationSerializationSchemaTest.testDeSerialization() at distance(s): 4
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassSerializerTest.&lt;init&gt;() at distance(s): 4
* org.apache.flink.api.java.typeutils.CompositeTypeTest.&lt;init&gt;() at distance(s): 4
* org.apache.flink.api.java.typeutils.runtime.kryo.SerializersTest.testTypeRegistrationFromTypeInfo() at distance(s): 4, 6, 7, 8, 10, 12
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible4() at distance(s): 4, 8
* org.apache.flink.api.common.serialization.TypeInformationSerializationSchemaTest.testSerializability() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testPojo() at distance(s): 4, 5, 9
* org.apache.flink.api.common.operators.ExpressionKeysTest.testNonKeyPojoField() at distance(s): 4, 8
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testRecursivePojoTypeExtraction() at distance(s): 4, 8
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithDifferentPojoType() at distance(s): 4, 8
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.&lt;init&gt;() at distance(s): 4, 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible7() at distance(s): 4
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible3() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible8() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testSimplePojoTypeExtraction() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testNestedPojoTypeExtraction() at distance(s): 4, 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible1() at distance(s): 4
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible4() at distance(s): 4, 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testInvalidPojo() at distance(s): 4, 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC() at distance(s): 5, 7, 9, 11, 12, 14
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoAllPublic() at distance(s): 5, 7, 8, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testRow() at distance(s): 5
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testRecursivePojoObjectTypeExtraction() at distance(s): 5, 9
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testNestedInterfaces() at distance(s): 6
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testBeanStyleObjects() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo() at distance(s): 6, 11
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 6
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 6
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testNestedObjects() at distance(s): 6
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testSimpleTypesObjects() at distance(s): 6
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testCompositeObject() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo2() at distance(s): 7
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple5CustomObjects() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericsSomeFieldsGeneric() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSuperclassInput() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericFields() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testDuplicateFieldException() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithRecursiveGenericField() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericTypeWithSubclassInput() at distance(s): 7
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionGeneric() at distance(s): 7, 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo1() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testDualUseOfPojo() at distance(s): 7, 10
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionGenericAnonymous() at distance(s): 7, 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojosWithMutualRecursion() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testIncorrectPojos() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo3() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testCorrectPojos() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedPojo() at distance(s): 7, 8
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testRowSerializerWithComplexTypes() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithComplexHierarchy() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojoWithTypeVariable() at distance(s): 7, 11
* org.apache.flink.api.common.state.ReducingStateDescriptorTest.testValueStateDescriptorLazySerializer() at distance(s): 9
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureRepopulateNonregisteredSubclassSerializerCache() at distance(s): 9, 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes() at distance(s): 9
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureDifferentSubclassRegistrationOrder() at distance(s): 9, 11, 13, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSnapshotConfigurationAndReconfigure() at distance(s): 9, 13
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithPreviouslyNonregisteredSubclasses() at distance(s): 9, 11, 13, 15
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testValueStateDescriptorLazySerializer() at distance(s): 9
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopy() at distance(s): 10, 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividuallyReusingValues() at distance(s): 10, 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyAsSequence() at distance(s): 10, 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceNoReuse() at distance(s): 10, 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividually() at distance(s): 10, 13
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorLazySerializer() at distance(s): 10
* org.apache.flink.api.common.state.ListStateDescriptorTest.testValueStateDescriptorLazySerializer() at distance(s): 10
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceReusingValues() at distance(s): 10, 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyIndividually() at distance(s): 10, 13
* org.apache.flink.api.java.typeutils.runtime.MultidimensionalArraySerializerTest.testObjectArrays() at distance(s): 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEqualityWithReference() at distance(s): 11
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoReusedElements() at distance(s): 11, 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoNewElements() at distance(s): 11, 13
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testInequality() at distance(s): 12
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArray() at distance(s): 12
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEquality() at distance(s): 12
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializabilityAndEquals() at distance(s): 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testConfigSnapshotInstantiation() at distance(s): 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testGetLength() at distance(s): 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMultiDimensionalArray() at distance(s): 17


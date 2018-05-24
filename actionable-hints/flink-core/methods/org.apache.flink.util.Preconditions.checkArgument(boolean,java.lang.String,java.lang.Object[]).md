# checkArgument(boolean,java.lang.String,java.lang.Object[])

**Class:** org.apache.flink.util.Preconditions

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/util/Preconditions.java#L160)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 94 test method(s) with a minimum stack distance of 2.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput2() at distance(s): 2
* org.apache.flink.api.java.typeutils.ValueTypeInfoTest.testValueTypeEqualsWithNull() at distance(s): 2
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC() at distance(s): 3, 7, 9, 11, 13, 15, 17
* org.apache.flink.api.common.operators.ExpressionKeysTest.testBasicType() at distance(s): 3, 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference6() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1() at distance(s): 4, 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference7() at distance(s): 4
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference4() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testPojoType() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testMultiDimensionalArray() at distance(s): 4, 5
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 4, 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference3() at distance(s): 4
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 4, 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference5() at distance(s): 4, 5
* org.apache.flink.api.java.typeutils.runtime.MultidimensionalArraySerializerTest.testGenericObjectArrays() at distance(s): 4
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMultiDimensionalArray() at distance(s): 4, 19
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValueSupertypeException() at distance(s): 5, 8, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchExceptions() at distance(s): 5, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingPartialOnInput() at distance(s): 5, 9, 13
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testValue() at distance(s): 5, 6, 7, 8, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple() at distance(s): 5, 7
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible2() at distance(s): 6, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible9() at distance(s): 6, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testPojoKeys() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.runtime.PojoComparatorTest.&lt;init&gt;() at distance(s): 6
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassComparatorTest.&lt;init&gt;() at distance(s): 6
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible5() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testValueTypes() at distance(s): 6
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible1() at distance(s): 6
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes() at distance(s): 6, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testTupleWithNestedPojo() at distance(s): 6, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible2() at distance(s): 6
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testOriginalTypes2() at distance(s): 6, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible6() at distance(s): 6
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassSerializerTest.&lt;init&gt;() at distance(s): 6
* org.apache.flink.api.java.typeutils.CompositeTypeTest.&lt;init&gt;() at distance(s): 6
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible4() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testPojoType2() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testPojo() at distance(s): 6, 7, 11
* org.apache.flink.api.common.operators.ExpressionKeysTest.testNonKeyPojoField() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testRecursivePojoTypeExtraction() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithDifferentPojoType() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.&lt;init&gt;() at distance(s): 6, 7, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible7() at distance(s): 6
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible3() at distance(s): 6
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible8() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testSimplePojoTypeExtraction() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testNestedPojoTypeExtraction() at distance(s): 6, 10
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible1() at distance(s): 6
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleOfValues() at distance(s): 6, 8, 10, 13
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible4() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testLargeMixedTuple() at distance(s): 6
* org.apache.flink.api.common.operators.ExpressionKeysTest.testInvalidPojo() at distance(s): 6, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoAllPublic() at distance(s): 7, 9, 11, 13
* org.apache.flink.api.java.typeutils.PojoTypeInformationTest.testRecursivePojoObjectTypeExtraction() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo() at distance(s): 8, 13
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo2() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericsSomeFieldsGeneric() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericFields() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithRecursiveGenericField() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo1() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testDualUseOfPojo() at distance(s): 9, 12
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojosWithMutualRecursion() at distance(s): 9, 13
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testIncorrectPojos() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojo3() at distance(s): 9, 13
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testCorrectPojos() at distance(s): 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedPojo() at distance(s): 9, 10
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testRowSerializerWithComplexTypes() at distance(s): 9
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithComplexHierarchy() at distance(s): 9, 12
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testRecursivePojoWithTypeVariable() at distance(s): 9, 13
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureRepopulateNonregisteredSubclassSerializerCache() at distance(s): 11, 15
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes() at distance(s): 11
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureDifferentSubclassRegistrationOrder() at distance(s): 11, 13, 15, 17
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSnapshotConfigurationAndReconfigure() at distance(s): 11, 15
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithPreviouslyNonregisteredSubclasses() at distance(s): 11, 13, 15, 17
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopy() at distance(s): 12, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividuallyReusingValues() at distance(s): 12, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyAsSequence() at distance(s): 12, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceNoReuse() at distance(s): 12, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividually() at distance(s): 12, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceReusingValues() at distance(s): 12, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyIndividually() at distance(s): 12, 15
* org.apache.flink.api.java.typeutils.runtime.MultidimensionalArraySerializerTest.testObjectArrays() at distance(s): 12
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEqualityWithReference() at distance(s): 13
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoReusedElements() at distance(s): 13, 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoNewElements() at distance(s): 13, 15
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testInequality() at distance(s): 14
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEquality() at distance(s): 14
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializabilityAndEquals() at distance(s): 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testConfigSnapshotInstantiation() at distance(s): 15
* org.apache.flink.api.common.typeutils.SerializerTestBase.testGetLength() at distance(s): 15


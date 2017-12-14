# Summary
**org.apache.flink.api.common.typeutils.base.IntSerializer.canEqual(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 62 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 62 test(s).
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible2() (Distance: 4)
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible4() (Distance: 4)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicTypes() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testTuples() (Distance: 7)
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testGetFlatFields() (Distance: 7)
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testFieldAtStringRef() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testMultiLevelDerivedInputFormatType() (Distance: 7)
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicArrays() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple1Int() (Distance: 10)
* org.apache.flink.api.common.typeinfo.BasicArrayTypeInfoTest.testSerialization()
* org.apache.flink.api.common.typeutils.TypeSerializerSerializationUtilTest.org.apache.flink.api.common.typeutils.TypeSerializerSerializationUtilTest
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference7()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible4()
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.common.typeinfo.BasicTypeInfoTest.testSerialization()
* org.apache.flink.api.common.typeinfo.IntegerTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes()
* org.apache.flink.api.common.typeutils.base.IntSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1()
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.runtime.MultidimensionalArraySerializerTest.testObjectArrays()
* org.apache.flink.api.java.typeutils.MapTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenericsSomeFieldsGeneric()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testPojo()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy()
* org.apache.flink.api.java.typeutils.EitherTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.common.typeinfo.IntegerTypeInfoTest.testSerialization()
* org.apache.flink.api.common.typeinfo.BasicTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics()
* org.apache.flink.api.java.typeutils.MultisetTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass()
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testRowSerializerWithComplexTypes()
* org.apache.flink.api.common.typeinfo.NumericTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible9()
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testTuplePojoTestEquality()
* org.apache.flink.api.common.typeinfo.NumericTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCreateTypeInfoFromInstance()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference6()
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testRowSerializer()
* org.apache.flink.api.java.typeutils.PojoTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testRow()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMultiDimensionalArray()
* org.apache.flink.api.common.typeinfo.BasicArrayTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithComplexHierarchy()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testExtractKeySelector()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPrimitiveArray()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSubclassOfTuple()
* org.apache.flink.api.java.typeutils.TupleTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.TupleTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics()
* org.apache.flink.api.java.typeutils.EitherTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testSimpleType()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testResultTypeQueryable()
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testLargeRowSerializer()
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics2()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

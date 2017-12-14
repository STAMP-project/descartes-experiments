# Summary
**org.apache.flink.api.common.typeutils.base.LongSerializer.canEqual(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 35 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 35 test(s).
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorAutoSerializer() (Distance: 6)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicTypes() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testTuples() (Distance: 7)
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testGetFlatFields() (Distance: 7)
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testFieldAtStringRef() (Distance: 7)
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicArrays() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.EitherSerializerTest.testEitherWithTuple() (Distance: 10)
* org.apache.flink.api.common.typeinfo.BasicArrayTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass()
* org.apache.flink.api.common.typeinfo.BasicTypeInfoTest.testSerialization()
* org.apache.flink.api.common.typeinfo.IntegerTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.common.typeutils.base.ListSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInferenceWithCustomTupleAndRichFunction()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC()
* org.apache.flink.api.common.typeinfo.IntegerTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd()
* org.apache.flink.api.common.typeinfo.BasicTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass()
* org.apache.flink.api.java.typeutils.MultisetTypeInfoTest.testSerialization()
* org.apache.flink.api.common.typeutils.base.LongSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.common.typeinfo.NumericTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass()
* org.apache.flink.api.common.typeinfo.NumericTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCreateTypeInfoFromInstance()
* org.apache.flink.api.common.typeutils.base.MapSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.common.typeinfo.BasicArrayTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference2()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples()
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassSerializerTest.testSerializabilityAndEquals()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

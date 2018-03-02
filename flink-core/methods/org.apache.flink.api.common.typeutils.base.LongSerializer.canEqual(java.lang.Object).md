# canEqual(java.lang.Object)

**Class:** org.apache.flink.api.common.typeutils.base.LongSerializer

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/LongSerializer.java#L83)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 24 test method(s) with a minimum stack distance of 3.

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

* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 3, 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializabilityAndEquals() at distance(s): 5, 6, 8, 9
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 6, 7
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorAutoSerializer() at distance(s): 6
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicTypes() at distance(s): 7
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testGetFlatFields() at distance(s): 7
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() at distance(s): 7
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testFieldAtStringRef() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference2() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCreateTypeInfoFromInstance() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInferenceWithCustomTupleAndRichFunction() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testTuples() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples() at distance(s): 7, 11
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicArrays() at distance(s): 8
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPojo() at distance(s): 10


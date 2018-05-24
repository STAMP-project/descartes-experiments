# createInstance()

**Class:** org.apache.flink.api.common.typeutils.base.array.IntPrimitiveArraySerializer

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/array/IntPrimitiveArraySerializer.java#L47)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `new int[]`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 12 test method(s) with a minimum stack distance of 2.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return new int[];
```

The following transformations were also applied and they were detected by the test suite:

```Java
return null;
```





## Observed test methods

* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividuallyReusingValues() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyAsSequence() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEqualityWithReference() at distance(s): 2
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividually() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoReusedElements() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceReusingValues() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyIndividually() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testInstantiate() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoNewElements() at distance(s): 2, 4, 6
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testInequality() at distance(s): 4
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEquality() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceNoReuse() at distance(s): 5, 6, 7


# getRandomString(java.util.Random,int,int)

**Class:** org.apache.flink.util.StringUtils

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/util/StringUtils.java#L219)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `&quot;&quot;`, `&quot;A&quot;`


It can be accessed from other classes and it is directly covered by the test suite. 
It has been covered by 24 test method(s).

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return "";
```

```Java
return "A";
```

The following transformations were also applied and they were detected by the test suite:

```Java
return null;
```





## Observed test methods

* org.apache.flink.types.StringSerializationTest.testLongValues() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericArraySerializerTest.testString() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple5CustomObjects() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testString() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple1StringArray() at distance(s): 1
* org.apache.flink.types.StringSerializationTest.testMixedValues() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple2StringDouble() at distance(s): 1
* org.apache.flink.types.StringValueSerializationTest.testLongValues() at distance(s): 1
* org.apache.flink.types.StringValueSerializationTest.testBinaryCopyOfLongStrings() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericArraySerializerTest.testSimpleTypesObjects() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple1String() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple2StringStringArray() at distance(s): 1
* org.apache.flink.api.java.typeutils.runtime.AbstractGenericTypeSerializerTest.testSimpleTypesObjects() at distance(s): 1
* org.apache.flink.types.StringSerializationTest.testBinaryCopyOfLongStrings() at distance(s): 1
* org.apache.flink.types.StringValueSerializationTest.testMixedValues() at distance(s): 1
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopy() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividuallyReusingValues() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyAsSequence() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceNoReuse() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividually() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoReusedElements() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceReusingValues() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyIndividually() at distance(s): 4
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoNewElements() at distance(s): 4


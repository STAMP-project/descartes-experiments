# getSerializationFormatIdentifier()

**Class:** org.apache.flink.api.common.typeutils.base.TypeSerializerSingleton

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/TypeSerializerSingleton.java#L81)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `&quot;&quot;`, `&quot;A&quot;`


It can not be accessed from other classes. 
It has been covered by 9 test method(s) with a minimum stack distance of 2.

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

* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithDifferentFieldOrder() at distance(s): 2, 5, 6, 7, 8
* org.apache.flink.api.common.typeutils.TypeSerializerSerializationUtilTest.testSerializerAndConfigPairsSerializationWithSerializerDeserializationFailures() at distance(s): 2
* org.apache.flink.api.common.typeutils.SerializerTestBase.testConfigSnapshotInstantiation() at distance(s): 2, 5, 6, 8
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSnapshotConfigurationAndReconfigure() at distance(s): 2, 3, 4, 5, 6, 7, 8
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureRepopulateNonregisteredSubclassSerializerCache() at distance(s): 4, 5, 6, 7, 8, 9, 10
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testSerializerSerializationFailureResilience() at distance(s): 4, 5, 6, 7, 8
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithDifferentPojoType() at distance(s): 4, 7
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureDifferentSubclassRegistrationOrder() at distance(s): 4, 5, 6, 7, 8, 9, 10
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithPreviouslyNonregisteredSubclasses() at distance(s): 4, 5, 6, 7, 8, 9, 10


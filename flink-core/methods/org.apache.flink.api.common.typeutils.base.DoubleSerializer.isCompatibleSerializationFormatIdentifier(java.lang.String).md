# isCompatibleSerializationFormatIdentifier(java.lang.String)

**Class:** org.apache.flink.api.common.typeutils.base.DoubleSerializer

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/DoubleSerializer.java#L88)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 6 test method(s) with a minimum stack distance of 2.

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

* org.apache.flink.api.common.typeutils.SerializerTestBase.testSnapshotConfigurationAndReconfigure() at distance(s): 2, 4, 6
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithDifferentFieldOrder() at distance(s): 4, 6
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureRepopulateNonregisteredSubclassSerializerCache() at distance(s): 4, 6, 8
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testSerializerSerializationFailureResilience() at distance(s): 4, 6
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureDifferentSubclassRegistrationOrder() at distance(s): 4, 6, 8
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testReconfigureWithPreviouslyNonregisteredSubclasses() at distance(s): 4, 6, 8


# equals(java.lang.Object)

**Class:** org.apache.flink.api.common.typeutils.CompositeType

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/CompositeType.java#L280)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 11 test method(s) with a minimum stack distance of 2.

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

* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 2, 3, 4
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 5, 6, 7
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testFieldAtStringRef() at distance(s): 6, 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testRow() at distance(s): 6
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoOf() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference() at distance(s): 7
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionTuple() at distance(s): 7
* org.apache.flink.api.common.serialization.AbstractDeserializationSchemaTest.testTypeExtractionTupleAnonymous() at distance(s): 7
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoDirect() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy() at distance(s): 8
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes() at distance(s): 10, 13


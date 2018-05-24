# invertNormalizedKey()

**Class:** org.apache.flink.api.common.typeutils.base.BasicTypeComparator

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/BasicTypeComparator.java#L75)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 15 test method(s) with a minimum stack distance of 5.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return false;
```

```Java
return true;
```





## Observed test methods

* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testTuplePojoTestEquality() at distance(s): 5
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testNormalizedKeysGreatSmallFullLength() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEqualityWithReference() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testKeyExtraction() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testNormalizedKeyReadWriter() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testNormalizedKeysEqualsHalfLength() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testNormalizedKeysGreatSmallAscDescHalfLength() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testNormalizedKeysEqualsFullLength() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.java.typeutils.runtime.tuple.base.TuplePairComparatorTestBase.testEqualityWithReference() at distance(s): 6
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testDuplicate() at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testNormalizedKeysEquals(boolean) at distance(s): 6, 8, 9, 10
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testInequalityWithReference() at distance(s): 7, 9, 10, 11
* org.apache.flink.api.java.typeutils.runtime.tuple.base.TuplePairComparatorTestBase.testInequalityWithReference() at distance(s): 7
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testInequality() at distance(s): 7, 9, 10, 11
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEquality() at distance(s): 7, 9, 10, 11


# canEqual(java.lang.Object)

**Class:** org.apache.flink.api.common.typeutils.base.BooleanSerializer

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/typeutils/base/BooleanSerializer.java#L83)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 29 test method(s) with a minimum stack distance of 3.

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

* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testSerialization() at distance(s): 3, 4, 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializabilityAndEquals() at distance(s): 5, 8
* org.apache.flink.api.common.typeutils.TypeInformationTestBase.testHashcodeAndEquals() at distance(s): 6, 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference2() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicTypes() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyOptionGenericType() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputAsSuperclass() at distance(s): 7, 9
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicType() at distance(s): 7, 9
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference2() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testCustomArrayWithTypeVariable() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInput() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray2() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testParameterizedArrays() at distance(s): 7, 10
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyEitherGenericType() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputFromInput() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInterface() at distance(s): 7
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference3() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchy() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTuple() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunction() at distance(s): 7
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics2() at distance(s): 7, 11, 15
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicArrays() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy() at distance(s): 8
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEither() at distance(s): 8
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoOf() at distance(s): 10
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoDirect() at distance(s): 10


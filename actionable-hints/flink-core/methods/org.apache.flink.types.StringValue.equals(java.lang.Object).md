# equals(java.lang.Object)

**Class:** org.apache.flink.types.StringValue

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/types/StringValue.java#L581)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes and it is directly covered by the test suite. 
It has been covered by 28 test method(s).

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

* org.apache.flink.types.RecordTest.testAllRetrievalMethods(org.apache.flink.types.Record,int[],org.apache.flink.types.Value[]) at distance(s): 1
* org.apache.flink.types.RecordTest.testAddField() at distance(s): 1
* org.apache.flink.types.PrimitiveDataTypeTest.testStringValue() at distance(s): 1
* org.apache.flink.types.RecordTest.testDeSerialization() at distance(s): 1
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEqualityWithReference() at distance(s): 3
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testDuplicate() at distance(s): 3
* org.apache.flink.types.parser.ParserTestBase.testConcatenated() at distance(s): 4
* org.apache.flink.types.parser.ParserTestBase.testValidStringInIsolation() at distance(s): 4
* org.apache.flink.types.parser.ParserTestBase.testConcatenatedMultiCharDelimiter() at distance(s): 4
* org.apache.flink.types.parser.ParserTestBase.testInValidStringsMixedIn() at distance(s): 4
* org.apache.flink.types.parser.ParserTestBase.testValidStringInIsolationWithEndDelimiter() at distance(s): 4
* org.apache.flink.util.StringValueUtilsTest.testToLowerCaseConverting() at distance(s): 5
* org.apache.flink.types.CopyableValueTest.testCopyTo() at distance(s): 5
* org.apache.flink.types.JavaToValueConverterTest.testJavaToValueConversion() at distance(s): 5
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopy() at distance(s): 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividuallyReusingValues() at distance(s): 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyAsSequence() at distance(s): 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceNoReuse() at distance(s): 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeIndividually() at distance(s): 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoReusedElements() at distance(s): 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializeAsSequenceReusingValues() at distance(s): 5, 6
* org.apache.flink.api.common.typeutils.SerializerTestBase.testSerializedCopyIndividually() at distance(s): 5, 6
* org.apache.flink.util.StringValueUtilsTest.testReplaceNonWordChars() at distance(s): 5
* org.apache.flink.types.CopyableValueTest.testCopy() at distance(s): 5
* org.apache.flink.api.common.typeutils.SerializerTestBase.testCopyIntoNewElements() at distance(s): 5, 6
* org.apache.flink.types.RecordTest.testUnionFields() at distance(s): 6
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testInequality() at distance(s): 7
* org.apache.flink.api.common.typeutils.ComparatorTestBase.testEquality() at distance(s): 7


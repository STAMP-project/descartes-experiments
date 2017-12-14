# Summary
**org.apache.flink.types.StringValue.equals(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 42 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 42 test(s).
* org.apache.flink.types.RecordTest.testDeSerialization() (Distance: 1)
* org.apache.flink.types.RecordTest.testAddField() (Distance: 1)
* org.apache.flink.types.RecordTest.blackBoxTests() (Distance: 3)
* org.apache.flink.types.CopyableValueTest.testCopy() (Distance: 5)
* org.apache.flink.types.CopyableValueTest.testCopyTo() (Distance: 5)
* org.apache.flink.types.JavaToValueConverterTest.testJavaToValueConversion() (Distance: 5)
* org.apache.flink.types.RecordTest.testUnionFields() (Distance: 6)
* org.apache.flink.api.java.typeutils.runtime.EitherSerializerTest.testStringValueDoubleValueEither() (Distance: 8)
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testCopyIntoReusedElements()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testSerializeIndividuallyReusingValues()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testSerializeAsSequenceNoReuse()
* org.apache.flink.api.common.typeutils.base.StringValueComparatorTest.testEquality()
* org.apache.flink.api.java.typeutils.runtime.CopyableValueComparatorTest.testEqualityWithReference()
* org.apache.flink.api.java.typeutils.runtime.CopyableValueComparatorTest.testEquality()
* org.apache.flink.types.PrimitiveDataTypeTest.testStringValue()
* org.apache.flink.types.parser.QuotedStringValueParserTest.testInValidStringsMixedIn()
* org.apache.flink.api.java.typeutils.runtime.ValueComparatorTest.testEqualityWithReference()
* org.apache.flink.api.java.typeutils.runtime.ValueComparatorTest.testInequality()
* org.apache.flink.api.common.typeutils.base.StringValueComparatorTest.testEqualityWithReference()
* org.apache.flink.types.parser.QuotedStringValueParserTest.testConcatenated()
* org.apache.flink.api.java.typeutils.runtime.ValueComparatorTest.testDuplicate()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testSerializedCopyIndividually()
* org.apache.flink.api.common.typeutils.base.StringValueComparatorTest.testInequality()
* org.apache.flink.types.parser.QuotedStringValueParserTest.testValidStringInIsolation()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testSerializeAsSequenceReusingValues()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testSerializeIndividually()
* org.apache.flink.types.parser.UnquotedStringValueParserTest.testConcatenated()
* org.apache.flink.types.parser.QuotedStringValueParserTest.testValidStringInIsolationWithEndDelimiter()
* org.apache.flink.types.RecordITCase.massiveRandomBlackBoxTests()
* org.apache.flink.types.parser.UnquotedStringValueParserTest.testConcatenatedMultiCharDelimiter()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testCopyIntoNewElements()
* org.apache.flink.api.common.typeutils.base.StringValueComparatorTest.testDuplicate()
* org.apache.flink.types.parser.UnquotedStringValueParserTest.testValidStringInIsolationWithEndDelimiter()
* org.apache.flink.api.java.typeutils.runtime.CopyableValueComparatorTest.testDuplicate()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testCopy()
* org.apache.flink.api.java.typeutils.runtime.CopyableValueComparatorTest.testInequality()
* org.apache.flink.api.common.typeutils.base.StringValueSerializerTest.testSerializedCopyAsSequence()
* org.apache.flink.util.StringValueUtilsTest.testReplaceNonWordChars()
* org.apache.flink.util.StringValueUtilsTest.testToLowerCaseConverting()
* org.apache.flink.types.parser.UnquotedStringValueParserTest.testValidStringInIsolation()
* org.apache.flink.api.java.typeutils.runtime.ValueComparatorTest.testEquality()
* org.apache.flink.types.parser.QuotedStringValueParserTest.testConcatenatedMultiCharDelimiter()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

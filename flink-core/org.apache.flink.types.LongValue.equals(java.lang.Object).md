# Summary
**org.apache.flink.types.LongValue.equals(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 24 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 24 test(s).
* org.apache.flink.types.RecordTest.blackBoxTests() (Distance: 3)
* org.apache.flink.types.CopyableValueTest.testCopy() (Distance: 5)
* org.apache.flink.types.CopyableValueTest.testCopyTo() (Distance: 5)
* org.apache.flink.types.JavaToValueConverterTest.testJavaToValueConversion() (Distance: 5)
* org.apache.flink.api.java.typeutils.runtime.EitherSerializerTest.testEitherWithTupleValues() (Distance: 9)
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testCopyIntoNewElements()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testSerializedCopyIndividually()
* org.apache.flink.types.parser.LongValueParserTest.testInValidStringsMixedIn()
* org.apache.flink.api.common.typeutils.base.LongValueComparatorTest.testEqualityWithReference()
* org.apache.flink.types.RecordITCase.massiveRandomBlackBoxTests()
* org.apache.flink.types.parser.LongValueParserTest.testValidStringInIsolation()
* org.apache.flink.types.parser.LongValueParserTest.testConcatenated()
* org.apache.flink.api.common.typeutils.base.LongValueComparatorTest.testDuplicate()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testSerializedCopyAsSequence()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testCopyIntoReusedElements()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testSerializeIndividually()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testCopy()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testSerializeAsSequenceNoReuse()
* org.apache.flink.api.common.typeutils.base.LongValueComparatorTest.testEquality()
* org.apache.flink.api.common.typeutils.base.LongValueComparatorTest.testInequality()
* org.apache.flink.types.parser.LongValueParserTest.testConcatenatedMultiCharDelimiter()
* org.apache.flink.types.parser.LongValueParserTest.testValidStringInIsolationWithEndDelimiter()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testSerializeAsSequenceReusingValues()
* org.apache.flink.api.common.typeutils.base.LongValueSerializerTest.testSerializeIndividuallyReusingValues()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

# Summary
**org.apache.flink.types.IntValue.equals(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 26 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 26 test(s).
* org.apache.flink.types.RecordTest.testDeSerialization() (Distance: 1)
* org.apache.flink.types.RecordTest.testAddField() (Distance: 1)
* org.apache.flink.types.RecordTest.blackBoxTests() (Distance: 3)
* org.apache.flink.types.CopyableValueTest.testCopy() (Distance: 5)
* org.apache.flink.types.CopyableValueTest.testCopyTo() (Distance: 5)
* org.apache.flink.types.JavaToValueConverterTest.testJavaToValueConversion() (Distance: 5)
* org.apache.flink.types.RecordTest.testUnionFields() (Distance: 6)
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testSerializeIndividuallyReusingValues()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testCopyIntoNewElements()
* org.apache.flink.types.parser.IntValueParserTest.testConcatenated()
* org.apache.flink.types.parser.IntValueParserTest.testValidStringInIsolation()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testSerializeAsSequenceReusingValues()
* org.apache.flink.types.parser.IntValueParserTest.testValidStringInIsolationWithEndDelimiter()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testSerializeIndividually()
* org.apache.flink.types.RecordITCase.massiveRandomBlackBoxTests()
* org.apache.flink.types.parser.IntValueParserTest.testConcatenatedMultiCharDelimiter()
* org.apache.flink.api.common.typeutils.base.IntValueComparatorTest.testDuplicate()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testSerializedCopyAsSequence()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testCopyIntoReusedElements()
* org.apache.flink.api.common.typeutils.base.IntValueComparatorTest.testInequality()
* org.apache.flink.api.common.typeutils.base.IntValueComparatorTest.testEquality()
* org.apache.flink.api.common.typeutils.base.IntValueComparatorTest.testEqualityWithReference()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testSerializedCopyIndividually()
* org.apache.flink.types.parser.IntValueParserTest.testInValidStringsMixedIn()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testSerializeAsSequenceNoReuse()
* org.apache.flink.api.common.typeutils.base.IntValueSerializerTest.testCopy()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

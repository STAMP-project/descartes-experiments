# Summary
**org.apache.flink.types.DoubleValue.equals(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 27 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 27 test(s).
* org.apache.flink.types.RecordTest.testAddField() (Distance: 1)
* org.apache.flink.types.RecordTest.blackBoxTests() (Distance: 3)
* org.apache.flink.util.InstantiationUtilTest.testSerializationToByteArray() (Distance: 4)
* org.apache.flink.types.CopyableValueTest.testCopy() (Distance: 5)
* org.apache.flink.types.CopyableValueTest.testCopyTo() (Distance: 5)
* org.apache.flink.types.JavaToValueConverterTest.testJavaToValueConversion() (Distance: 5)
* org.apache.flink.api.java.typeutils.runtime.EitherSerializerTest.testStringValueDoubleValueEither() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.EitherSerializerTest.testEitherWithTupleValues() (Distance: 8)
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testSerializeIndividuallyReusingValues()
* org.apache.flink.api.common.typeutils.base.DoubleValueComparatorTest.testEquality()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testSerializedCopyAsSequence()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testSerializeIndividually()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testSerializeAsSequenceNoReuse()
* org.apache.flink.types.parser.DoubleValueParserTest.testValidStringInIsolationWithEndDelimiter()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testCopy()
* org.apache.flink.api.common.typeutils.base.DoubleValueComparatorTest.testDuplicate()
* org.apache.flink.api.common.typeutils.base.DoubleValueComparatorTest.testEqualityWithReference()
* org.apache.flink.types.parser.DoubleValueParserTest.testConcatenatedMultiCharDelimiter()
* org.apache.flink.api.common.typeutils.base.DoubleValueComparatorTest.testInequality()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testCopyIntoNewElements()
* org.apache.flink.types.RecordITCase.massiveRandomBlackBoxTests()
* org.apache.flink.types.parser.DoubleValueParserTest.testValidStringInIsolation()
* org.apache.flink.types.parser.DoubleValueParserTest.testInValidStringsMixedIn()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testCopyIntoReusedElements()
* org.apache.flink.types.parser.DoubleValueParserTest.testConcatenated()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testSerializeAsSequenceReusingValues()
* org.apache.flink.api.common.typeutils.base.DoubleValueSerializerTest.testSerializedCopyIndividually()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

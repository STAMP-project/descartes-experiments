# Summary
**org.apache.flink.api.common.io.FileInputFormat.close()**

This method is **strong pseudo-tested**.
It is covered by 41 test(s). 


## Transformations applied

- void


The test suite was not able to detect any transformation applied.

More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 41 test(s).
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadWithCharset()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithEmptyField()
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadCustomDelimiter()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryFalse()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithHeaderLine()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesWithFilteredFilesTrue()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testGetStatisticsOneFileInNestedDir()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadTooShortInputLenient()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosAllDeflate()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithParseQuotedStrings()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadWithBufferSizeIsMultiple()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testConfigure()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadExactlyBufferSize()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesTrue()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testSerialization()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testSparseParseWithIndices()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadWithoutTrailingDelimiter()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryTrue()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testOpen()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadCustomDelimiterWithCharset()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadInvalidContentsLenient()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadInvalidContents()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadRecordsLargerThanBuffer()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testDelimiterOnBufferBoundary()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadWithTrailingDelimiter()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadTooShortInput()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testGetStatisticsMultipleNestedFiles()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosAll()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testSparseFieldArray()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testMultiCharDelimiter()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testLongLongLong()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadOverSplitBoundariesUnaligned()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testSparseParse()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOnlyLevel2NestedDirectories()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testSparseParseWithIndicesMultiCharDelimiter()
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testNoNestedDirectoryTrue()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosFirstN()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithHeaderLineAndInvalidIntermediate()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosAllGzip()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadInvalidContentsLenientWithSkipping()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

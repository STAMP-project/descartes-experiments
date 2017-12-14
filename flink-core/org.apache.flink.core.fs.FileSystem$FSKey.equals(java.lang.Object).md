# Summary
**org.apache.flink.core.fs.FileSystem$FSKey.equals(java.lang.Object)**

This method is **strong pseudo-tested**.
It is covered by 58 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect any transformation applied.

More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 58 test(s).
* org.apache.flink.core.fs.FileSystemTest.testGet() (Distance: 5)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testGetStatisticsMultipleNestedFiles() (Distance: 6)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testGetStatisticsOneFileInNestedDir() (Distance: 6)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testNoNestedDirectoryTrue() (Distance: 7)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesTrue() (Distance: 7)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOnlyLevel2NestedDirectories() (Distance: 7)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryFalse() (Distance: 7)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryTrue() (Distance: 7)
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesWithFilteredFilesTrue() (Distance: 7)
* org.apache.flink.api.common.io.BinaryInputFormatTest.testCreateInputSplitsWithOneFile() (Distance: 7)
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadWithCharset()
* org.apache.flink.api.common.io.FileInputFormatTest.testExcludeFiles()
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsMultipleFilesWithCachedVersion()
* org.apache.flink.api.common.io.FileOutputFormatTest.testOverwriteNonParallelLocalFS()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithEmptyField()
* org.apache.flink.api.common.io.FileOutputFormatTest.testOverwriteParallelLocalFS()
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadCustomDelimiter()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithHeaderLine()
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsOneFileNoCachedVersion()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadTooShortInputLenient()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosAllDeflate()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithParseQuotedStrings()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadWithBufferSizeIsMultiple()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadExactlyBufferSize()
* org.apache.flink.configuration.FilesystemSchemeConfigTest.testDefaultsToLocal()
* org.apache.flink.core.fs.PathTest.testMakeQualified()
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsMultipleFilesNoCachedVersion()
* org.apache.flink.api.common.io.FileInputFormatTest.testDecorateInputStream()
* org.apache.flink.api.common.io.FileInputFormatTest.testReadMultiplePatterns()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testSparseParseWithIndices()
* org.apache.flink.api.common.io.FileOutputFormatTest.testCreateParallelLocalFS()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadWithoutTrailingDelimiter()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testOpen()
* org.apache.flink.api.common.io.FileInputFormatTest.testFileInputSplit()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadCustomDelimiterWithCharset()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadInvalidContentsLenient()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadInvalidContents()
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsNonExistingFile()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadRecordsLargerThanBuffer()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testDelimiterOnBufferBoundary()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadWithTrailingDelimiter()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadTooShortInput()
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsOneFileWithCachedVersion()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosAll()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testMultiCharDelimiter()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testLongLongLong()
* org.apache.flink.api.common.io.DelimitedInputFormatTest.testReadOverSplitBoundariesUnaligned()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testSparseParse()
* org.apache.flink.api.common.io.FileOutputFormatTest.testCreateNonParallelLocalFS()
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatsIgnoredUnderscoreFiles()
* org.apache.flink.core.fs.LimitedConnectionsConfigurationTest.testConfiguration()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testSparseParseWithIndicesMultiCharDelimiter()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosFirstN()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.readWithHeaderLineAndInvalidIntermediate()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadNoPosAllGzip()
* org.apache.flink.api.common.io.GenericCsvInputFormatTest.testReadInvalidContentsLenientWithSkipping()
* org.apache.flink.api.common.io.FileInputFormatTest.testIgnoredUnderscoreFiles()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

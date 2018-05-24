# equals(java.lang.Object)

**Class:** org.apache.flink.core.fs.FileSystem$FSKey

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/core/fs/FileSystem.java#L1045)

This method is **pseudo-tested**.


It can not be accessed from other classes. 
It has been covered by 34 test method(s) with a minimum stack distance of 5.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return false;
```

```Java
return true;
```





## Observed test methods

* org.apache.flink.core.fs.PathTest.testMakeQualified() at distance(s): 5
* org.apache.flink.core.fs.FileSystemTest.testGet() at distance(s): 5
* org.apache.flink.core.fs.LimitedConnectionsConfigurationTest.testConfiguration() at distance(s): 5
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.testSamplingOverlyLongRecord() at distance(s): 6
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testGetStatisticsOneFileInNestedDir() at distance(s): 6, 9, 10
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsMultipleFilesNoCachedVersion() at distance(s): 6, 9
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatsIgnoredUnderscoreFiles() at distance(s): 6, 9
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsNonExistingFile() at distance(s): 6
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.testSamplingDirectory() at distance(s): 6, 9
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.testNumSamplesMultipleFiles() at distance(s): 6, 9
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.testNumSamplesOneFile() at distance(s): 6
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsOneFileNoCachedVersion() at distance(s): 6
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.testDifferentDelimiter() at distance(s): 6
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.testSamplingOneFile() at distance(s): 6
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testGetStatisticsMultipleNestedFiles() at distance(s): 6, 9, 10
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsOneFileWithCachedVersion() at distance(s): 6
* org.apache.flink.api.common.io.DelimitedInputFormatSamplingTest.testCachedStatistics() at distance(s): 6
* org.apache.flink.api.common.io.FileInputFormatTest.testGetStatisticsMultipleFilesWithCachedVersion() at distance(s): 6, 9
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesWithFilteredFilesTrue() at distance(s): 7, 8, 9, 10
* org.apache.flink.api.common.io.FileInputFormatTest.testDecorateInputStream() at distance(s): 7
* org.apache.flink.api.common.io.FileOutputFormatTest.testCreateNonParallelLocalFS() at distance(s): 7
* org.apache.flink.api.common.io.FileOutputFormatTest.testOverwriteNonParallelLocalFS() at distance(s): 7
* org.apache.flink.api.common.io.FileOutputFormatTest.testCreateParallelLocalFS() at distance(s): 7
* org.apache.flink.api.common.io.FileInputFormatTest.testIgnoredUnderscoreFiles() at distance(s): 7, 8
* org.apache.flink.api.common.io.FileInputFormatTest.testReadMultiplePatterns() at distance(s): 7, 8
* org.apache.flink.api.common.io.FileOutputFormatTest.testOverwriteParallelLocalFS() at distance(s): 7
* org.apache.flink.api.common.io.FileInputFormatTest.testExcludeFiles() at distance(s): 7, 8
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryTrue() at distance(s): 7, 8, 9
* org.apache.flink.api.common.io.BinaryInputFormatTest.testCreateInputSplitsWithOneFile() at distance(s): 7, 8
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryFalse() at distance(s): 7, 8
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testNoNestedDirectoryTrue() at distance(s): 7
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesTrue() at distance(s): 7, 8, 9, 10
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOnlyLevel2NestedDirectories() at distance(s): 7, 8, 9, 10
* org.apache.flink.api.common.io.FileInputFormatTest.testFileInputSplit() at distance(s): 7, 8


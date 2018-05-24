# getBlockIndexForPosition(org.apache.flink.core.fs.BlockLocation[],long,long,int)

**Class:** org.apache.flink.api.common.io.FileInputFormat

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/api/common/io/FileInputFormat.java#L657)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `0`


It can not be accessed from other classes. 
It has been covered by 9 test method(s) with a minimum stack distance of 2.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return 0;
```

The following transformations were also applied and they were detected by the test suite:

```Java
return 1;
```





## Observed test methods

* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesWithFilteredFilesTrue() at distance(s): 2
* org.apache.flink.api.common.io.FileInputFormatTest.testDecorateInputStream() at distance(s): 2
* org.apache.flink.api.common.io.FileInputFormatTest.testIgnoredUnderscoreFiles() at distance(s): 2
* org.apache.flink.api.common.io.FileInputFormatTest.testExcludeFiles() at distance(s): 2
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryTrue() at distance(s): 2
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOneNestedDirectoryFalse() at distance(s): 2
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testNoNestedDirectoryTrue() at distance(s): 2
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testTwoNestedDirectoriesTrue() at distance(s): 2
* org.apache.flink.api.common.io.EnumerateNestedFilesTest.testOnlyLevel2NestedDirectories() at distance(s): 2


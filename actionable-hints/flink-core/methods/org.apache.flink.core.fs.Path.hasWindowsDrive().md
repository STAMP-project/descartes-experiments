# hasWindowsDrive()

**Class:** org.apache.flink.core.fs.Path

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/core/fs/Path.java#L506)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 12 test method(s) with a minimum stack distance of 2.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return false;
```

The following transformations were also applied and they were detected by the test suite:

```Java
return true;
```





## Observed test methods

* org.apache.flink.api.common.io.GlobFilePathFilterTest.testDoubleStarPattern() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testIncludeFileWithCharacterSetMatcher() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testExcludeFilesIfMatchesExclude() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testIncludeFileWithAnyCharacterMatcher() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testExcludeFilesNotInIncludePatterns() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testIncludeFileWithCharacterRangeMatcher() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testSingleStarPattern() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testGlobFilterSerializable() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testExcludeFilenameWithStart() at distance(s): 2
* org.apache.flink.api.common.io.GlobFilePathFilterTest.testExcludeHDFSFile() at distance(s): 2
* org.apache.flink.api.common.io.FileInputFormatTest.testReadMultiplePatterns() at distance(s): 5
* org.apache.flink.api.common.io.FileInputFormatTest.testExcludeFiles() at distance(s): 5


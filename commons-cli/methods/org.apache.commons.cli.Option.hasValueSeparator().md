# hasValueSeparator()

**Class:** org.apache.commons.cli.Option

[[View code]](https://github.com/apache/commons-cli/blob/2392ae8afc08b496a3eb49908aa421ea86a9679e/src/main/java//org/apache/commons/cli/Option.java#L411)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 79 test method(s) with a minimum stack distance of 3.

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

* org.apache.commons.cli.OptionTest.testGetValue() at distance(s): 3
* org.apache.commons.cli.OptionTest.testClone() at distance(s): 4
* org.apache.commons.cli.OptionTest.testClear() at distance(s): 4
* org.apache.commons.cli.bug.BugsTest.test31148() at distance(s): 6
* org.apache.commons.cli.ParserTestCase.testStopAtExpectedArg() at distance(s): 6, 7
* org.apache.commons.cli.bug.BugCLI148Test.testWorkaround1() at distance(s): 7
* org.apache.commons.cli.PatternOptionBuilderTest.testExistingFilePatternFileNotExist() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertiesOption2() at distance(s): 7, 8
* org.apache.commons.cli.bug.BugsTest.test15648() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testSimpleLong() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testNullhOption() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testLongWithEqualDoubleDash() at distance(s): 7, 9
* org.apache.commons.cli.ParserTestCase.testArgumentStartingWithHyphen() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertiesOption1() at distance(s): 7, 8
* org.apache.commons.cli.CommandLineTest.testGetOptionPropertiesWithOption() at distance(s): 7
* org.apache.commons.cli.ApplicationTest.testLs() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertyOverrideValues() at distance(s): 7, 8
* org.apache.commons.cli.ValueTest.testShortOptionalNArgValuesWithOption() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testNegativeArgument() at distance(s): 7
* org.apache.commons.cli.ValueTest.testLongOptionalNArgValues() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI148Test.testWorkaround2() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI13Test.testCLI13() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testSimpleShort() at distance(s): 7
* org.apache.commons.cli.bug.BugsTest.test11458() at distance(s): 7
* org.apache.commons.cli.bug.BugsTest.test15046() at distance(s): 7
* org.apache.commons.cli.ValueTest.testLongOptionalArgValues() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testSingleDash() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testMultipleWithLong() at distance(s): 7
* org.apache.commons.cli.ValueTest.testLongOptionalArgValuesWithOption() at distance(s): 7
* org.apache.commons.cli.PatternOptionBuilderTest.testNumberPattern() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testGetParsedOptionValueWithChar() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testOptionAndRequiredOption() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testGetParsedOptionValueWithOption() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI265Test.shouldParseShortOptionWithValue() at distance(s): 7
* org.apache.commons.cli.bug.BugsTest.test11680() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testNegativeOption() at distance(s): 7
* org.apache.commons.cli.PatternOptionBuilderTest.testSimplePattern() at distance(s): 7
* org.apache.commons.cli.PatternOptionBuilderTest.testExistingFilePattern() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI71Test.testGetsDefaultIfOptional() at distance(s): 7
* org.apache.commons.cli.PatternOptionBuilderTest.testURLPattern() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI71Test.testBasic() at distance(s): 7
* org.apache.commons.cli.ValueTest.setUp() at distance(s): 7
* org.apache.commons.cli.ValueTest.testShortOptionalArgValues() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testUnlimitedArgs() at distance(s): 7
* org.apache.commons.cli.ValueTest.testShortOptionalArgValue() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testUnambiguousPartialLongOption3() at distance(s): 7, 9
* org.apache.commons.cli.ArgumentIsOptionTest.testOptionAndOptionWithArgument() at distance(s): 7
* org.apache.commons.cli.ValueTest.testShortOptionalArgValueWithOption() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testGetOptionProperties() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testStopBursting2() at distance(s): 7, 9
* org.apache.commons.cli.ApplicationTest.testAnt() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertyOptionFlags() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testLongWithEqualSingleDash() at distance(s): 7, 9
* org.apache.commons.cli.ValuesTest.setUp() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testMultiple() at distance(s): 7
* org.apache.commons.cli.ValueTest.testShortOptionalNArgValues() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testBursting() at distance(s): 7, 9
* org.apache.commons.cli.ArgumentIsOptionTest.testOptionWithArgument() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testWithRequiredOption() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertyOptionMultipleValues() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertyOptionSingularValue() at distance(s): 7
* org.apache.commons.cli.PatternOptionBuilderTest.testClassPattern() at distance(s): 7
* org.apache.commons.cli.bug.BugsTest.test11456() at distance(s): 7
* org.apache.commons.cli.ValueTest.testLongOptionalArgValueWithOption() at distance(s): 7
* org.apache.commons.cli.ValueTest.testLongOptionalNArgValuesWithOption() at distance(s): 7
* org.apache.commons.cli.ApplicationTest.testNLT() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testShortWithEqual() at distance(s): 7, 8
* org.apache.commons.cli.ApplicationTest.testGroovy() at distance(s): 7
* org.apache.commons.cli.ValueTest.testLongOptionalArgValue() at distance(s): 7
* org.apache.commons.cli.PatternOptionBuilderTest.testObjectPattern() at distance(s): 7
* org.apache.commons.cli.ValueTest.testShortOptionalArgValuesWithOption() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testShortWithoutEqual() at distance(s): 7, 9
* org.apache.commons.cli.bug.BugCLI71Test.testMistakenArgument() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testLongWithoutEqualSingleDash() at distance(s): 8
* org.apache.commons.cli.ParserTestCase.testAmbiguousLongWithoutEqualSingleDash() at distance(s): 8
* org.apache.commons.cli.ParserTestCase.testUnambiguousPartialLongOption4() at distance(s): 9
* org.apache.commons.cli.DisablePartialMatchingTest.testDisablePartialMatching() at distance(s): 9
* org.apache.commons.cli.DisablePartialMatchingTest.testRegularPartialMatching() at distance(s): 9


# isLongOption(java.lang.String)

**Class:** org.apache.commons.cli.DefaultParser

[[View code]](https://github.com/apache/commons-cli/blob/2392ae8afc08b496a3eb49908aa421ea86a9679e/src/main/java//org/apache/commons/cli/DefaultParser.java#L371)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can not be accessed from other classes. 
It has been covered by 22 test method(s) with a minimum stack distance of 6.

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

* org.apache.commons.cli.ParserTestCase.testStopAtExpectedArg() at distance(s): 6
* org.apache.commons.cli.ParserTestCase.testSimpleLong() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testNullhOption() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testArgumentStartingWithHyphen() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertiesOption1() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testPropertyOverrideValues() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testNegativeArgument() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testSimpleShort() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testSingleDash() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testMultipleWithLong() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testGetParsedOptionValueWithChar() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testAmbiguousLongWithoutEqualSingleDash() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testOptionAndRequiredOption() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testGetParsedOptionValueWithOption() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI265Test.shouldParseShortOptionWithValue() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testNegativeOption() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testUnlimitedArgs() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI265Test.shouldParseShortOptionWithoutValue() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testMultiple() at distance(s): 7
* org.apache.commons.cli.ParserTestCase.testWithRequiredOption() at distance(s): 7
* org.apache.commons.cli.bug.BugCLI265Test.shouldParseConcatenatedShortOptions() at distance(s): 7
* org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue() at distance(s): 7


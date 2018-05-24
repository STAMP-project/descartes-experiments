# meetsConverterRequirements(java.lang.reflect.Method,java.lang.Class)

**Class:** joptsimple.internal.Reflection

[[View code]](https://github.com/jopt-simple/jopt-simple/blob/b38b70d1e7685766ab400d8b57ef9ca9c010e0bb/src/main/java//joptsimple/internal/Reflection.java#L128)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can not be accessed from other classes. 
It has been covered by 62 test method(s) with a minimum stack distance of 4.

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

* joptsimple.ConfigurableOptionParserHelpTest.oneOptionRequiredArgWithDescriptionAndType() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.oneOptionRequiredArgNoDescriptionWithType() at distance(s): 4
* joptsimple.ConfigurableOptionParserHelpTest.bothColumnsExceedingAllocatedWidths() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.bothColumnsExceedingAllocatedWidths() at distance(s): 4
* joptsimple.examples.SpecialOptionalArgumentHandlingTest.handlesNegativeNumberOptionalArguments() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.oneOptionOptionalArgWithDescriptionAndType() at distance(s): 4
* joptsimple.OptionParserTest.typedArguments() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.byteArgumentType() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.canSubvertTypeSafetyIfYouGiveAnOptionSpecToOptionSetAsTheWrongType() at distance(s): 4
* joptsimple.HandlingDefaultValuesForOptionArgumentsTest.optionalArgOptionWithDefaultGivesArgIfSpecifiedOnCommandLine() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.includesListOfDefaultsForArgumentWithDescription() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.floatArgumentType() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.optionsWithNegativeNumberArgumentsAndNonNumberOptions() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.sqlTimeArgumentType() at distance(s): 4
* joptsimple.examples.ExportOptionsTest.allowsExportOfOptions() at distance(s): 4
* joptsimple.examples.DefaultValuesForOptionArgumentsTest.allowsSpecificationOfDefaultValues() at distance(s): 4
* joptsimple.HandlingDefaultValuesForOptionArgumentsTest.requiredArgOptionWithDefaultGivesArgIfArgSpecifiedOnCommandLine() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.fixForIssue85() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.primitiveIntAllowedAsTypeSpecifier() at distance(s): 4
* joptsimple.HandlingDefaultValuesForOptionArgumentsTest.withCompileTimeArraySpecifyingDefaults() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.booleanArgumentType() at distance(s): 4
* joptsimple.ConfigurableOptionParserHelpTest.oneOptionOptionalArgNoDescriptionWithType() at distance(s): 4
* joptsimple.ConfigurableOptionParserHelpTest.oneOptionOptionalArgWithDescriptionAndType() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.primitiveDoubleAllowedAsTypeSpecifier() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.primitiveLongAllowedAsTypeSpecifier() at distance(s): 4
* joptsimple.HandlingDefaultValuesForOptionArgumentsTest.optionalArgOptionWithDefaultGivesDefaultIfArgNotSpecifiedOnCommandLine() at distance(s): 4
* joptsimple.WExtensionWithArgumentTest.typedTogetherArg() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.canSubvertTypeSafetyIfYouUseAnOptionSpecAsTheWrongType() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.oneOptionRequiredArgWithDescriptionAndType() at distance(s): 4
* joptsimple.ConfigurableOptionParserHelpTest.optionSynonymsWithRequiredArgument() at distance(s): 4
* joptsimple.WExtensionWithArgumentTest.typedSeparateArg() at distance(s): 4
* joptsimple.OptionSynonymRequiredArgumentTest.initializeParser() at distance(s): 4
* joptsimple.JVMSystemPropertiesArgumentParsingTest.initializeParser() at distance(s): 4
* joptsimple.HandlingDefaultValuesForOptionArgumentsTest.allowsListOfDefaults() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.primitiveBooleanAllowedAsTypeSpecifier() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.retrievalOfTypedOptionalArgumentsInATypesafeManner() at distance(s): 4
* joptsimple.HandlingDefaultValuesForOptionArgumentsTest.specifiedOptionArgumentsTrumpsListOfDefaults() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.shortArgumentType() at distance(s): 4
* joptsimple.examples.OptionArgumentValueTypeTest.convertsArgumentsToJavaValueTypes() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.sqlTimestampArgumentType() at distance(s): 4
* joptsimple.examples.TypesafeOptionArgumentRetrievalTest.allowsTypesafeRetrievalOfOptionArguments() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.optionSynonymsWithRequiredArgument() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.includesDefaultValueForOptionalOptionArgument() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.canUseBooleanType() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.illegalOptionArgumentMethodConversion() at distance(s): 4
* joptsimple.ConfigurableOptionParserHelpTest.oneOptionRequiredArgNoDescriptionWithType() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.sqlDateArgumentType() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.optionsWithOptionalNegativeNumberArgumentsAndNumberOptions() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.retrievalOfTypedRequiredArgumentsInATypesafeManner() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.integerArgumentType() at distance(s): 4
* joptsimple.DefaultSettingsOptionParserHelpTest.oneOptionOptionalArgNoDescriptionWithType() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.longArgumentType() at distance(s): 4
* joptsimple.ConfigurableOptionParserHelpTest.includesListOfDefaultsForArgumentWithDescription() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.primitiveByteAllowedAsTypeSpecifier() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.optionsWithOptionalNegativeNumberArguments() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.primitiveFloatAllowedAsTypeSpecifier() at distance(s): 4
* joptsimple.TypesafeOptionArgumentRetrievalTest.primitiveShortAllowedAsTypeSpecifier() at distance(s): 4
* joptsimple.ConfigurableOptionParserHelpTest.includesDefaultValueForOptionalOptionArgument() at distance(s): 4
* joptsimple.Issue76Test.setUp() at distance(s): 4
* joptsimple.OptionParserNewDeclarationTest.doubleArgumentType() at distance(s): 4
* joptsimple.ArgumentAcceptingOptionSpecTest.optionalArgOfValueTypeBasedOnValueOf() at distance(s): 6
* joptsimple.ArgumentAcceptingOptionSpecTest.requiredArgOfValueTypeBasedOnValueOf() at distance(s): 6


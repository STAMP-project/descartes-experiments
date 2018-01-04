# Summary
**org.xwiki.velocity.internal.DefaultVelocityEngine.restoreTemplateScope(org.apache.velocity.context.InternalContextAdapterImpl,org.apache.velocity.runtime.directive.Scope)**

This method is **strong pseudo-tested**.
It is covered by 38 test(s). It can not be directly accessed from tests methods.


## Transformations applied

- void


The test suite was not able to detect any transformation applied.

More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 38 test(s).
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testEvaluateReader() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testEmptyChain() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testInvalidUberspectorsAreIgnored() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testDeprecatedUberspector() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testSecureUberspectorEnabledByDefault() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testDefaultUberspectorWorks() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testSecureUberspectorWorks() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testChainBreakingOnNonChainableEntry() (Distance: 3)
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testBasicChaining() (Distance: 3)
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testBasicArray() (Distance: 3)
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testEmptyArray() (Distance: 3)
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testInvalidUberspectorsAreIgnored() (Distance: 3)
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testSecureUberspectorEnabledByDefault() (Distance: 3)
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testDefaultUberspectorWorks() (Distance: 3)
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testSecureUberspectorWorks() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenNoConversion() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenVarargsWithConversionAndVarargParamPassedNeedingConversion() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenVarargsWithConversionAndNoVarargParamPassed() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenVarargsWithNoConversionAndNoVarargParamPassed() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenExistingMethodNameButInvalidSignature() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenVarargsWithConversionAndOneVarargParamPassed() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenAddingSameMethodNameToExtendingClassAndConversion() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenVarargsWithConversionAndTwoVarargParamsPassed() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenVarargsWithNoConversionAndTwoVarargParamsPassed() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenNoMatchingMethod() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWithGeneric() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenInnerMethodAndNoConversion() (Distance: 3)
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenVarargsWithNoConversionAndOneVarargParamPassed() (Distance: 3)
* org.xwiki.velocity.internal.jmx.JMXVelocityEngineTest.testGetTemplates() (Distance: 4)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testConfigureMacrosToBeGlobal() (Distance: 4)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testMacroIsolation() (Distance: 4)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testOverrideConfiguration() (Distance: 4)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testThreadsafeNamespaces() (Distance: 4)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testMacroNamespaceCleanup() (Distance: 4)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testSettingNullAllowedByDefault() (Distance: 4)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testSecureUberspectorActiveByDefault() (Distance: 6)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testEvaluateString() (Distance: 6)
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testEvaluateWithStopCommand() (Distance: 6)


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

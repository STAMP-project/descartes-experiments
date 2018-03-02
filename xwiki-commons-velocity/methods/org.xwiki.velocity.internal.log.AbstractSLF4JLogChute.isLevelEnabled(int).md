# isLevelEnabled(int)

**Class:** org.xwiki.velocity.internal.log.AbstractSLF4JLogChute

[[View code]](https://github.com/xwiki/xwiki-commons/blob/6090f4369cf659a57237449a21105515b1c27995/xwiki-commons-core/xwiki-commons-velocity/src/main/java//org/xwiki/velocity/internal/log/AbstractSLF4JLogChute.java#L89)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 27 test method(s) with a minimum stack distance of 6.

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

* org.xwiki.velocity.introspection.LinkingUberspectorTest.testSecureUberspectorWorks() at distance(s): 6, 7, 8
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testSecureUberspectorEnabledByDefault() at distance(s): 6, 7, 8
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testEmptyChain() at distance(s): 6, 7, 8
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.getMethodWhenNoMatchingMethod() at distance(s): 6
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testSecureUberspectorWorks() at distance(s): 6, 7, 8
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testEmptyArray() at distance(s): 6, 7, 8
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testSecureUberspectorEnabledByDefault() at distance(s): 6, 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testSettingNullAllowedByDefault() at distance(s): 7, 8, 9
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testEvaluateReader() at distance(s): 7, 8
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testDefaultUberspectorWorks() at distance(s): 7, 8
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testBasicChaining() at distance(s): 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testEvaluateWithStopCommand() at distance(s): 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testEvaluateString() at distance(s): 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testConfigureMacrosToBeGlobal() at distance(s): 7, 8, 10
* org.xwiki.velocity.internal.jmx.JMXVelocityEngineTest.testGetTemplates() at distance(s): 7, 8, 10
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testDeprecatedUberspector() at distance(s): 7, 8
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testBasicArray() at distance(s): 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testThreadsafeNamespaces() at distance(s): 7, 8, 10
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testChainBreakingOnNonChainableEntry() at distance(s): 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testMacroIsolation() at distance(s): 7, 8, 10
* org.xwiki.velocity.introspection.ChainingUberspectorTest.testInvalidUberspectorsAreIgnored() at distance(s): 7, 8
* org.xwiki.velocity.introspection.MethodArgumentUberspectorTest.setUp() at distance(s): 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testSecureUberspectorActiveByDefault() at distance(s): 7, 8, 9
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testDefaultUberspectorWorks() at distance(s): 7, 8
* org.xwiki.velocity.introspection.LinkingUberspectorTest.testInvalidUberspectorsAreIgnored() at distance(s): 7, 8
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testMacroNamespaceCleanup() at distance(s): 7, 8, 10
* org.xwiki.velocity.internal.DefaultVelocityEngineTest.testOverrideConfiguration() at distance(s): 7, 8


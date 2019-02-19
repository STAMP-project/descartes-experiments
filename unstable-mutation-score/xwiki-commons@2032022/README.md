# Module

`xwiki-commons-tools-xar-plugin`@[2032022c6f8f705be1811f1014726f5f597f4abb](https://github.com/xwiki/xwiki-commons/commit/2032022c6f8f705be1811f1014726f5f597f4abb)

Executed the mutation analysis 30 times. No mutant is covered in any execution.
There is a misconfiguration for this module.

PIT is configured for the entire `xwiki-commons` project to use the Junit 5 plugin.

In this particular module `xwiki-commons-tools-xar-plugin`, when the tests are executed, Junit5 is not included on the classpath.

Since Junit5 is not in the classpath, the PIT Junit5 plugin fails to execute and therefore no test class is found.

This is the Junit configuration in the `pom.xml` for `xwiki-commons-tools-xar-plugin` 

```xml
<!-- Test dependencies -->
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
</dependency>
```

This is the message given by PIT:

```
WARNING: TestEngine with ID 'junit-jupiter' failed to discover tests
java.lang.NoClassDefFoundError: org/junit/jupiter/api/extension/ExtensionContext
        at org.junit.jupiter.engine.JupiterTestEngine.discover(JupiterTestEngine.java:60)
        at org.junit.platform.launcher.core.DefaultLauncher.discoverEngineRoot(DefaultLauncher.java:130)
        at org.junit.platform.launcher.core.DefaultLauncher.discoverRoot(DefaultLauncher.java:117)
        at org.junit.platform.launcher.core.DefaultLauncher.discover(DefaultLauncher.java:82)
        at org.pitest.junit5.JUnit5TestUnitFinder.findTestUnits(JUnit5TestUnitFinder.java:43)
        at org.pitest.testapi.execute.FindTestUnits.findTestUnits(FindTestUnits.java:57)
        at org.pitest.testapi.execute.FindTestUnits.getTestUnits(FindTestUnits.java:40)
        at org.pitest.testapi.execute.FindTestUnits.findTestUnitsForAllSuppliedClasses(FindTestUnits.java:29)
        at org.pitest.coverage.execute.CoverageMinion.discoverTests(CoverageMinion.java:157)
        at org.pitest.coverage.execute.CoverageMinion.getTestsFromParent(CoverageMinion.java:138)
        at org.pitest.coverage.execute.CoverageMinion.main(CoverageMinion.java:84)
Caused by: java.lang.ClassNotFoundException: org.junit.jupiter.api.extension.ExtensionContext
        at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
        at sun.misc.Launcher$AppClassLoader.loadClass (Launcher.java:338)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
        ... 11 more

```

This is the classpath for the mutation analysis,a s given by PIT. Note that Junit 4.12 and the Junit 5 PIT plugin are included but Junit 5 itself is not included.

```
Projects/playground/xwiki-commons/xwiki-commons-tools/xwiki-commons-tool-xar/xwiki-commons-tool-xar-plugin/target/test-classes, 
Projects/playground/xwiki-commons/xwiki-commons-tools/xwiki-commons-tool-xar/xwiki-commons-tool-xar-plugin/target/classes, 
.m2/repository/org/dom4j/dom4j/2.1.0/dom4j-2.1.0.jar, 
.m2/repository/org/codehaus/plexus/plexus-archiver/3.6.0/plexus-archiver-3.6.0.jar, 
.m2/repository/org/codehaus/plexus/plexus-io/3.0.1/plexus-io-3.0.1.jar, 
.m2/repository/org/apache/commons/commons-compress/1.16.1/commons-compress-1.16.1.jar,
.m2/repository/org/objenesis/objenesis/2.6/objenesis-2.6.jar, 
.m2/repository/org/iq80/snappy/snappy/0.4/snappy-0.4.jar, 
.m2/repository/org/tukaani/xz/1.8/xz-1.8.jar,
.m2/repository/jaxen/jaxen/1.1.6/jaxen-1.1.6.jar, 
.m2/repository/com/ibm/icu/icu4j/50.1.1/icu4j-50.1.1.jar, 
.m2/repository/commons-io/commons-io/2.6/commons-io-2.6.jar, 
.m2/repository/org/apache/commons/commons-lang3/3.7/commons-lang3-3.7.jar, 
.m2/repository/org/codehaus/plexus/plexus-utils/3.1.0/plexus-utils-3.1.0.jar, 
.m2/repository/org/apache/maven/maven-artifact/3.3.9/maven-artifact-3.3.9.jar, 
.m2/repository/org/apache/maven/maven-plugin-api/3.3.9/maven-plugin-api-3.3.9.jar, 
.m2/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/0.3.3/org.eclipse.sisu.plexus-0.3.3.jar, 
.m2/repository/javax/enterprise/cdi-api/1.0/cdi-api-1.0.jar, .m2/repository/javax/inject/javax.inject/1/javax.inject-1.jar, 
.m2/repository/org/eclipse/sisu/org.eclipse.sisu.inject/0.3.3/org.eclipse.sisu.inject-0.3.3.jar,
.m2/repository/org/apache/maven/maven-compat/3.3.9/maven-compat-3.3.9.jar, 
.m2/repository/org/apache/maven/maven-model-builder/3.3.9/maven-model-builder-3.3.9.jar, 
.m2/repository/org/apache/maven/maven-builder-support/3.3.9/maven-builder-support-3.3.9.jar, 
.m2/repository/com/google/guava/guava/20.0/guava-20.0.jar, 
.m2/repository/org/apache/maven/maven-settings/3.3.9/maven-settings-3.3.9.jar, 
.m2/repository/org/apache/maven/maven-core/3.3.9/maven-core-3.3.9.jar,
.m2/repository/org/apache/maven/maven-settings-builder/3.3.9/maven-settings-builder-3.3.9.jar, 
.m2/repository/org/apache/maven/maven-repository-metadata/3.3.9/maven-repository-metadata-3.3.9.jar, 
.m2/repository/org/apache/maven/maven-aether-provider/3.3.9/maven-aether-provider-3.3.9.jar, 
.m2/repository/org/eclipse/aether/aether-spi/1.0.2.v20150114/aether-spi-1.0.2.v20150114.jar, 
.m2/repository/org/eclipse/aether/aether-impl/1.0.2.v20150114/aether-impl-1.0.2.v20150114.jar, 
.m2/repository/org/eclipse/aether/aether-api/1.0.2.v20150114/aether-api-1.0.2.v20150114.jar, 
.m2/repository/org/eclipse/aether/aether-util/1.0.2.v20150114/aether-util-1.0.2.v20150114.jar, 
.m2/repository/com/google/inject/guice/4.0/guice-4.0-no_aop.jar, 
.m2/repository/aopalliance/aopalliance/1.0/aopalliance-1.0.jar, 
.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.jar, 
.m2/repository/org/sonatype/plexus/plexus-cipher/1.4/plexus-cipher-1.4.jar, 
.m2/repository/org/codehaus/plexus/plexus-interpolation/1.24/plexus-interpolation-1.24.jar, 
.m2/repository/org/codehaus/plexus/plexus-component-annotations/1.7.1/plexus-component-annotations-1.7.1.jar, 
.m2/repository/org/apache/maven/wagon/wagon-provider-api/2.10/wagon-provider-api-2.10.jar, 
.m2/repository/org/apache/maven/maven-model/3.3.9/maven-model-3.3.9.jar, 
.m2/repository/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5/maven-plugin-annotations-3.5.jar, 
.m2/repository/org/codehaus/plexus/plexus-container-default/1.7.1/plexus-container-default-1.7.1.jar, 
.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.jar, 
.m2/repository/org/apache/xbean/xbean-reflect/3.7/xbean-reflect-3.7.jar, 
.m2/repository/com/google/collections/google-collections/1.0/google-collections-1.0.jar, 
.m2/repository/org/twdata/maven/mojo-executor/2.2.0/mojo-executor-2.2.0.jar, 
.m2/repository/xerces/xercesImpl/2.11.0/xercesImpl-2.11.0.jar, 
.m2/repository/xml-apis/xml-apis/1.4.01/xml-apis-1.4.01.jar,
.m2/repository/junit/junit/4.12/junit-4.12.jar, 
.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar, 
.m2/repository/org/pitest/pitest-junit5-plugin/0.5/pitest-junit5-plugin-0.5.jar, 
.m2/repository/eu/stamp-project/descartes/1.2/descartes-1.2.jar, 
.m2/repository/org/pitest/pitest/1.4.0/pitest-1.4.0.jar
```
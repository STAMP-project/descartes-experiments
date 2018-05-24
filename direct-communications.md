# Direct communications and pull requests

This file contains a list of methods found to be *pseudo-tested* or *partially-required* (formerly partially-tested) and were consulted directly to the developers of 5 open source projects. It also contains links to pull requests made to 2 external projects proposing fixes to testing issues behind pseudo-tested methods.

## Direct communications

### Apache Flink Core

* [org.apache.flink.api.common.io.BinaryInputFormat.configure(org.apache.flink.configuration.Configuration)](actionable-hints/flink-core/methods/org.apache.flink.api.common.io.BinaryInputFormat.configure(org.apache.flink.configuration.Configuration).md)

### SAT4J Core

* [org.sat4j.tools.xplain.Xplain.removeConstr(org.sat4j.specs.IConstr)](actionable-hints/sat4j-core/methods/org.sat4j.tools.xplain.Xplain.removeConstr(org.sat4j.specs.IConstr).md)
* [org.sat4j.minisat.core.Solver.learn(org.sat4j.specs.Constr)](actionable-hints/sat4j-core/methods/org.sat4j.minisat.core.Solver.learn(org.sat4j.specs.Constr).md)

### Spoon

* [spoon.reflect.visitor.DefaultJavaPrettyPrinter.visitCtAssert(spoon.reflect.code.CtAssert)](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/DefaultJavaPrettyPrinter.java#L479).
This method is covered only by the method test [spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass()](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/test/java/spoon/test/ctClass/CtClassTest.java#L66), but not directly and the test is verifying other functionalities.

* [spoon.support.reflect.declaration.CtTypeParameterImpl.isSameInSameScope(spoon.reflect.declaration.CtTypeParameter,spoon.reflect.reference.CtTypeReference)](actionable-hints/spoon/methods/spoon.support.reflect.declaration.CtTypeParameterImpl.isSameInSameScope(spoon.reflect.declaration.CtTypeParameter,spoon.reflect.reference.CtTypeReference).md)
* [spoon.support.reflect.declaration.CtTypeParameterImpl.isSubtypeOf(spoon.support.visitor.GenericTypeAdapter,spoon.reflect.declaration.CtTypeParameter,spoon.reflect.declaration.CtTypeParameter)](actionable-hints/spoon/methods/spoon.support.reflect.declaration.CtTypeParameterImpl.isSubtypeOf(spoon.support.visitor.GenericTypeAdapter,spoon.reflect.declaration.CtTypeParameter,spoon.reflect.declaration.CtTypeParameter).md)
* [spoon.template.TemplateMatcher.addMatch(java.lang.Object,java.lang.Object)](actionable-hints/spoon/methods/spoon.template.TemplateMatcher.addMatch(java.lang.Object,java.lang.Object).md)

A general issue was opened. [See here.](https://github.com/INRIA/spoon/issues/1818)

### XWiki Rendering
* org.xwiki.rendering.macro.MacroId.equals(Object) was signaled as partially-required. A commit was made to target the issue. [See here.](https://github.com/xwiki/xwiki-rendering/commit/2d6d8c34865f2e979248c32f85edafb56197beca)

### XWiki Commons Velocity
* [org.xwiki.velocity.internal.util.VelocityParserContext.isInVelocityBlock()](actionable-hints/xwiki-commons-velocity/methods/org.xwiki.velocity.internal.util.VelocityParserContext.isInVelocityBlock().md)

## Pull requests

* **[Amazon Web Services Java SDK](https://github.com/aws/aws-sdk-java/pull/1437)**
* **[Apache Commons Collections](https://github.com/apache/commons-collections/pull/36)**

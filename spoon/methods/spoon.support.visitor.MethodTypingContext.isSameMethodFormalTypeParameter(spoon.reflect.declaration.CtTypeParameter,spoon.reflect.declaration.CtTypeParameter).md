# isSameMethodFormalTypeParameter(spoon.reflect.declaration.CtTypeParameter,spoon.reflect.declaration.CtTypeParameter)

**Class:** spoon.support.visitor.MethodTypingContext

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/MethodTypingContext.java#L238)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can not be accessed from other classes. 
It has been covered by 20 test method(s) with a minimum stack distance of 5.

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

* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 5
* spoon.test.generics.GenericsTest.testIsSameSignatureWithReferencedGenerics() at distance(s): 6, 7, 9, 10, 11, 12, 13
* spoon.test.generics.GenericsTest.testClassTypingContextMethodSignature() at distance(s): 6, 7, 9, 10, 11
* spoon.test.generics.GenericsTest.testIsSameSignatureWithMethodGenerics() at distance(s): 6, 7, 11, 12, 13
* spoon.test.generics.GenericsTest.testIsGenericTypeEqual() at distance(s): 7
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeParameters() at distance(s): 7
* spoon.test.generics.GenericsTest.testMethodTypingContextAdaptMethod() at distance(s): 7
* spoon.test.metamodel.MMMethod.overrides(spoon.reflect.declaration.CtMethod) at distance(s): 7, 13
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 8
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 12
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 12
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 28, 33, 34
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 29, 30, 31
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 30, 31
* spoon.test.lambda.LambdaTest.testGetOverriddenMethodWithFunction() at distance(s): 33, 37
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 64, 70
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 111, 112, 115, 116, 117, 120, 121


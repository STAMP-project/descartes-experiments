# hasSameMethodFormalTypeParameters(spoon.reflect.declaration.CtFormalTypeDeclarer)

**Class:** spoon.support.visitor.MethodTypingContext

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/MethodTypingContext.java#L222)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 43 test method(s) with a minimum stack distance of 4.

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

* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 4
* spoon.test.generics.GenericsTest.testIsSameSignatureWithReferencedGenerics() at distance(s): 5, 6, 8, 9, 10, 11, 12
* spoon.test.generics.GenericsTest.testClassTypingContextMethodSignature() at distance(s): 5, 6, 8, 9, 10
* spoon.test.generics.GenericsTest.testIsSameSignatureWithMethodGenerics() at distance(s): 5, 6, 10, 11, 12
* spoon.test.generics.GenericsTest.testIsSameSignatureWithGenerics() at distance(s): 5, 6
* spoon.test.generics.GenericsTest.testIsGenericTypeEqual() at distance(s): 6
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeParameters() at distance(s): 6
* spoon.test.generics.GenericsTest.testMethodTypingContextAdaptMethod() at distance(s): 6
* spoon.test.metamodel.MMMethod.overrides(spoon.reflect.declaration.CtMethod) at distance(s): 6, 12
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 7
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 7
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 10
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 10
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 10
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 11, 12
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 11, 12
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 25, 27, 32, 33
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35
* spoon.test.interfaces.InterfaceTest.testRedefinesStaticMethodInSubInterface() at distance(s): 26
* spoon.test.interfaces.InterfaceTest.testExtendsStaticMethodInSubInterface() at distance(s): 26
* spoon.test.interfaces.InterfaceTest.testExtendsDefaultMethodInSubInterface() at distance(s): 26
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 26, 27, 28, 29, 30, 31
* spoon.test.interfaces.InterfaceTest.testRedefinesDefaultMethodInSubInterface() at distance(s): 26
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 26
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 27, 29
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 27
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 27, 28, 29, 30, 31
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 32, 34
* spoon.test.lambda.LambdaTest.testGetOverriddenMethodWithFunction() at distance(s): 32, 36
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 32, 34
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 33, 34, 35, 36, 37, 38
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 63, 69
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 58, 59, 60, 114, 115, 116
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 59
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 59
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 60, 87
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 60, 87
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 60, 87
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 60, 87
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 106, 108, 133, 135
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 110, 111, 114, 115, 116, 119, 120


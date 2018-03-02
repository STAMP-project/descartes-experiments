# checkSameTypingContext(spoon.support.visitor.ClassTypingContext,spoon.reflect.declaration.CtFormalTypeDeclarer)

**Class:** spoon.support.visitor.MethodTypingContext

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/MethodTypingContext.java#L313)

This method is **pseudo-tested**.


It can not be accessed from other classes. 
It has been covered by 65 test method(s) with a minimum stack distance of 2.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.generics.GenericsTest.testIsGenericTypeEqual() at distance(s): 2
* spoon.test.generics.GenericsTest.testMethodTypingContextAdaptMethod() at distance(s): 2
* spoon.test.generics.GenericsTest.testIsSameSignatureWithReferencedGenerics() at distance(s): 4, 5
* spoon.test.generics.GenericsTest.testClassTypingContextMethodSignature() at distance(s): 4, 5
* spoon.test.generics.GenericsTest.testIsSameSignatureWithMethodGenerics() at distance(s): 4, 5
* spoon.test.generics.GenericsTest.testIsSameSignatureWithGenerics() at distance(s): 4, 5
* spoon.test.metamodel.MMMethod.overrides(spoon.reflect.declaration.CtMethod) at distance(s): 5
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 6
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 8
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 9
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 9
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 9
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 10
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 10
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 10
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 10
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 10
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 10
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 10
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 10
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 10
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 10
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 10, 11
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 10
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 10
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 10
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 10, 11
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 10, 11
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 24, 26, 27, 28, 29
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 24, 25, 26, 27, 28, 29, 30
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 24, 25, 26
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 24, 25, 26, 27, 28, 29, 30
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 24, 25, 26, 27, 28, 29, 30, 31, 32
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 24, 25
* spoon.test.interfaces.InterfaceTest.testRedefinesStaticMethodInSubInterface() at distance(s): 25
* spoon.test.lambda.LambdaTest.testLambdaMethod() at distance(s): 25
* spoon.test.interfaces.InterfaceTest.testExtendsStaticMethodInSubInterface() at distance(s): 25
* spoon.test.interfaces.InterfaceTest.testExtendsDefaultMethodInSubInterface() at distance(s): 25
* spoon.test.imports.ImportTest.testGetImportKindReturnRightValue() at distance(s): 25
* spoon.test.interfaces.InterfaceTest.testRedefinesDefaultMethodInSubInterface() at distance(s): 25
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 26, 27
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 26, 27, 28, 29, 30, 31, 32
* spoon.test.lambda.LambdaTest.testGetOverriddenMethodWithFunction() at distance(s): 26
* spoon.test.method.MethodTest.testGetAllMethods() at distance(s): 26
* spoon.test.reference.TypeReferenceTest.testGetAllExecutablesForInterfaces() at distance(s): 27
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 28
* spoon.test.parameters.ParameterTest.testMultiParameterLambdaTypeReference() at distance(s): 29
* spoon.test.lambda.LambdaTest.testEqualsLambdaParameterRef() at distance(s): 29
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 31, 33
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 31, 32, 33
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 32, 33, 34, 35, 36, 37
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 34, 35, 36, 37, 38, 39, 40, 62, 68
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 73
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 55, 56, 99, 100
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 56, 57, 58, 59, 112, 113, 114, 115
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 58
* spoon.test.filters.FilterTest.testOverriddenMethodFromAbstractClass() at distance(s): 58, 61
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 58
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 59, 86
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 59, 86
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 59, 86
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 59, 86
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 66, 68, 112
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 104, 105, 108, 109, 110, 113
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 105, 107, 132, 134, 159


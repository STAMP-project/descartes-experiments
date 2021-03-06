# setLabel(java.lang.String)

**Class:** spoon.support.reflect.code.CtInvocationImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/reflect/code/CtInvocationImpl.java#L158)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 54 test method(s) with a minimum stack distance of 14.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return null;
```





## Observed test methods

* spoon.generating.CtBiScannerGenerator.process() at distance(s): 14, 15, 16, 17, 19, 20, 21, 22, 24, 26
* spoon.test.parent.ParentContractTest.testContract() at distance(s): 15, 17
* spoon.test.replace.ReplaceParametrizedTest.testContract() at distance(s): 15, 17
* spoon.test.parent.SetParentTest.testContract() at distance(s): 15, 17
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 16, 18
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 16, 18
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 16, 17, 18, 19
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 16, 18
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 16, 17, 18, 19
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 16, 17, 18, 19
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 16, 17, 18, 19
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 16, 17, 18, 19
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 16, 17, 18, 19
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 16, 18
* spoon.test.ctBlock.TestCtBlock.testAddStatementInCase() at distance(s): 18, 20
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 21, 23, 26, 28, 30, 32
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 21, 23, 27, 29, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 98, 100, 101, 103, 108, 110, 113, 115
* spoon.test.prettyprinter.QualifiedThisRefTest.testCloneThisAccess() at distance(s): 22, 24
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 22, 24
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 22, 24, 27, 29, 31
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 23, 25, 27, 29
* spoon.test.reference.CloneReferenceTest.testGetDeclarationAfterClone() at distance(s): 27, 29, 36, 38, 41, 43, 46, 48
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 27, 29, 36, 38, 41, 43, 46, 48
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 27, 29
* spoon.test.ctBlock.TestCtBlock.testAddStatementInBlock() at distance(s): 27, 29
* spoon.test.reference.CloneReferenceTest.testGetDeclarationOfFieldAfterClone() at distance(s): 27, 29, 36, 38, 41, 43, 46, 48
* spoon.test.generics.GenericsTest.testTypeParameterDeclarer() at distance(s): 27, 29
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 28, 30
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 28, 30
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 51, 53
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 29, 31
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 29, 31
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 29, 31, 33, 35
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 29, 30, 31, 32
* spoon.generating.RoleHandlersGenerator.process() at distance(s): 29, 31, 33, 35, 36, 37, 38, 39, 41
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 29, 31, 34, 36
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 29, 31, 33, 35, 37, 39, 41, 43
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 29, 31
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 29, 31
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 29, 31, 32, 34, 38, 39, 40, 41, 42, 43, 44, 45, 47
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 30, 32, 35, 37
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 31, 33
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 31, 33, 51, 53
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 32, 34
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 32, 34
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 32, 34
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 32, 33, 34, 35
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 33, 35, 63, 65
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 33, 35
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 33, 35
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 33, 35
* spoon.test.factory.FactoryTest.testClone() at distance(s): 44, 46
* spoon.test.method.MethodTest.testClone() at distance(s): 44, 46
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 46, 48


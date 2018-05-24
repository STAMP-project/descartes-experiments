# visitCtInvocation(spoon.reflect.code.CtInvocation)

**Class:** spoon.support.visitor.clone.CloneBuilder

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/clone/CloneBuilder.java#L166)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 54 test method(s) with a minimum stack distance of 13.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.generating.CtBiScannerGenerator.process() at distance(s): 13, 14, 18, 19, 23
* spoon.test.parent.ParentContractTest.testContract() at distance(s): 14
* spoon.test.replace.ReplaceParametrizedTest.testContract() at distance(s): 14
* spoon.test.parent.SetParentTest.testContract() at distance(s): 14
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 15
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 15
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 15, 16
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 15
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 15, 16
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 15, 16
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 15, 16
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 15, 16
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 15, 16
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 15
* spoon.test.ctBlock.TestCtBlock.testAddStatementInCase() at distance(s): 17
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 20, 25, 29
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 20, 26, 31, 32, 36, 37, 38, 41, 42, 43, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 62, 63, 64, 65, 68, 69, 70, 74, 75, 76, 79, 80, 81, 84, 85, 86, 89, 90, 91, 95, 97, 100, 107, 112
* spoon.test.prettyprinter.QualifiedThisRefTest.testCloneThisAccess() at distance(s): 21
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 21
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 21, 26, 28
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 22, 26
* spoon.test.reference.CloneReferenceTest.testGetDeclarationAfterClone() at distance(s): 26, 35, 40, 45
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 26, 35, 40, 45
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 26
* spoon.test.ctBlock.TestCtBlock.testAddStatementInBlock() at distance(s): 26
* spoon.test.reference.CloneReferenceTest.testGetDeclarationOfFieldAfterClone() at distance(s): 26, 35, 40, 45
* spoon.test.generics.GenericsTest.testTypeParameterDeclarer() at distance(s): 26
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 27
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 27
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 27, 31, 32, 35, 36, 39, 40, 41, 44, 45, 50
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 28
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 28
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 28, 32
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 28, 29
* spoon.generating.RoleHandlersGenerator.process() at distance(s): 28, 30, 34, 35, 38
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 28, 33
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 28, 32, 36, 40
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 28
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 28
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 28, 31, 37, 38, 41, 42, 44
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 29, 34
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 30
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 30, 50
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 31
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 31
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 31
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 31, 32
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 32, 62
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 32
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 32
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 32
* spoon.test.factory.FactoryTest.testClone() at distance(s): 43
* spoon.test.method.MethodTest.testClone() at distance(s): 43
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 45


# scanCtStatement(spoon.reflect.code.CtStatement)

**Class:** spoon.support.visitor.clone.CloneBuilder

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/clone/CloneBuilder.java#L87)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 66 test method(s) with a minimum stack distance of 10.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 10, 21, 22, 27, 28, 32, 33, 34, 38, 39, 40, 43, 44, 45, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 64, 65, 66, 67, 68, 70, 71, 72, 76, 77, 78, 81, 82, 83, 86, 87, 88, 91, 92, 93, 97, 99, 102, 109, 114
* spoon.generating.CtBiScannerGenerator.process() at distance(s): 11, 14, 15, 16, 20, 21, 25
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 13, 17, 22
* spoon.test.reference.CloneReferenceTest.testGetDeclarationAfterClone() at distance(s): 13, 22, 27, 28, 31, 36, 37, 41, 42, 47
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 13, 22, 27, 28, 31, 36, 37, 41, 42, 47
* spoon.test.ctBlock.TestCtBlock.testAddStatementInCase() at distance(s): 13, 18, 19
* spoon.test.ctBlock.TestCtBlock.testAddStatementInBlock() at distance(s): 13, 18, 19, 22, 28
* spoon.test.reference.CloneReferenceTest.testGetDeclarationOfFieldAfterClone() at distance(s): 13, 22, 27, 28, 31, 36, 37, 41, 42, 47
* spoon.test.generics.GenericsTest.testTypeParameterDeclarer() at distance(s): 13, 22, 28
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 14
* spoon.test.parent.ParentContractTest.testContract() at distance(s): 14, 15, 16, 17, 18
* spoon.test.replace.ReplaceParametrizedTest.testContract() at distance(s): 14, 15, 16, 17, 18
* spoon.test.reference.VariableAccessTest.testReferences() at distance(s): 14
* spoon.test.intercession.insertBefore.InsertMethodsTest.testInsertAfterSwitchCase() at distance(s): 14
* spoon.test.parent.SetParentTest.testContract() at distance(s): 14, 15, 16, 17, 18
* spoon.test.intercession.insertBefore.InsertMethodsTest.testInsertBeforeSwitchCase() at distance(s): 14
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 15, 19, 24, 28, 29
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 15, 17, 24, 25, 26, 29, 30, 31, 34
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 15, 17, 22, 23, 24, 28, 29, 30
* spoon.generating.RoleHandlersGenerator.process() at distance(s): 15, 17, 22, 24, 26, 30, 31, 32, 36, 37, 40
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 15
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 16, 22, 27, 31
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 16, 17, 21, 23, 25, 26, 28, 30, 32, 35, 37, 42
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 17
* spoon.test.prettyprinter.QualifiedThisRefTest.testCloneThisAccess() at distance(s): 17, 23
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 17, 31, 36
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 17, 23
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 17, 18
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 17
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 17, 19, 28, 33, 34
* spoon.test.factory.FactoryTest.testClone() at distance(s): 17, 22, 28, 30, 39, 45
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 17, 18
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 17, 19, 28, 33, 34
* spoon.test.method.MethodTest.testClone() at distance(s): 17, 22, 28, 30, 39, 45
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 17, 18
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 17, 23
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 17, 18
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 17, 18
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 17, 22, 26, 32, 46, 52
* spoon.test.api.AwesomeProcessor.process(spoon.reflect.declaration.CtClass) at distance(s): 17, 23
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 17, 18
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 17, 25, 31
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 18, 27, 32, 33
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 18, 27, 32, 33, 34, 38, 43
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 18, 27, 32, 33
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 18, 24, 27, 29, 30, 32, 33, 34
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 18, 24, 25, 26, 27, 29, 30, 33, 34, 35, 38, 39, 40, 43, 44, 45, 46, 49, 51
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 19, 24
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 23, 29
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 23, 24, 29, 30, 34
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 23, 29
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 23, 28, 29, 32, 33, 34, 37, 38, 41, 42, 43, 46, 47, 52
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 24, 28
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 24, 30
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 24, 29, 34, 46, 51, 55, 60, 64
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 24, 29
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 24, 30
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 24, 29
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 24, 30, 35
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 24, 29, 30, 34, 38, 42
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 24, 29, 30
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 24, 30, 41, 47
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 24, 29, 34
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 24
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 25, 28, 31, 36
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 32, 41, 47


# visitCtExecutableReference(spoon.reflect.reference.CtExecutableReference)

**Class:** spoon.support.visitor.equals.EqualsChecker

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/equals/EqualsChecker.java#L213)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 43 test method(s) with a minimum stack distance of 13.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 13
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 13
* spoon.test.executable.ExecutableRefTest.testOverridingMethod() at distance(s): 13
* spoon.test.reference.ExecutableReferenceTest.testCallMethodOfClassNotPresent() at distance(s): 13
* spoon.test.reference.ExecutableReferenceTest.testHashcodeWorksWithReference() at distance(s): 13
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 13
* spoon.test.lambda.LambdaTest.testEqualsLambdaParameterRef() at distance(s): 13
* spoon.test.filters.FilterTest.unionOfTwoFilters() at distance(s): 16
* spoon.test.ctBlock.TestCtBlock.testAddStatementInCase() at distance(s): 17
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureWithVariableAccess() at distance(s): 17
* spoon.test.parameters.ParameterTest.testGetParameterReferenceInLambdaNoClasspath() at distance(s): 17
* spoon.test.reference.TypeReferenceTest.testEqualityTypeReference() at distance(s): 17
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 18, 35, 74, 91
* spoon.test.processing.ProcessingTest.testInsertBegin() at distance(s): 21
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 21, 26, 75, 78, 79, 82
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 23, 30, 37, 41, 48
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 23, 28, 32, 33, 36, 37, 38, 40, 41, 45, 46, 53
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 25, 29, 33, 34
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 26
* spoon.test.ctBlock.TestCtBlock.testAddStatementInBlock() at distance(s): 26
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 28, 32, 33, 37, 41, 45
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 28, 33, 37, 38, 41, 46, 47, 50
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 28, 32, 33, 36, 37, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 58, 59, 60, 64, 68, 69, 72, 80
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorClass() at distance(s): 29
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorName() at distance(s): 29
* spoon.testing.FileAssertTest.testEqualsBetweenTwoSameFile() at distance(s): 29
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorInstantiated() at distance(s): 29
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 31, 40, 43, 45, 47, 50, 59
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 32
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 32, 35, 42, 44, 45, 47, 76, 79
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 35, 79
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 41, 44, 45, 46, 47, 48
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 45, 47, 91
* spoon.test.serializable.SerializableTest.testSerializationModelStreamer() at distance(s): 51
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 51, 95
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 51, 95
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 58, 61, 62, 67, 83
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 65, 89, 91, 93, 110, 112, 113, 118, 125, 126
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 70, 74
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 71, 80
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 75, 78
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 76


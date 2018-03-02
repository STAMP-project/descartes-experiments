# addClassReference(spoon.reflect.reference.CtTypeReference)

**Class:** spoon.support.visitor.java.JavaReflectionTreeBuilder$7

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/java/JavaReflectionTreeBuilder.java#L422)

This method is **pseudo-tested**.


It can not be accessed from other classes. 
It has been covered by 147 test method(s) with a minimum stack distance of 9.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 9, 10, 11, 12, 13, 14
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerArrayReference() at distance(s): 10, 11, 12
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 10, 11, 12, 13
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerAnnotation() at distance(s): 10, 11, 13
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 11, 12, 27, 28, 78, 79, 86, 87, 88, 104
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 11, 12, 13, 14, 15, 16, 17, 18
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 11, 12, 13, 14, 15
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredMethods() at distance(s): 12
* spoon.test.api.MetamodelTest.testGetterSetterFroRole() at distance(s): 12, 28, 85
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 12, 18, 19, 21
* spoon.test.annotation.AnnotationTest.testSpoonManageRecursivelyDefinedAnnotation() at distance(s): 12
* spoon.test.annotation.AnnotationTest.testAccessAnnotationValue() at distance(s): 12
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 13, 14, 15, 16, 26, 28
* spoon.test.parent.ParentContractTest.testContract() at distance(s): 13
* spoon.test.replace.ReplaceParametrizedTest.testContract() at distance(s): 13
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 13, 14
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 14, 15, 17, 27, 28, 29, 30
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 14, 15, 16, 17
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 15, 16, 17, 18
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 15, 16, 17, 18
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 15, 16, 17, 18
* spoon.test.casts.CastTest.testCast2() at distance(s): 15, 16, 17, 18
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 15, 16, 17, 18
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 15, 16, 17, 18
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 15, 16, 17, 18
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 15, 16, 17, 18
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 15, 16, 17, 18
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 15, 16, 17, 18
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 15, 16, 17, 18
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 15, 16, 17, 18
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 15, 16, 17, 18
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 15, 16, 17, 18
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 15, 16, 17, 18, 24, 25, 26, 27
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 15, 16, 17, 18, 28, 30
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 15, 16, 17, 18
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 15, 16, 17, 18
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 15, 16, 17, 18
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 15, 16, 17, 18, 23, 24, 25, 26
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 15, 16, 17, 18
* spoon.test.casts.CastTest.testCast3() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 15, 16, 17, 18
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 15, 16, 17, 18
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 15, 16, 17, 18
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 15, 16, 17, 18
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 15, 16, 17, 18
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 15, 16, 17, 18
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 15, 16, 17, 18
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 15, 16, 17, 18
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 15, 16, 17, 18
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 15, 16, 17, 18
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 15, 16, 17, 18
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 15, 16, 17, 18
* spoon.test.casts.CastTest.testCast1() at distance(s): 15, 16, 17, 18
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 15, 16, 17, 18
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 15, 16, 17, 18
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 16, 18, 39, 52, 53
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 16, 17, 39, 52, 53
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 16
* spoon.test.lambda.LambdaTest.testGetDeclarationOnTypeParameterFromLambda() at distance(s): 16
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 16, 17
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 17
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 17, 31, 34, 35, 36, 37, 44, 45
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 17
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 17, 18
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 17, 18
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 17, 18
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 17, 32, 34
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 17, 21, 22, 23, 24, 25, 26, 36
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 17, 18
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 17, 18, 40, 53, 54
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 17, 59, 61, 62, 75, 76
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 17, 18
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 17, 18, 40, 53, 54
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 17, 18, 50
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 17, 18, 20
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 17, 61, 62, 63, 64, 65, 66, 73, 74, 75, 76, 77, 78, 82, 83, 84, 85
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 17, 18, 20
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 17, 18
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 17, 18, 40, 53, 54
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 17, 18
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 17, 18
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 17, 18
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 17
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 17
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 17, 18
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 17, 18, 20
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 17
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 17
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 18, 19, 20, 21
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 18, 25, 38, 39
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 18, 25, 38, 39
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 18, 25, 38, 39
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 18, 25, 38, 39
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 18, 25, 38, 39
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 18, 52, 65, 66
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 18, 19, 20, 21, 22, 23
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 18, 25, 38, 39
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 18, 19, 20, 21, 22, 23
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 19, 20, 22
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 19, 20, 21
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 19, 20, 21, 22, 23, 24, 26
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 19, 20, 22
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 19, 20, 22
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 19, 20, 22
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 19, 20, 21, 22, 23, 24
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 19, 21, 22
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 19, 21
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithSimpleImport() at distance(s): 20
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 20, 21, 22
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 20, 21, 22
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 20, 21, 22
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 20, 21, 22, 23, 24, 25
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 21, 22
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 21
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 21, 22
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 21, 22
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 23, 25, 35, 37, 95, 96, 97, 98, 99, 109
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 24, 25, 27, 29, 51, 52, 53, 54
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 25, 26, 28, 30, 52, 53, 54, 55
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldByReflection() at distance(s): 26, 28, 29
* spoon.test.filters.FilterTest.testAnnotationFilter() at distance(s): 27, 28
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 28, 29, 30
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 29, 30, 31, 32, 33
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 46, 47, 49
* spoon.reflect.ast.AstCheckerTest.testPushToStackChanges() at distance(s): 47
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 57, 58, 60, 61, 62, 63
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 57, 70, 71
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 64
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 83, 85
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 75, 76, 77, 78, 80
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 79, 80, 82, 83, 84, 85
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 79, 80, 82, 83, 84, 85
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 79, 80, 82, 83, 84, 85
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 79, 80, 82, 83, 84, 85
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 84, 86, 87, 88, 89, 90, 103, 104, 105, 106, 107, 108, 117
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 97, 108, 111, 112, 113, 114
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 97, 108, 111, 112, 113, 114
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 97, 108, 111, 112, 113, 114
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 125, 126, 128, 129, 130, 131


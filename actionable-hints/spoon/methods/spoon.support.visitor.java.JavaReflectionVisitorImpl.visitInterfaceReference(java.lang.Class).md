# visitInterfaceReference(java.lang.Class)

**Class:** spoon.support.visitor.java.JavaReflectionVisitorImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/java/JavaReflectionVisitorImpl.java#L345)

This method is **pseudo-tested**.


It can not be accessed from other classes. 
It has been covered by 159 test method(s) with a minimum stack distance of 5.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredMethods() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerArrayReference() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerInterface() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerGenericsInClass() at distance(s): 5
* spoon.test.parent.SetParentTest.testContract() at distance(s): 6
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 6, 8
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 7, 9, 11, 21
* spoon.test.secondaryclasses.ClassesTest.testAnonymousClass() at distance(s): 7
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 7, 9, 11
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 7
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredField() at distance(s): 7
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 7, 8, 9, 10
* spoon.test.annotation.AnnotationTest.testAnnotationValueReflection() at distance(s): 7
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 7
* spoon.test.enums.EnumsTest.testGetAllMethods() at distance(s): 8
* spoon.test.compilation.CompilationTest.testSingleClassLoader() at distance(s): 9
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 10, 12, 22, 23
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 10
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 11
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 11
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 11
* spoon.test.casts.CastTest.testCast2() at distance(s): 11
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 11, 22
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 11
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 11
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 11
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 11
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 11
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 11
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 11
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 11
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 11
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 11
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 11
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 11
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 11, 20
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 11
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 11, 13, 23
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 11
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 11
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 11
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 11
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 11, 19
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 11
* spoon.test.casts.CastTest.testCast3() at distance(s): 11
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 11
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 11
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 11
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 11
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 11
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 11
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 11
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 11
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 11
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 11
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 11
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 11
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 11
* spoon.test.casts.CastTest.testCast1() at distance(s): 11
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 11
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 11
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 11
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 11
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 12
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 13, 15
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 13, 15
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 13, 15
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 14
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 14, 16
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 14
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 14, 16, 18
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 14, 16, 18
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 15, 17
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 15
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 15
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 15, 17, 19, 21
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 15, 17, 19
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 15
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 15, 17
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 15, 17
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 15
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 15
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 15
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 15, 17, 19
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 15
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 15
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 15
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 16, 18, 20
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 17, 69, 79, 80, 81, 82, 83, 84, 86, 87, 88
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 17, 26, 31
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 18, 27, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 18, 27, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 18, 27, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 18, 27, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 18, 27, 32
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 18, 30, 84, 90, 92, 100, 101, 102, 103, 104
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 18, 27, 32
* spoon.test.lambda.LambdaTest.testBuildExecutableReferenceFromLambda() at distance(s): 19
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 19
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 19
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 20
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 20, 21, 22, 23, 46, 47
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 20
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 20, 22, 24, 25, 26
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses() at distance(s): 21
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 21, 22, 23, 24, 47, 48
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 22, 32, 33
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 22, 23, 24, 25, 26
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 23
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 24, 27, 30, 32, 38
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 25
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 26
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 26
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 26
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 26, 27
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 26
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 26
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 27
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 27
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 27
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 27, 33
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 27
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 27, 33, 47
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 27
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 27
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 27, 33, 47
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 27
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 27
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 27
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 28, 45, 59
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 29
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 29
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 30, 32, 46
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 31, 33, 47
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 32, 46
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 34, 36
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 35
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 42
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 42, 44
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 50, 64
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 51, 57, 59, 69, 70, 71, 78
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 53, 54, 55, 56
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 54, 55, 69
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 62, 64, 66, 68, 72, 78
* spoon.test.reference.VariableAccessTest.testDeclaringTypeOfALambdaReferencedByParameterReference() at distance(s): 69
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 71
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 75, 76, 77, 78
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 75, 76, 77, 78
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 75, 76, 77, 78
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 75, 76, 77, 78
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 76
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 79, 83, 85, 95, 99, 112
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 83
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 107
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 107
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 107
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 121, 122, 123, 124
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 126


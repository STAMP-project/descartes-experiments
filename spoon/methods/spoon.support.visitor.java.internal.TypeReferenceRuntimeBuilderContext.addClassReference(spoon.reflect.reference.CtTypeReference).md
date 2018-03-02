# addClassReference(spoon.reflect.reference.CtTypeReference)

**Class:** spoon.support.visitor.java.internal.TypeReferenceRuntimeBuilderContext

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/java/internal/TypeReferenceRuntimeBuilderContext.java#L41)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 96 test method(s) with a minimum stack distance of 9.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 9, 10, 12, 13, 14, 16, 18
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 12, 13, 14, 15, 16
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 14
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 14, 18, 19
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 14, 17, 18
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 15, 18, 19
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 15, 18, 19
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 15, 18, 19
* spoon.test.casts.CastTest.testCast2() at distance(s): 15, 18, 19
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 15, 18, 19
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 15, 18, 19
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 15, 18, 19
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 15, 18, 19
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 15, 18, 19
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 15, 18, 19
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 15, 18, 19
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 15, 18, 19
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 15, 18, 19
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 15, 18, 19
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 15, 18, 19
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 15, 18, 19
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 15, 18, 19
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 15, 18, 19, 24, 27, 28
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 15, 18, 19
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 15, 18, 19
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 15, 18, 19
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 15, 18, 19
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 15, 18, 19
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 15, 18, 19, 23, 26, 27
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 15, 18, 19
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 15, 18, 19
* spoon.test.casts.CastTest.testCast3() at distance(s): 15, 18, 19
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 15, 18, 19
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 15, 18, 19
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 15, 18, 19
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 15, 18, 19
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 15, 18, 19
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 15, 18, 19
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 15, 18, 19
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 15, 18, 19
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 15, 18, 19
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 15, 18, 19
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 15, 18, 19
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 15, 18, 19
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 15, 18, 19
* spoon.test.casts.CastTest.testCast1() at distance(s): 15, 18, 19
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 15, 18, 19
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 15, 18, 19
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 15, 18, 19
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 15, 18, 19
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 16, 17, 18, 20, 27
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 17, 22
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 17, 22
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 17, 22
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 18, 21, 22
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 18, 23
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 18, 19, 20, 21, 22, 23, 24
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 18, 19, 20, 21, 22, 23, 24
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 19, 24
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 19, 20, 22, 29
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 19, 21, 23, 25
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 19, 24
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 19, 21, 22, 23, 24
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 19, 21, 22, 23, 24
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 19, 20, 21, 22, 23, 24, 25
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 20, 21, 22, 23, 24, 26
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 20, 21, 22, 23, 24, 25, 26
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 21, 22, 24, 25, 26, 28, 30
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 24, 25, 29
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 24, 28
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 25, 26, 30
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 27, 28, 29, 30, 31
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnType() at distance(s): 28
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnTypeRef() at distance(s): 29
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 30
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 38, 49
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 38, 42
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 44, 46
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 46, 51
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 50
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 57, 58, 62
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 75, 82, 85, 86
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 69, 70, 71, 72, 73, 75, 76, 77, 79, 81
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 75, 77, 78, 82
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 79, 80, 84
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 79, 80, 84
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 79, 80, 84
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 79, 80, 84
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 85, 86, 87, 88, 89
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 88, 90, 91, 101, 103, 104, 106, 107, 108, 110, 112
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 101, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 111, 114, 115
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 111, 114, 115
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 111, 114, 115
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 125, 126, 130


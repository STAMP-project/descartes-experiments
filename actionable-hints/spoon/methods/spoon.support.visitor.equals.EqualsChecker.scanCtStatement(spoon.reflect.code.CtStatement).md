# scanCtStatement(spoon.reflect.code.CtStatement)

**Class:** spoon.support.visitor.equals.EqualsChecker

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/equals/EqualsChecker.java#L71)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 205 test method(s) with a minimum stack distance of 10.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 10, 26
* spoon.test.processing.ProcessingTest.testInsertBegin() at distance(s): 10, 15
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 10, 26
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 10, 14, 15, 18, 19, 20, 23, 79, 81, 83, 85
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 11, 20, 25, 29, 30, 34
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoCtElementWithTheSameSignatureButNotTheSameContent() at distance(s): 11
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 11, 16, 20, 25, 30, 31, 32, 33, 34, 35, 38
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 11, 20, 25, 29, 30, 34, 35, 38, 42
* spoon.test.compilationunit.GetBinaryFilesTest.testAnonymousClasses() at distance(s): 11
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 11, 16, 20, 25, 29, 30, 31, 32, 33, 34, 38, 39, 42, 43, 44, 47, 48, 49, 52, 53, 56, 57, 61, 65, 66, 69
* spoon.test.delete.DeleteTest.testDeleteAStatementInConstructor() at distance(s): 12
* spoon.test.delete.DeleteTest.testDeleteAStatementInMethod() at distance(s): 12
* spoon.test.delete.DeleteTest.testDeleteStatementInCase() at distance(s): 12
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorClass() at distance(s): 12, 21, 26
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 12, 13, 31, 33
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorName() at distance(s): 12, 21, 26
* spoon.test.delete.DeleteTest.testDeleteACaseOfASwitch() at distance(s): 12
* spoon.test.delete.DeleteTest.testDeleteAStatementInAnonymousExecutable() at distance(s): 12
* spoon.testing.FileAssertTest.testEqualsBetweenTwoSameFile() at distance(s): 12, 21, 26
* spoon.test.delete.DeleteTest.testDeleteAStatementInStaticAnonymousExecutable() at distance(s): 12
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorInstantiated() at distance(s): 12, 21, 26
* spoon.testing.FileAssertTest.testEqualsBetweenTwoDifferentFile() at distance(s): 12
* spoon.test.parent.ParentTest.testGetParentWithFilter() at distance(s): 14
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 14, 18, 26
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 14, 26
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 14, 23, 28, 32, 37, 42, 47
* spoon.test.ctBlock.TestCtBlock.testAddStatementInCase() at distance(s): 14, 15
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureWithVariableAccess() at distance(s): 14
* spoon.test.ctBlock.TestCtBlock.testAddStatementInBlock() at distance(s): 14, 15, 18, 23
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 14, 26
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 14, 19, 26
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 14, 22, 26, 30, 31
* spoon.test.filters.FilterTest.unionOfTwoFilters() at distance(s): 14
* spoon.test.position.PositionTest.getPositionOfImplicitBlock() at distance(s): 14
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessDeclaredInADefaultClass() at distance(s): 15
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 17, 18, 19, 21, 36, 41, 47, 48, 49, 50
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 17
* spoon.generating.RoleHandlersGenerator.process() at distance(s): 17
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 18, 23, 26
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 18
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 18, 23, 26
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 18
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 18, 20, 79, 81
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 19, 20, 30, 32, 33, 34, 44, 45, 72, 93
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 20
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 23, 32, 33, 34, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 25
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 25
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 26
* spoon.test.casts.CastTest.testCast2() at distance(s): 26
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 26
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 26
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 26
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 26
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 26
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 26
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 26
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 26
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 26
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 26
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 26
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 26, 35
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 26
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 26
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 26
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 26
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 26, 34
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 26
* spoon.test.casts.CastTest.testCast3() at distance(s): 26
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 26
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 26
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 26
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 26
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 26
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 26
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 26
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 26
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 26
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 26
* spoon.test.casts.CastTest.testCast1() at distance(s): 26
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 26
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 26
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 26
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 26
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 28, 29, 31
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 28, 29, 31
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 28, 29, 31
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 29, 30, 32
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 29, 31, 33
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 29
* spoon.test.methodreference.MethodReferenceTest.setUp() at distance(s): 29, 31
* spoon.test.support.ResourceTest.testFilteringFolder() at distance(s): 29, 31
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 29, 30, 32
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 29, 31, 33
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 29, 30, 32
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 29, 31
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldInAnonymousClass() at distance(s): 30, 32
* spoon.test.imports.ImportScannerTest.testComputeImportsInClassWithSameName() at distance(s): 30, 31, 32, 33
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnParameterInMethod() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnLocalVariableInMethod() at distance(s): 30, 32
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testStaticClasses() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInNewInstance() at distance(s): 30, 32
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 30
* spoon.test.architecture.SpoonArchitectureEnforcerTest.noTreeSetInSpoon() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testNotTargetedExpression() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInStatements() at distance(s): 30, 32
* spoon.test.reference.ElasticsearchStackoverflowTest.testStackOverflow() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation() at distance(s): 30, 31, 32, 33
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationBeforeExceptionInSignatureOfMethod() at distance(s): 30, 32
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testSpecPackage() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInvInInnerClass() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInClassDeclaration() at distance(s): 30, 32
* spoon.test.factory.FieldFactoryTest.testCreateFromSource() at distance(s): 30, 32
* spoon.test.reference.VariableAccessTest.testVariableAccessDeclarationInAnonymousClass() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testGenericInField() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testDeclarationOfTypeParameterReference() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testTargetOfFieldAccess() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testClassTypingContext() at distance(s): 30, 32
* spoon.test.compilation.CompilationTest.testFilterResourcesDir() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testIsGenericsMethod() at distance(s): 30, 32
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessInAnonymousClass() at distance(s): 30, 32
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameterWithImports() at distance(s): 30, 31, 32, 33
* spoon.test.generics.GenericsTest.testClassTypingContextMethodSignature() at distance(s): 30, 32
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 30
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 30
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfStaticFieldAccess() at distance(s): 30, 32
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccess() at distance(s): 30, 32
* spoon.test.prettyprinter.PrinterTest.testFQNModeWriteFQNConstructorInCtVisitor() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessor() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInvInAnonymousClass() at distance(s): 30, 32
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 30, 32, 62, 73, 74, 77, 78, 79, 80, 82, 84, 85, 86, 88, 89, 90, 91, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 123, 124, 125, 126, 129, 130, 133, 135, 136, 141, 151, 168, 178
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 30, 31, 33
* spoon.test.annotation.AnnotationTest.testUsageOfParametersInTypeAnnotation() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInReturnTypeInMethod() at distance(s): 30, 32
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 30, 32, 34
* spoon.test.visibility.VisibilityTest.testInvocationVisibilityInFieldDeclaration() at distance(s): 30, 32
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 30, 31, 33
* spoon.test.annotation.AnnotationTest.testAnnotatedElementTypes() at distance(s): 30, 32
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 30, 32, 34, 54
* spoon.test.annotation.AnnotationValuesTest.testAnnotationPrintAnnotation() at distance(s): 30, 32
* spoon.test.trycatch.TryCatchTest.testRethrowingExceptionsJava7() at distance(s): 30, 32
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInCast() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInv() at distance(s): 30, 32
* spoon.reflect.visitor.CtScannerTest.testScan() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testGenericTypeReference() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testisGeneric() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testStaticTargetsOfInv() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testMethodTypingContextAdaptMethod() at distance(s): 30, 32
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccessInInnerClass() at distance(s): 30, 32
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameter() at distance(s): 30, 31, 32, 33
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInExtendsImplementsOfAClass() at distance(s): 30, 32
* spoon.test.generics.GenericsTest.testCtTypeReference_getSuperclass() at distance(s): 30, 32
* spoon.test.visibility.VisibilityTest.testFullyQualifiedNameOfTypeReferenceWithGeneric() at distance(s): 31, 32, 33, 34
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 31, 33
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 31, 33
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 31, 33
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 31, 33
* spoon.test.methodreference.MethodReferenceTest.testCompileMethodReferenceGeneratedBySpoon() at distance(s): 31, 33
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 31, 33
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 31, 33
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 31, 33
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 31, 32, 33, 34
* spoon.test.fieldaccesses.FieldAccessTest.testIncrementationOnAVarIsAUnaryOperator() at distance(s): 31, 33
* spoon.test.generics.GenericsTest.testRecursiveTypeAdapting() at distance(s): 31, 33
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionListener() at distance(s): 31, 32, 33, 34
* spoon.test.fieldaccesses.FieldAccessTest.testFieldWriteWithPlusEqualsOperation() at distance(s): 31, 33
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageFullQualified() at distance(s): 31, 33
* spoon.test.reference.TypeReferenceTest.testToStringEqualityBetweenTwoGenericTypeDifferent() at distance(s): 31, 33
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunction() at distance(s): 31, 32, 33, 34
* spoon.test.generics.GenericsTest.testTypeAdapted() at distance(s): 31, 33
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 31, 32, 34
* spoon.test.query_function.VariableReferencesTest.setup() at distance(s): 31, 33
* spoon.test.fieldaccesses.FieldAccessTest.testGetReference() at distance(s): 31, 33
* spoon.test.fieldaccesses.FieldAccessTest.testTypeOfFieldAccess() at distance(s): 31, 33
* spoon.test.ctType.CtTypeParameterTest.testTypeErasure() at distance(s): 31, 33
* spoon.test.generics.GenericsTest.testGenericsInQualifiedNameInConstructorCall() at distance(s): 32, 34
* spoon.test.generics.GenericsTest.testInvocationGenerics() at distance(s): 32, 34
* spoon.test.generics.GenericsTest.testConstructorCallGenerics() at distance(s): 32, 34
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 32
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 32, 34
* spoon.test.generics.GenericsTest.testNewClassGenerics() at distance(s): 32, 34
* spoon.test.generics.GenericsTest.testName() at distance(s): 32, 34
* spoon.test.generics.GenericsTest.testMethodsWithGenericsWhoExtendsObject() at distance(s): 32, 34
* spoon.test.serializable.SerializableTest.testSerializationModelStreamer() at distance(s): 34, 43, 48
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 35, 36
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 35, 46
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 35
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 36, 37
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 49
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 57
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 68, 69
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 68
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 83
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 86
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 90, 91
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 90, 91
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 90, 91
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 90, 91
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 107, 115, 116, 117
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 122
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 122
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 122
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 136, 137


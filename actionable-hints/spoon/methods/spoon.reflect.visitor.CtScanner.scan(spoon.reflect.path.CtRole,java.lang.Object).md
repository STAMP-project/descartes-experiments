# scan(spoon.reflect.path.CtRole,java.lang.Object)

**Class:** spoon.reflect.visitor.CtScanner

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/CtScanner.java#L198)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 361 test method(s) with a minimum stack distance of 6.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.comment.CommentTest.testCombinedPackageInfoComment() at distance(s): 6, 45, 46, 47
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 7, 8
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 8, 43
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessor() at distance(s): 12, 13, 17, 18, 19, 23, 24, 25, 29, 30, 34, 40, 41, 44, 47, 48, 49, 50, 53, 54, 55, 59, 60, 61, 65, 66, 67, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessorWithGlobalAnnotation() at distance(s): 12, 13, 17, 18, 23, 24, 25, 29, 34, 44, 45, 48, 49, 53, 54, 59, 60, 61, 65, 70, 80, 81
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 13, 14, 17, 18, 19, 20, 23, 24, 25, 27, 28, 29, 30, 32, 33, 35, 36, 37, 38, 41, 42, 43, 44, 47, 48, 49, 51, 52, 53, 54, 55, 58, 59, 60, 61, 64, 65, 66, 67, 69, 70, 71, 73, 74, 75, 76, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 95, 96, 101, 102
* spoon.test.api.APITest.testPrintNotAllSourcesWithFilter() at distance(s): 16, 17, 22, 23, 37, 38, 43, 44, 70
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 16, 59
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 16, 42, 43, 48, 49, 54, 55, 59, 60, 61, 64, 65, 70, 71, 75, 76, 81, 82, 87, 88, 92, 93, 98, 102, 103, 104, 108
* spoon.test.api.APITest.testPrintNotAllSourcesWithNames() at distance(s): 16, 17, 22, 23, 37, 38, 43, 44, 70
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 18, 50, 55, 56, 57, 62, 93, 94, 95
* spoon.test.prettyprinter.PrinterTest.testFQNModeWriteFQNConstructorInCtVisitor() at distance(s): 18, 24, 54, 60
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 18, 19, 49, 50, 51, 52, 56, 57
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 20, 59
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 21, 60
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 22, 27, 40, 43, 46, 47, 48, 49, 50, 52, 55
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 22, 23, 28, 29, 33, 34, 40, 43, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 60, 61, 62, 68, 69, 71, 72, 74, 77, 80, 83, 85, 86, 88, 89, 90, 93, 101, 104
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 22, 75
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 22, 27, 40, 43, 46, 47, 49, 50, 52, 53, 54, 55, 56, 58, 61, 68, 69, 71, 72, 74, 77, 80, 83, 90, 93, 101, 104
* spoon.test.compilationunit.TestCompilationUnit.testAddDeclaredTypeInCU() at distance(s): 22, 48
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 22, 27, 28, 33, 40, 43, 46, 47, 49, 50, 52, 54, 55, 58, 60
* spoon.generating.RoleHandlersGenerator.process() at distance(s): 23, 24
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 23, 28, 38, 39, 42, 44, 45, 50, 51, 52, 54, 56, 57, 61, 62, 63, 66, 67, 71, 72, 73, 77, 78, 79, 83, 84, 88, 89, 90, 94, 95, 100, 105, 106, 110, 111, 112
* spoon.test.prettyprinter.LinesTest.testPrettyPrinterWithLines() at distance(s): 23, 59
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 24, 38, 61, 62, 63, 68, 77, 78, 79, 82
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 24, 61, 62, 63, 68
* spoon.test.compilation.CompilationTest.testNewInstanceFromExistingClass() at distance(s): 28, 30, 55
* spoon.test.modifiers.TestModifiers.testGetModifiersHelpers() at distance(s): 28, 30, 55, 57, 62
* spoon.test.intercession.IntercessionContractTest.data() at distance(s): 29, 42, 48, 49, 54
* spoon.test.annotation.AnnotationTest.testGetAnnotationFromParameter() at distance(s): 30, 31, 41, 42
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionNoClasspath() at distance(s): 30
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 30
* spoon.reflect.ast.CloneTest.testCloneMethodsDeclaredInAST() at distance(s): 34, 43, 49, 50, 55, 56, 61, 71, 72, 77, 83, 93, 104
* spoon.reflect.ast.AstCheckerTest.testPushToStackChanges() at distance(s): 35, 39, 40, 41, 45, 48, 53, 54, 55, 58, 60, 63, 64, 70, 71, 72, 76, 81, 82, 92, 97, 103
* spoon.test.signature.SignatureTest.testBugSignature() at distance(s): 35
* spoon.test.pkg.PackageTest.testPackage() at distance(s): 35
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testStaticClasses() at distance(s): 36, 37, 42, 43, 48, 49, 52, 54, 55, 59, 60, 61, 64, 65, 69, 70, 71, 75, 76, 77, 81, 82, 86, 87, 88, 92, 93, 98, 103, 104, 108, 109, 110
* spoon.test.architecture.SpoonArchitectureEnforcerTest.noTreeSetInSpoon() at distance(s): 36, 37, 42, 43, 48, 49, 52, 54, 55, 59, 60, 61, 64, 65, 69, 70, 71, 75, 76, 77, 81, 82, 86, 87, 88, 92, 93, 98, 103, 104, 108, 109, 110
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 36, 37, 38
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testSpecPackage() at distance(s): 36, 37, 42, 43, 48, 49, 52, 54, 55, 59, 60, 61, 64, 65, 69, 70, 71, 75, 76, 77, 81, 82, 86, 87, 88, 92, 93, 98, 103, 104, 108, 109, 110
* spoon.test.compilationunit.GetBinaryFilesTest.testMultiClassInSingleFile() at distance(s): 36
* spoon.LauncherTest.testLauncherInEmptyWorkingDir() at distance(s): 36
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 36, 37, 42, 43, 48, 49, 54, 55, 60, 64, 70, 71, 75, 76, 77, 81, 82, 86, 87, 88, 92, 98, 103, 109, 110
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 36, 37, 42, 43, 48, 49, 52, 54, 55, 59, 60, 61, 64, 65, 69, 70, 71, 75, 76, 77, 81, 82, 86, 87, 88, 92, 93, 98, 103, 104, 108, 109, 110
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 36, 37, 42, 43, 48, 49, 53, 54, 55, 59, 60, 61, 62, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 96, 97, 98, 101, 102, 103, 104, 108, 109, 113, 114, 118, 129, 135
* spoon.test.reference.TypeReferenceTest.testGetTypeDeclaration() at distance(s): 36
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 36
* spoon.test.compilationunit.TestCompilationUnit.testGetUnitTypeWorksWithDeclaredPackage() at distance(s): 36
* spoon.testing.AbstractAssertTest.testTransformationFromCtElementWithProcessor() at distance(s): 40, 41, 42, 43
* spoon.reflect.visitor.CtVisitorTest.testMethodsInVisitor() at distance(s): 40, 43, 46, 47, 49, 50, 52, 53, 55, 56, 58, 61, 68, 69, 71, 72, 74, 77, 80, 83, 90, 93, 101, 104
* spoon.reflect.visitor.CtInheritanceScannerMethodsTest.testMethodsInInheritanceScanner() at distance(s): 40, 43, 46, 47, 49, 50, 52, 53, 55, 56, 58, 61, 68, 69, 71, 72, 74, 77, 80, 83, 90, 93, 101, 104
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 41
* spoon.test.pkg.PackageTest.testAnnotationOnPackage() at distance(s): 41, 43, 44, 47, 49, 50
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 41, 51, 53, 82, 84, 85
* spoon.test.filters.FilterTest.setup() at distance(s): 42, 43, 48, 49
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 42, 43, 48, 49, 54, 55, 59, 60, 61, 64, 65, 70, 71, 75, 76, 81, 82, 87, 88, 92, 93, 98, 103, 104, 108
* spoon.test.api.MetamodelTest.testGetterSetterFroRole() at distance(s): 42, 48, 49, 54
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoCtElementWithTheSameSignatureButNotTheSameContent() at distance(s): 42, 43
* spoon.test.generics.GenericsTest.testTypeParameterReference() at distance(s): 42, 43
* spoon.testing.CtElementAssertTest.testEqualityBetweenACtElementAndAString() at distance(s): 42, 43
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoDifferentCtElement() at distance(s): 42, 43
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnPackage() at distance(s): 42, 43, 48, 49, 54, 55, 60, 61, 65, 66
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 42, 48, 49, 54, 55, 60, 70, 71, 76, 82, 92, 103
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 42, 83, 84, 85, 86
* spoon.test.SpoonTestHelpers.getAllInstantiableMetamodelInterfaces() at distance(s): 42, 48, 49, 54, 55, 60, 70, 71, 76, 82, 92, 103
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoCtElement() at distance(s): 42, 43
* spoon.test.annotation.AnnotationTest.testAnnotatedElementTypes() at distance(s): 42, 43, 48, 49, 53, 54, 55, 59, 60, 61, 62, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 80, 81, 82, 83, 84, 86, 88, 89, 90, 96, 97, 102, 103
* spoon.reflect.visitor.CtScannerTest.testScannerContract() at distance(s): 42, 48, 49, 54, 55, 60, 70, 71, 76, 82, 92, 103
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 42, 48, 49, 54
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(java.io.File) at distance(s): 43, 49, 50, 55, 56, 61, 71, 72, 77, 83, 93, 104
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 43, 44, 45, 46, 51, 52
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 43, 84, 86, 87
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 43, 84, 86, 87
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 43, 44, 45, 46, 49, 50, 51, 52, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 76, 78, 79, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 94, 95, 96, 98, 99, 101, 102, 104, 105, 106, 107, 109, 111
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstants() at distance(s): 43, 44, 45, 46, 51, 52
* spoon.processing.ProcessingTest.testInterruptAProcessor() at distance(s): 43
* spoon.test.reference.ElasticsearchStackoverflowTest.testStackOverflow() at distance(s): 44, 49, 50, 54, 60, 66, 67, 72, 99, 127
* spoon.test.comment.CommentTest.testInLineComment() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testCodeFactory() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testJavaDocCommentOnUnix() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testJavaDocEmptyCommentAndTag() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testInsertNewComment() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testWildComments() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testRemoveComment() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testCoreFactory() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testCommentsInComment1And2() at distance(s): 45, 46, 47
* spoon.test.comment.CommentTest.testBlockComment() at distance(s): 45, 46, 47
* spoon.test.refactoring.RefactoringTest.testTransformedInstanceofAfterATransformation() at distance(s): 46, 47, 49, 50, 51, 52, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 93, 94, 95, 96, 101, 102, 103, 104, 105, 106, 107
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 46, 47, 49, 50, 51, 52, 55, 56, 57, 58, 60, 61, 62, 63, 65, 66, 67, 68, 70, 71, 73, 76, 78, 79, 96, 98, 99, 101, 102, 104, 106
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 46, 47, 49, 50, 51, 52, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 93, 94, 95, 96, 101, 102, 103, 104, 105, 106, 107
* spoon.test.refactoring.RefactoringTest.testThisInConstructorAfterATransformation() at distance(s): 46, 47, 49, 50, 51, 52, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 93, 94, 95, 96, 101, 102, 103, 104, 105, 106, 107
* spoon.test.support.ResourceTest.testFilteringFolder() at distance(s): 47, 80, 85
* spoon.test.prettyprinter.PrinterTest.testPrettyPrinter() at distance(s): 47, 48, 53, 96
* spoon.test.delete.DeleteTest.testDeleteAStatementInConstructor() at distance(s): 48, 81
* spoon.test.annotation.AnnotationTest.testPersistenceProperty() at distance(s): 48, 49
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 48
* spoon.test.prettyprinter.QualifiedThisRefTest.testCloneThisAccess() at distance(s): 48, 81
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 48, 54, 55, 60, 61, 62
* spoon.test.architecture.SpoonArchitectureEnforcerTest.statelessFactory() at distance(s): 48, 49, 54, 59, 60, 64, 65, 70, 75, 98, 103
* spoon.test.factory.FactoryTest.testIncrementalModel() at distance(s): 48
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 48, 54, 55, 60, 70, 71, 76, 82, 92, 103
* spoon.test.fieldaccesses.FieldAccessTest.testModelBuildingFieldAccesses() at distance(s): 48, 49
* spoon.test.arrays.ArraysTest.testArrayReferences() at distance(s): 48, 49, 73, 74
* spoon.test.position.PositionTest.testPositionInterface() at distance(s): 48, 49, 54
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 48, 49
* spoon.test.annotation.AnnotationTest.testModelBuildingAnnotationBoundUsage() at distance(s): 48, 54, 55, 60, 61, 62
* spoon.test.delete.DeleteTest.testDeleteAStatementInMethod() at distance(s): 48, 81
* spoon.test.delete.DeleteTest.testDeleteStatementInCase() at distance(s): 48, 81
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnConstructor() at distance(s): 48, 49, 54, 55, 60, 61, 65, 66
* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 48, 49, 54, 60, 66
* spoon.test.generics.GenericsTest.testGenericInField() at distance(s): 48, 49
* spoon.test.generics.GenericsTest.testClassTypingContext() at distance(s): 48, 49, 54, 60, 66
* spoon.test.compilation.CompilationTest.testFilterResourcesDir() at distance(s): 48, 49, 54, 55, 60, 65, 76, 81, 86, 104
* spoon.test.position.PositionTest.testPositionClass() at distance(s): 48, 49, 54
* spoon.test.delete.DeleteTest.testDeleteACaseOfASwitch() at distance(s): 48, 81
* spoon.test.generics.GenericsTest.testGenericMethodCallWithExtend() at distance(s): 48
* spoon.test.generics.GenericsTest.testClassTypingContextMethodSignature() at distance(s): 48, 49, 54, 60, 66
* spoon.test.annotation.AnnotationTest.testAnnotationWithDefaultArrayValue() at distance(s): 48, 49, 54, 55
* spoon.test.delete.DeleteTest.testDeleteMethod() at distance(s): 48, 81
* spoon.test.delete.DeleteTest.testDeleteAStatementInAnonymousExecutable() at distance(s): 48, 81
* spoon.test.delete.DeleteTest.testDeleteBodyOfAMethod() at distance(s): 48, 81
* spoon.test.annotation.AnnotationTest.annotationOverrideFQNIsOK() at distance(s): 48, 86
* spoon.test.generics.GenericsTest.testBugComparableComparator() at distance(s): 48, 49
* spoon.test.delete.DeleteTest.testDeleteChainOfAssignment() at distance(s): 48, 81
* spoon.test.position.PositionTest.testPositionAnnotation() at distance(s): 48, 49, 54
* spoon.test.model.TypeTest.testGetUsedTypes() at distance(s): 48
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnMethod() at distance(s): 48, 49, 54, 55, 60, 61, 65, 66
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnClass() at distance(s): 48, 49, 54, 55, 60, 61, 65, 66
* spoon.test.annotation.AnnotationTest.testModelBuildingAnnotationBound() at distance(s): 48, 49
* spoon.test.method.MethodTest.testClone() at distance(s): 48, 81
* spoon.test.casts.CastTest.testCase4() at distance(s): 48, 49, 59, 60, 70, 71
* spoon.test.compilationunit.TestCompilationUnit.testCompilationUnitDeclaredTypes() at distance(s): 48
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnField() at distance(s): 48, 49, 54, 55, 60, 61, 65, 66
* spoon.test.annotation.AnnotationTest.testAccessAnnotationValue() at distance(s): 48, 54, 55, 60, 61, 62
* spoon.test.invocations.InvocationTest.testIssue1753() at distance(s): 48, 76
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 48, 49
* spoon.test.pkg.PackageTest.testPrintPackageInfoWhenNothingInPackage() at distance(s): 48, 49, 50, 51
* spoon.test.annotation.AnnotationTest.testReplaceAnnotationValue() at distance(s): 48, 54, 55, 60, 61, 62
* spoon.test.delete.DeleteTest.testDeleteAClassTopLevel() at distance(s): 48, 81
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 48
* spoon.test.delete.DeleteTest.testDeleteAStatementInStaticAnonymousExecutable() at distance(s): 48, 81
* spoon.test.delete.DeleteTest.testDeleteConditionInACondition() at distance(s): 48, 81
* spoon.test.annotation.AnnotationValuesTest.testAnnotationPrintAnnotation() at distance(s): 48, 49, 53, 54, 55, 56
* spoon.test.executable.ExecutableRefTest.testGetActualClassTest() at distance(s): 48
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnParameter() at distance(s): 48, 49, 54, 55, 60, 61, 65, 66
* spoon.test.delete.DeleteTest.testDeleteReturn() at distance(s): 48, 81
* spoon.test.control.ControlTest.testModelBuildingFor() at distance(s): 48, 49
* spoon.test.generics.GenericsTest.testModelBuildingTree() at distance(s): 48, 49
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnLocalVariable() at distance(s): 48, 49, 54, 55, 60, 61, 65, 66
* spoon.test.eval.EvalTest.testArrayLength() at distance(s): 48, 49
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 48, 49
* spoon.test.generics.GenericsTest.testisGeneric() at distance(s): 48, 49, 54, 60, 66
* spoon.test.generics.GenericsTest.testBugCommonCollection() at distance(s): 48, 49, 54
* spoon.test.reference.TypeReferenceTest.testAnonymousClassesHaveAnEmptyStringForItsNameInNoClasspath() at distance(s): 48, 69, 70, 71
* spoon.test.delete.DeleteTest.testDeleteAnnotationOnAClass() at distance(s): 48, 81
* spoon.test.generics.GenericsTest.testMethodTypingContextAdaptMethod() at distance(s): 48, 49, 54, 60, 66
* spoon.test.delete.DeleteTest.testDeleteParameterOfMethod() at distance(s): 48, 81
* spoon.test.annotation.AnnotationTest.testAnnotationInterfacePreserveMethods() at distance(s): 48, 49
* spoon.test.model.TypeTest.superclassTest() at distance(s): 48
* spoon.test.generics.GenericsTest.testCtTypeReference_getSuperclass() at distance(s): 48, 49, 54, 60, 66
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 49, 51, 55, 56, 57, 62, 71, 73, 76
* spoon.test.casts.CastTest.testTypeAnnotationOnCast() at distance(s): 49, 50, 60, 61, 71, 72
* spoon.test.factory.FactoryTest.testClassAccessCreatedFromFactories() at distance(s): 49
* spoon.test.annotation.AnnotationValuesTest.testValuesOnJava7Annotation() at distance(s): 49, 50, 55, 56, 62, 76, 77, 83, 89
* spoon.test.executable.ExecutableRefTest.methodTest() at distance(s): 49
* spoon.test.executable.ExecutableRefTest.constructorTest() at distance(s): 49
* spoon.test.refactoring.RefactoringTest.testThisInConstructor() at distance(s): 49, 50, 51, 52, 57, 58, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 93, 94, 95, 96, 103, 104, 105, 106, 107
* spoon.test.reference.TypeReferenceTest.testToStringEqualityBetweenTwoGenericTypeDifferent() at distance(s): 49, 50, 82, 87
* spoon.test.annotation.AnnotationValuesTest.testValuesOnJava8Annotation() at distance(s): 49, 50, 55, 56, 62, 76, 77, 83, 89
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 49, 50
* spoon.test.query_function.VariableReferencesTest.setup() at distance(s): 49, 76
* spoon.test.generics.GenericsTest.testGenericsInQualifiedNameInConstructorCall() at distance(s): 50, 51, 52, 53, 56, 58, 59, 62, 63, 64, 68, 69, 70, 75
* spoon.test.generics.GenericsTest.testInvocationGenerics() at distance(s): 50, 51, 52, 53, 56, 58, 59, 62, 63, 64, 68, 69, 70, 75
* spoon.test.generics.GenericsTest.testConstructorCallGenerics() at distance(s): 50, 51, 52, 53, 56, 58, 59, 62, 63, 64, 68, 69, 70, 75
* spoon.test.generics.GenericsTest.testNewClassGenerics() at distance(s): 50, 51, 52, 53, 56, 58, 59, 62, 63, 64, 68, 69, 70, 75
* spoon.test.generics.GenericsTest.testName() at distance(s): 50, 51, 52, 53, 56, 58, 59, 62, 63, 64, 68, 69, 70, 75
* spoon.test.generics.GenericsTest.testMethodsWithGenericsWhoExtendsObject() at distance(s): 50, 51, 52, 53, 56, 58, 59, 62, 63, 64, 68, 69, 70, 75
* spoon.test.constructor.ConstructorTest.setUp() at distance(s): 50, 51, 52, 53, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 68, 69, 70, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88
* spoon.test.constructor.ConstructorTest.testTransformationOnConstructorWithInsertBegin() at distance(s): 50, 51, 55, 56, 57, 61, 62, 63, 73, 74, 78, 79, 80, 84, 85
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 52, 55, 57, 58, 61, 62, 63, 68, 79, 82, 84, 85
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 52, 55, 57, 58, 61, 62, 63, 68, 79, 82, 84, 85
* spoon.test.prettyprinter.LinesTest.setup() at distance(s): 53, 96
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 53, 54, 59, 60, 76, 77, 81, 82, 86, 87, 88
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.superInvocationWithEnclosingInstance() at distance(s): 53
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInAClassPackage() at distance(s): 53
* spoon.test.methodreference.MethodReferenceTest.setUp() at distance(s): 53, 54, 56, 57, 61, 62
* spoon.test.annotation.AnnotationTest.testDefaultValueInAnnotationsForAnnotationFields() at distance(s): 53, 54
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 53, 54, 56, 57, 59, 60, 62, 63, 67, 68, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91
* spoon.test.loop.LoopTest.testAnnotationInForLoop() at distance(s): 54, 55, 70, 71, 75, 76
* spoon.test.generics.GenericsTest.testIsSameSignatureWithReferencedGenerics() at distance(s): 54
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 54
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 54
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 54
* spoon.test.annotation.AnnotationTest.testInnerAnnotationsWithArray() at distance(s): 54, 55, 67, 68, 74, 75
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 54, 55
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 54, 81
* spoon.test.position.PositionTest.testPositionGeneric() at distance(s): 54
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 54, 55
* spoon.test.annotation.AnnotationTest.testRepeatableAnnotationAreManaged() at distance(s): 54, 55, 60, 61
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 54, 56, 61
* spoon.test.template.TemplateTest.testSimpleTemplate() at distance(s): 54
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 54
* spoon.test.staticFieldAccess.StaticAccessTest.testProcessAndCompile() at distance(s): 54, 76, 85
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 54
* spoon.test.annotation.AnnotationTest.testGetAnnotationOuter() at distance(s): 54, 55, 67, 68, 74, 75
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 54, 55, 56, 57, 60, 61, 62, 67
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotationWithArrays() at distance(s): 54, 55, 60, 61
* spoon.reflect.declaration.CtTypeInformationTest.setUp() at distance(s): 54
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 54
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotation() at distance(s): 54, 55, 60, 61
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 54, 55
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 54
* spoon.test.reference.VariableAccessTest.testSuperAccess() at distance(s): 54
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 54
* spoon.test.annotation.AnnotationTest.testAnnotationIntrospection() at distance(s): 54
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 54
* spoon.test.refactoring.MethodsRefactoringTest.testSubInheritanceHierarchyFunction() at distance(s): 54, 55, 60, 61, 77, 78, 82, 83, 87, 88, 89
* spoon.test.visibility.VisibilityTest.testInvocationVisibilityInFieldDeclaration() at distance(s): 54, 55, 60, 70, 81, 97, 103
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 54
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 54, 55, 60, 61, 77, 78, 82, 83, 87, 88, 89
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 54
* spoon.test.generics.GenericsTest.testIsSameSignatureWithMethodGenerics() at distance(s): 54
* spoon.test.secondaryclasses.ClassesTest.testInnerClassContruction() at distance(s): 54
* spoon.test.refactoring.MethodsRefactoringTest.testExecutableReferenceFilter() at distance(s): 54, 55, 60, 61, 77, 78, 82, 83, 87, 88, 89
* spoon.test.generics.GenericsTest.testIsSameSignatureWithGenerics() at distance(s): 54
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 54
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 54, 56, 61
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 54, 55, 56, 57, 61, 62
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 54
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 54
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 54
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 54, 60, 81
* spoon.test.targeted.TargetedExpressionTest.testCtSuperAccess() at distance(s): 54
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 54
* spoon.test.annotation.AnnotationTest.testWritingAnnotParamArray() at distance(s): 54, 55
* spoon.test.template.TemplateTest.testSubstitutionInsertAllNtoN() at distance(s): 54
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 54, 60, 81
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 54
* spoon.test.annotation.AnnotationTest.testRepeatableAnnotationAreManagedWithArrays() at distance(s): 54, 55, 60, 61
* spoon.test.loop.LoopTest.testForeachShouldHaveAlwaysABlockInItsBody() at distance(s): 54
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testElementMapFunction() at distance(s): 55, 82
* spoon.test.type.TypeTest.testTypeAccessOfArrayObjectInFullyQualifiedName() at distance(s): 55, 56, 57, 58, 62, 63, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 55, 56, 57, 58, 61, 62, 63, 68, 82, 84, 85
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 55, 82
* spoon.test.ctType.CtTypeTest.testIsSubTypeOf() at distance(s): 55
* spoon.test.filters.FilterTest.testQueryInQuery() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testInvalidQueryStepFailurePolicyIgnore() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testOverriddenMethodFromAbstractClass() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testReuseOfBaseQuery() at distance(s): 55, 82
* spoon.test.ctType.CtTypeTest.testHasMethodInSuperClass() at distance(s): 55, 57, 62
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 55, 82
* spoon.test.type.TypeTest.testTypeAccessForTypeAccessInInstanceOf() at distance(s): 55, 56, 57, 58, 62, 63, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90
* spoon.test.filters.FilterTest.testCtScannerListener() at distance(s): 55, 82
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 55, 56, 61, 82
* spoon.test.type.TypeTest.testIntersectionTypeReferenceInGenericsAndCasts() at distance(s): 55, 56, 57, 58, 62, 63, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90
* spoon.test.methodreference.MethodReferenceTest.testCompileMethodReferenceGeneratedBySpoon() at distance(s): 55, 56
* spoon.test.filters.FilterTest.testFilterChildrenWithoutFilterQueryStep() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testQueryStepScannWithConsumer() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testEarlyTerminatingQuery() at distance(s): 55, 82
* spoon.test.type.TypeTest.testTypeReferenceInGenericsAndCasts() at distance(s): 55, 56, 57, 58, 62, 63, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90
* spoon.test.annotation.AnnotationTest.testAnnotationTypeAndFieldOnField() at distance(s): 55, 56, 57, 58, 61, 63, 64, 66, 68, 73
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 55, 82
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeParameters() at distance(s): 55
* spoon.test.filters.FilterTest.testInvalidQueryStep() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testFunctionQueryStep() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testFilterQueryStep() at distance(s): 55, 82
* spoon.test.methodreference.MethodReferenceTest.testReferenceBuilderWithComplexGenerics() at distance(s): 55, 56
* spoon.test.filters.FilterTest.testParentFunction() at distance(s): 55, 82
* spoon.test.executable.ExecutableRefTest.testOverridingMethod() at distance(s): 55
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testElementMapConsumableFunction() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 55, 82
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 55, 61, 82
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 55
* spoon.test.reference.TypeReferenceTest.testRecursiveTypeReference() at distance(s): 55, 56, 57, 58, 62, 63
* spoon.test.filters.FilterTest.testOverriddenMethodFromInterface() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testReflectionBasedTypeFilter() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testReuseOfQuery() at distance(s): 55, 82
* spoon.test.executable.ExecutableTest.testBlockInExecutable() at distance(s): 55
* spoon.test.type.TypeTest.testTypeAccessForDotClass() at distance(s): 55, 56, 57, 58, 62, 63, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90
* spoon.test.filters.FilterTest.testClassCastExceptionOnForEach() at distance(s): 55, 82
* spoon.test.filters.FilterTest.testQueryWithOptionalNumberOfInputs() at distance(s): 55, 82
* spoon.test.ctType.CtTypeTest.testHasMethodInDefaultMethod() at distance(s): 55, 57, 62
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 55, 82
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 55
* spoon.test.enums.EnumsTest.testAnnotationsOnEnum() at distance(s): 56, 58, 63
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 56, 62, 83
* spoon.test.reference.VariableAccessTest.testDeclarationOfVariableReference() at distance(s): 58
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnParameterInMethod() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnLocalVariableInMethod() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInNewInstance() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInStatements() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 59
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation() at distance(s): 59, 60, 61, 62, 65, 66, 67, 68, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 96, 97, 98, 99, 102, 103, 104, 105
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationBeforeExceptionInSignatureOfMethod() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 59
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInClassDeclaration() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 59
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 59, 75
* spoon.test.annotation.AnnotationTest.testUsageOfParametersInTypeAnnotation() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 59, 75
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInReturnTypeInMethod() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 156, 157, 158, 159, 160, 161, 162, 169, 170, 172, 173
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInCast() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 59, 60
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 59, 75
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInExtendsImplementsOfAClass() at distance(s): 59, 60, 65, 66, 70, 76, 77, 80, 83, 84, 86, 89, 90, 96, 97, 102, 103
* spoon.test.annotation.AnnotationTest.testSpoonSpoonResult() at distance(s): 60, 61, 63, 65, 66, 68, 71, 72, 73, 74, 76, 77, 78, 79, 82, 86, 87, 89, 90, 92, 93, 95
* spoon.test.generics.GenericsTest.testDeclarationOfTypeParameterReference() at distance(s): 60
* spoon.test.generics.GenericsTest.testIsGenericsMethod() at distance(s): 60
* spoon.test.targeted.TargetedExpressionTest.testCtThisAccess() at distance(s): 60, 61
* spoon.test.type.TypeTest.testPolyTypBindingInTernaryExpression() at distance(s): 60, 66
* spoon.test.jdtimportbuilder.ImportBuilderTest.testInternalImportWhenNoClasspath() at distance(s): 60
* spoon.test.generics.GenericsTest.testGenericTypeReference() at distance(s): 60
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameLocalVariableToSameName() at distance(s): 61, 62, 66, 67, 77, 78, 82, 83, 84, 88, 89, 93, 94, 104, 105
* spoon.test.generics.GenericsTest.testDiamondComplexGenericsRxJava() at distance(s): 61, 62, 63, 67, 68, 69, 74
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 61
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRefactorWrongUsage() at distance(s): 61, 62, 66, 67, 77, 78, 82, 83, 84, 88, 89, 93, 94, 104, 105
* spoon.test.generics.GenericsTest.testTypeAdapted() at distance(s): 61
* spoon.test.reference.TypeReferenceTest.testIgnoreEnclosingClassInActualTypes() at distance(s): 61, 82
* spoon.test.ctType.CtTypeParameterTest.testTypeErasure() at distance(s): 61
* spoon.test.reference.TypeReferenceTest.testSubTypeAnonymous() at distance(s): 61, 82
* spoon.test.reference.TypeReferenceTest.testUnknownSuperClassWithSameNameInNoClasspath() at distance(s): 61, 63, 68
* spoon.test.trycatch.TryCatchTest.testCatchWithExplicitFinalVariable() at distance(s): 65, 67, 98, 99, 101
* spoon.test.lambda.LambdaTest.testFieldAccessInLambdaNoClassPathExternal1Example() at distance(s): 66, 72, 73
* spoon.test.ctClass.CtClassTest.testSpoonShouldInferImplicitPackageInNoClasspath() at distance(s): 66, 72, 94
* spoon.test.reference.ExecutableReferenceTest.testLambdaNoClasspath() at distance(s): 66, 67
* spoon.test.method.MethodTest.testGetAllMethods() at distance(s): 68
* spoon.test.reference.TypeReferenceTest.testAnnotationOnMethodWithPrimitiveReturnTypeInNoClasspath() at distance(s): 69, 70, 71
* spoon.test.limits.utils.InternalTest.testStaticFinalFieldInAnonymousClass() at distance(s): 70, 71
* spoon.test.constructorcallnewclass.NewClassTest.testNewClassInEnumeration() at distance(s): 70
* spoon.test.limits.utils.InternalTest.testInternalClasses() at distance(s): 70, 71
* spoon.test.arrays.ArraysTest.testInitializeWithNewArray() at distance(s): 70
* spoon.test.annotation.AnnotationLoopTest.testAnnotationDeclaredInForInit() at distance(s): 72, 73
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 75
* spoon.test.secondaryclasses.ClassesTest.testAnonymousClassInStaticField() at distance(s): 77, 104
* spoon.test.staticFieldAccess.StaticAccessTest.setUp() at distance(s): 79
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldInAnonymousClass() at distance(s): 81
* spoon.test.constructorcallnewclass.NewClassTest.testMoreThan9NewClass() at distance(s): 81, 113
* spoon.test.targeted.TargetedExpressionTest.testNotTargetedExpression() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInvInInnerClass() at distance(s): 81
* spoon.test.factory.FieldFactoryTest.testCreateFromSource() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testTargetOfFieldAccess() at distance(s): 81
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessInAnonymousClass() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfStaticFieldAccess() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccess() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInvInAnonymousClass() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInv() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testStaticTargetsOfInv() at distance(s): 81
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccessInInnerClass() at distance(s): 81
* spoon.test.fieldaccesses.FieldAccessTest.testTypeDeclaredInAnonymousClass() at distance(s): 82
* spoon.test.fieldaccesses.FieldAccessTest.testIncrementationOnAVarIsAUnaryOperator() at distance(s): 82
* spoon.test.fieldaccesses.FieldAccessTest.testFieldWriteWithPlusEqualsOperation() at distance(s): 82
* spoon.test.fieldaccesses.FieldAccessTest.testGetReference() at distance(s): 82
* spoon.test.fieldaccesses.FieldAccessTest.testTypeOfFieldAccess() at distance(s): 82
* spoon.test.pkg.PackageTest.testGetFQNInNoClassPath() at distance(s): 88
* spoon.test.type.TypeTest.test() at distance(s): 88
* spoon.test.trycatch.TryCatchTest.testMultiTryCatchWithCustomExceptions() at distance(s): 97
* spoon.test.trycatch.TryCatchTest.testCompileMultiTryCatchWithCustomExceptions() at distance(s): 97, 101, 103


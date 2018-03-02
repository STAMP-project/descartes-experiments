# visitConstructor(java.lang.reflect.Constructor)

**Class:** spoon.support.visitor.java.JavaReflectionVisitorImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/java/JavaReflectionVisitorImpl.java#L166)

This method is **pseudo-tested**.


It can not be accessed from other classes. 
It has been covered by 238 test method(s) with a minimum stack distance of 5.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredMethods() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerArrayReference() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 5, 7
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerEnum() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredConstructor() at distance(s): 5
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredField() at distance(s): 5, 7
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerGenericsInClass() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotationWithArrays() at distance(s): 6
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 6, 8
* spoon.test.imports.ImportTest.testEqualsImports() at distance(s): 6, 8
* spoon.test.type.TypeTest.testShadowType() at distance(s): 6, 7
* spoon.test.imports.ImportTest.testGetImportKindReturnRightValue() at distance(s): 6, 20
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 6
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 7, 9, 11, 21
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 7, 9, 11, 13
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 7, 26, 27, 28, 38, 51
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 7
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 7
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 7, 8, 9, 10
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 7, 9
* spoon.test.reference.ExecutableReferenceGenericTest.testReferencesBetweenConstructorsInOtherClass() at distance(s): 8
* spoon.test.reference.TypeReferenceTest.doNotCloseLoader() at distance(s): 8, 22
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionListener() at distance(s): 8, 17, 18, 19
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunction() at distance(s): 8, 17, 18, 19
* spoon.test.enums.EnumsTest.testGetAllMethods() at distance(s): 8
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses() at distance(s): 9, 21
* spoon.test.compilation.CompilationTest.testSingleClassLoader() at distance(s): 9
* spoon.test.lambda.LambdaTest.testGetDeclarationOnTypeParameterFromLambda() at distance(s): 9
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 10, 11, 13, 15, 18, 19, 20, 22, 25
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 10, 11, 13, 15, 18, 19, 21, 23
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 10, 12
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 10, 12
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 11, 13
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 11, 13
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 11, 13
* spoon.test.casts.CastTest.testCast2() at distance(s): 11, 13
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 11, 13, 22, 24, 34
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 11, 13
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 11, 13
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 11, 13
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 11, 13
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 11, 13
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 11, 13
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 11, 13
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 11, 13
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 11, 13
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 11, 13, 53
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 11, 13
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 11, 13
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 11, 13
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 11, 13, 23, 24
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 11, 13
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 11, 13
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 11, 13
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 11, 13
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 11, 13
* spoon.test.casts.CastTest.testCast3() at distance(s): 11, 13
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 11, 13
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 11, 13
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 11, 13
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 11, 13
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 11, 13
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 11, 13
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 11, 13
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 11, 13
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 11, 13
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 11, 13
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 11, 13
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 11, 13
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 11, 13
* spoon.test.casts.CastTest.testCast1() at distance(s): 11, 13
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 11, 13
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 11, 13
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 11, 13
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 11, 13
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 12, 127
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 12
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 13, 15
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 13, 15, 35
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 13, 15
* spoon.test.jdtimportbuilder.ImportBuilderTest.testSimpleStaticImport() at distance(s): 14
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 14, 42
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 14, 16
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 14, 76, 77
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 14, 16
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 14, 16, 18
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 14, 16, 18, 26
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 15, 17, 40
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 15, 89, 90
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 15, 79
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 15, 17, 19, 21
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 15, 17, 19, 85
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 15, 89, 90
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 15, 17, 40
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 15, 17, 83
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 15, 17, 83
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 15, 79
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 15, 17, 70
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 15, 17, 19, 24
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 15, 17, 89
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 15, 89, 90
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 16, 18, 20, 41
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 17, 19, 25, 26, 27
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionNoClasspath() at distance(s): 17
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 18, 26, 27, 28, 31, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 18, 26, 27, 28, 31, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 18, 26, 27, 28, 31, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 18, 26, 27, 28, 31, 32
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 18, 26, 27, 28, 31, 32
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 18, 79, 84, 90, 91, 92, 94, 100, 101, 102, 103, 104, 119
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 18, 26, 27, 28, 31, 32
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 20, 32
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 20, 21, 22, 23
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 20, 22, 30, 31, 32, 33
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 20, 22, 32
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 20, 22, 24, 25
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 21, 22, 23, 24
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 21
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 21
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnType() at distance(s): 21, 22, 23, 24, 25
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 21
* spoon.test.method.MethodTest.testGetAllMethods() at distance(s): 21
* spoon.test.ctType.CtTypeTest.testIsSubTypeOf() at distance(s): 22
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 22
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnTypeRef() at distance(s): 22, 23, 24, 25, 26
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldByReflection() at distance(s): 22
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 23
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 23
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 23, 35
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 24, 26, 27, 28, 30, 32, 37, 38
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 24
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 24
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 24
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 25, 26, 27
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 25, 26, 27
* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 25
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 25, 26, 27
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 25, 32, 45, 46
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 25
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 25, 26
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 25, 26, 27
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 25, 26, 27
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 26, 28, 38
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 26, 27, 32
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 26, 27, 32, 65
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 26, 27, 32
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 26, 27, 32, 33
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 26, 27, 32
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 26, 27, 32, 33, 46, 47
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 26, 27, 32
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 26, 27, 32, 33, 46, 47
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 26, 27, 32
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 26, 27, 32, 39, 41
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 26, 27, 32
* spoon.test.query_function.VariableReferencesTest.testPotentialVariableAccessFromStaticMethod() at distance(s): 26
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 27
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 27, 28, 33, 45, 58, 59
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 28
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameLocalVariableToSameName() at distance(s): 28
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 28, 29, 30
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 28, 29, 30
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 29, 30, 31, 32, 45, 46
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 30, 31, 32, 33, 46, 47
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccessInInnerClass() at distance(s): 31
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeReferences() at distance(s): 33, 37, 45
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 34, 36
* spoon.test.prettyprinter.PrinterTest.testChangeAutoImportModeWorks() at distance(s): 35
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.importsFromMultipleTypesSupported() at distance(s): 35
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 35, 36
* spoon.test.compilation.CompilationTest.testExoticClassLoader() at distance(s): 36
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 42, 54
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 42
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 42, 44
* spoon.test.prettyprinter.QualifiedThisRefTest.testPrintCtFieldAccessWorkEvenWhenParentNotInitialized() at distance(s): 43
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 44, 55, 68, 69
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 44, 54
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 44
* spoon.test.prettyprinter.QualifiedThisRefTest.testQualifiedThisRef() at distance(s): 45
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 50, 51, 63, 64
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 53, 54, 55, 56
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 56
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 56
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 57, 59, 61, 63, 69, 70, 75, 76, 77, 78, 80
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 60
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 61
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 62, 64, 68, 70, 72
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 68
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 70, 71
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 71, 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReferenceAutoImport() at distance(s): 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 73
* spoon.test.executable.ExecutableRefTest.testOverridingMethod() at distance(s): 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReferenceAutoImport() at distance(s): 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 73
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 74
* spoon.test.filters.FilterTest.testOverriddenMethodFromAbstractClass() at distance(s): 74
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 74
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 75, 76, 77, 78
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 75, 76, 77, 78
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 75, 76, 77, 78
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 75, 76, 77, 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 76
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 79, 82, 83
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 79
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 79
* spoon.test.imports.ImportTest.testImportWithGenerics() at distance(s): 79
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 82
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 83, 85, 95, 99, 101, 111
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 83, 95
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 84
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 84
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameterWithImports() at distance(s): 84
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 84
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 85
* spoon.test.refactoring.MethodsRefactoringTest.testSubInheritanceHierarchyFunction() at distance(s): 85
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 87
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 87
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 87
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageFullQualified() at distance(s): 87
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 90, 96, 101, 106, 107, 109
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 90, 96, 101, 106, 107, 109
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 90, 96, 101, 106, 107, 109
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 91
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByField() at distance(s): 94
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByLocalVariable() at distance(s): 94
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 97
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameterWithImports() at distance(s): 98
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 98
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 100
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 102
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInLoop() at distance(s): 103
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInTryCatch() at distance(s): 104
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 112
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 121, 122, 123, 124
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 126, 127
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 137


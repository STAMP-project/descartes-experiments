# setShadow(boolean)

**Class:** spoon.support.reflect.declaration.CtConstructorImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/reflect/declaration/CtConstructorImpl.java#L199)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 251 test method(s) with a minimum stack distance of 7.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return null;
```





## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredMethods() at distance(s): 7
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerArrayReference() at distance(s): 7
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 7, 9
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerEnum() at distance(s): 7
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredConstructor() at distance(s): 7
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredField() at distance(s): 7, 9
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerGenericsInClass() at distance(s): 7
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotationWithArrays() at distance(s): 8
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 8, 10
* spoon.test.imports.ImportTest.testEqualsImports() at distance(s): 8, 10
* spoon.test.type.TypeTest.testShadowType() at distance(s): 8, 9
* spoon.test.imports.ImportTest.testGetImportKindReturnRightValue() at distance(s): 8, 22
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 8
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 9, 11, 13, 23
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 9, 11, 13, 15
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 9, 20, 28, 29, 30, 40, 53
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 9
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 9
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 9, 10, 11, 12
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 9, 11
* spoon.test.reference.ExecutableReferenceGenericTest.testReferencesBetweenConstructorsInOtherClass() at distance(s): 10
* spoon.test.reference.TypeReferenceTest.doNotCloseLoader() at distance(s): 10, 24
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionListener() at distance(s): 10, 19, 20, 21
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunction() at distance(s): 10, 19, 20, 21
* spoon.test.enums.EnumsTest.testGetAllMethods() at distance(s): 10
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses() at distance(s): 11, 23
* spoon.test.compilation.CompilationTest.testSingleClassLoader() at distance(s): 11
* spoon.test.lambda.LambdaTest.testGetDeclarationOnTypeParameterFromLambda() at distance(s): 11
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 12, 13, 15, 17, 20, 21, 22, 24, 27
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 12, 13, 15, 17, 20, 21, 23, 25
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 12, 14
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 12, 14
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 13, 15
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 13, 15
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 13, 15
* spoon.test.casts.CastTest.testCast2() at distance(s): 13, 15
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 13, 15, 24, 26, 36
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 13, 15
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 13, 15
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 13, 15
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 13, 15
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 13, 15
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 13, 15
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 13, 15
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 13, 15
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 13, 15
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 13, 15, 55
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 13, 15
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 13, 15
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 13, 15
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 13, 15, 25, 26
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 13, 15
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 13, 15
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 13, 15
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 13, 15
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 13, 15
* spoon.test.casts.CastTest.testCast3() at distance(s): 13, 15
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 13, 15
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 13, 15
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 13, 15
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 13, 15
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 13, 15
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 13, 15
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 13, 15
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 13, 15
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 13, 15
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 13, 15
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 13, 15
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 13, 15
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 13, 15
* spoon.test.casts.CastTest.testCast1() at distance(s): 13, 15
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 13, 15
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 13, 15
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 13, 15
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 13, 15
* spoon.test.parent.ParentContractTest.testContract() at distance(s): 14
* spoon.test.replace.ReplaceParametrizedTest.testContract() at distance(s): 14
* spoon.test.parent.SetParentTest.testContract() at distance(s): 14
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 14, 129
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 14
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 15, 17
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 15, 17, 37
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 15, 17
* spoon.test.jdtimportbuilder.ImportBuilderTest.testSimpleStaticImport() at distance(s): 16
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 16, 44
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 16, 18
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 16, 78, 79
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 16, 18
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 16
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 16, 18, 20
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 16, 18, 20, 28
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 17, 19, 42
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 17, 91, 92
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 17, 81
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 17, 19, 21, 23
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 17, 19, 21, 87
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 17, 91, 92
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 17, 19, 42
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 17, 19, 85
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 17, 19, 85
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 17, 81
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 17, 19, 72
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 17, 19, 21, 26
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 17, 19, 91
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 17, 91, 92
* spoon.test.reference.CloneReferenceTest.testGetDeclarationAfterClone() at distance(s): 18
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 18
* spoon.test.reference.CloneReferenceTest.testGetDeclarationOfFieldAfterClone() at distance(s): 18
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 18, 20, 22, 43
* spoon.test.generics.GenericsTest.testTypeParameterDeclarer() at distance(s): 18
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 19, 21, 27, 28, 29
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionNoClasspath() at distance(s): 19
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 20, 28, 29, 30, 33, 34
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 20, 32, 33, 34, 35, 48, 49
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 20, 21, 36, 38
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 20, 28, 29, 30, 33, 34
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 20
* spoon.generating.RoleHandlersGenerator.process() at distance(s): 20, 22
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 20, 28, 29, 30, 33, 34
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 20, 28, 29, 30, 33, 34
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 20, 28, 29, 30, 33, 34
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 20, 81, 86, 92, 93, 94, 96, 102, 103, 104, 105, 106, 121
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 20, 28, 29, 30, 33, 34
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 22, 34
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 22, 23, 24, 25
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 22, 24, 32, 33, 34, 35
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 22, 24, 34
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 22, 27, 28
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 22, 24, 26, 27
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 23, 24, 25, 26
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 23, 24
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 23, 30, 31, 32
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 23, 24
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 23, 44, 56
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnType() at distance(s): 23, 24, 25, 26, 27
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 23, 30, 31, 32
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 23, 28, 29, 34, 41, 43
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 23
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 23, 29, 30, 35, 47, 60, 61
* spoon.test.method.MethodTest.testGetAllMethods() at distance(s): 23
* spoon.test.ctType.CtTypeTest.testIsSubTypeOf() at distance(s): 24
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 24
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnTypeRef() at distance(s): 24, 25, 26, 27, 28
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldByReflection() at distance(s): 24
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 25
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 25
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 25, 37
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 26, 28, 29, 30, 32, 34, 39, 40
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 26
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 26
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 26
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 27, 28, 29
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 27, 28, 29
* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 27
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 27, 28, 29
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 27, 34, 47, 48
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 27
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 27, 28, 29
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 27, 28, 29
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 28, 30, 40
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 28, 29, 34
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 28, 29, 34, 67
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 28, 29, 34
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 28, 29, 34, 35
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 28, 29, 34
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 28, 29, 34, 35, 48, 49
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 28, 29, 34
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 28, 29, 34, 35, 48, 49
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 28, 29, 34
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 28, 29, 34
* spoon.test.query_function.VariableReferencesTest.testPotentialVariableAccessFromStaticMethod() at distance(s): 28
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 29
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 30
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameLocalVariableToSameName() at distance(s): 30
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 31, 32, 33, 34, 47, 48
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccessInInnerClass() at distance(s): 33
* spoon.test.factory.FactoryTest.testClone() at distance(s): 35
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeReferences() at distance(s): 35, 39, 47
* spoon.test.method.MethodTest.testClone() at distance(s): 35
* spoon.test.prettyprinter.PrinterTest.testChangeAutoImportModeWorks() at distance(s): 37
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 37
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.importsFromMultipleTypesSupported() at distance(s): 37
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 37, 38
* spoon.test.compilation.CompilationTest.testExoticClassLoader() at distance(s): 38
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 44
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 44, 46
* spoon.test.prettyprinter.QualifiedThisRefTest.testPrintCtFieldAccessWorkEvenWhenParentNotInitialized() at distance(s): 45
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 46, 57, 70, 71
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 46, 56
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 46
* spoon.test.prettyprinter.QualifiedThisRefTest.testQualifiedThisRef() at distance(s): 47
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 52, 53, 65, 66
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 55, 56, 57, 58
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 58
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 58
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 59, 61, 63, 65, 71, 72, 77, 78, 79, 80, 82
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 62
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 63
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 64, 66, 70, 72, 74
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 70
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 72, 73
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 73, 75
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReferenceAutoImport() at distance(s): 75
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 75
* spoon.test.executable.ExecutableRefTest.testOverridingMethod() at distance(s): 75
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 75
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReferenceAutoImport() at distance(s): 75
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 75
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 75
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 76
* spoon.test.filters.FilterTest.testOverriddenMethodFromAbstractClass() at distance(s): 76
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 76
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 77, 78, 79, 80
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 77, 78, 79, 80
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 77, 78, 79, 80
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 77, 78, 79, 80
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 78
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 81, 84, 85
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 81
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 81
* spoon.test.imports.ImportTest.testImportWithGenerics() at distance(s): 81
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 84
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 85, 87, 97, 101, 103, 113
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 85, 97
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 86
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 86
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameterWithImports() at distance(s): 86
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 86
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 87
* spoon.test.refactoring.MethodsRefactoringTest.testSubInheritanceHierarchyFunction() at distance(s): 87
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 89
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 89
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 89
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageFullQualified() at distance(s): 89
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 92, 98, 103, 108, 109, 111
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 92, 98, 103, 108, 109, 111
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 92, 98, 103, 108, 109, 111
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 93
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByField() at distance(s): 96
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByLocalVariable() at distance(s): 96
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 99
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameterWithImports() at distance(s): 100
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 100
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 102
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 104
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInLoop() at distance(s): 105
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInTryCatch() at distance(s): 106
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 114
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 123, 124, 125, 126
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 128, 129
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 139


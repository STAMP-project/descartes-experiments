# setShadow(boolean)

**Class:** spoon.support.reflect.declaration.CtParameterImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/reflect/declaration/CtParameterImpl.java#L181)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 260 test method(s) with a minimum stack distance of 9.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return null;
```





## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredMethods() at distance(s): 9, 10
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerArrayReference() at distance(s): 9, 10
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 9, 10, 11, 12
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerEnum() at distance(s): 9
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredConstructor() at distance(s): 9, 10
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredField() at distance(s): 9, 10, 12
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerInterface() at distance(s): 10
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 10, 11, 12, 13
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerGenericsInClass() at distance(s): 10
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 11, 12, 13, 14, 15, 16, 25, 26, 27
* spoon.test.interfaces.InterfaceTest.testDefaultMethodInConsumer() at distance(s): 11
* spoon.test.parent.SetParentTest.testContract() at distance(s): 11, 13
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 11, 12, 13, 14, 15, 16, 17, 18
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 11, 12
* spoon.test.type.TypeTest.testShadowType() at distance(s): 11, 12
* spoon.test.generics.GenericsTest.testIsSameSignatureWithGenerics() at distance(s): 11
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 11, 12, 13, 14
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 11
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 11, 12, 14
* spoon.test.generics.GenericsTest.testWildCardonShadowClass() at distance(s): 12
* spoon.test.secondaryclasses.ClassesTest.testAnonymousClass() at distance(s): 12
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 12
* spoon.test.imports.ImportTest.testEqualsImports() at distance(s): 12
* spoon.test.SpoonTestHelpers.getAllMetamodelMethods(spoon.reflect.declaration.CtType) at distance(s): 12
* spoon.test.enums.EnumsTest.testGetAllMethods() at distance(s): 12, 13
* spoon.test.annotation.AnnotationTest.testAnnotationValueReflection() at distance(s): 12
* spoon.test.reference.ExecutableReferenceGenericTest.testReferencesBetweenConstructorsInOtherClass() at distance(s): 13
* spoon.test.reference.TypeReferenceTest.doNotCloseLoader() at distance(s): 13, 27
* spoon.test.parent.ParentContractTest.testContract() at distance(s): 13
* spoon.test.replace.ReplaceParametrizedTest.testContract() at distance(s): 13
* spoon.test.lambda.LambdaTest.testLambdaMethod() at distance(s): 13
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses() at distance(s): 13, 25
* spoon.test.model.TypeTest.superclassTest() at distance(s): 13
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 30
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 28
* spoon.test.lambda.LambdaTest.testGetDeclarationOnTypeParameterFromLambda() at distance(s): 14
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 14, 15, 16, 17, 27, 28, 29
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 14, 15, 16, 17
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 15, 16, 17, 18
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 15, 16, 17, 18
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 15, 16, 17, 18
* spoon.test.casts.CastTest.testCast2() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 15, 34, 35, 36, 37, 49, 50, 51
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 15, 16, 17, 18, 26, 27, 29, 39, 40
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 15, 16, 17, 18
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 15, 16, 17, 18
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 15, 16, 17, 18
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 15, 16, 17, 18
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 15, 31, 32, 37
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 15, 31, 32, 37, 70
* spoon.generating.CtBiScannerGenerator.process() at distance(s): 15
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 15, 16, 17, 18
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 15, 31, 32, 37
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 15, 16, 17, 18
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 15, 16, 17, 18, 58
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 15, 16, 17, 18
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 15, 16, 17, 18
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 15, 31, 32, 37, 38, 52
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 15, 16, 17, 18, 27, 28, 29, 30
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 15, 25, 35, 36, 37, 38, 50, 51, 52
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 15, 16, 17, 18
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 15, 16, 17, 18
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 15, 33, 34, 35
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 15, 31, 32, 37
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 15, 16, 17, 18
* spoon.test.casts.CastTest.testCast3() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 15, 31, 32, 37, 38, 50, 51, 52
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 15, 16, 17, 18
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 15, 16, 17, 18
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 15, 25, 31, 32, 37
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 15, 31, 32, 37, 38, 50, 51, 52
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 15, 33, 34, 35
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 15, 16, 17, 18
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 15, 16, 17, 18
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 15, 16, 17, 18
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 15, 31, 32, 37
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 15, 25, 31, 32, 37, 43, 44
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 15, 16, 17, 18
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 15, 16, 17, 18
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 15, 31, 32, 37
* spoon.test.casts.CastTest.testCast1() at distance(s): 15, 16, 17, 18
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 15, 16, 17, 18
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 15, 16, 17, 18
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 15, 16, 17, 18
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 15, 16, 17, 18
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 16, 25, 32, 33, 36, 38, 49, 50, 62, 63, 64
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 17, 30, 132
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 17, 18, 19, 20
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 17, 18, 19, 20, 40
* spoon.test.parameters.ParameterTest.testMultiParameterLambdaTypeReference() at distance(s): 17
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 17
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 17, 18, 19, 20
* spoon.test.lambda.LambdaTest.testEqualsLambdaParameterRef() at distance(s): 17
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 18, 19, 20, 21, 34
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 18, 25, 28, 54
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 18, 19, 20, 21
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 18, 19, 20, 21, 22, 23
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 18, 19, 20, 21, 22, 23, 31
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 19, 20, 21, 22, 45
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 19, 20, 94, 95
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 19, 47
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 19, 20, 84
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 19, 81, 82, 83
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 19, 20, 21, 22, 23, 24, 25, 26
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 19, 26, 29
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 19, 20, 21, 22, 23, 24, 90
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 19, 20, 94, 95
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 19, 20, 21, 22, 45
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 19, 20, 21, 22, 88
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 19, 20, 22, 88
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 19, 20, 84
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 19, 20, 22, 75, 76
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 19, 20, 21, 22, 23, 24, 29
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 19, 20, 94
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 19, 87
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 19, 20, 94, 95
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 20, 84
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 20, 21, 22, 23, 24, 25, 46
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 21, 22, 23, 24, 30, 31, 32, 33, 36
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 22, 74, 84, 85, 86, 87, 88, 89, 90, 102
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 22, 23, 31, 32, 33, 34, 35, 36, 37
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 22, 23, 31, 32, 33, 34, 35, 36, 37
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 22, 23, 31, 32, 33, 34, 35, 36, 37
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionNoClasspath() at distance(s): 22
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 22, 23, 31, 32, 33, 34, 35, 36, 37
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 22, 23, 31, 32, 33, 34, 35, 36, 37
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 22, 23, 26, 35, 36, 62, 84, 85, 88, 89, 91, 94, 95, 96, 97, 98, 99, 104, 105, 106, 107, 108, 109, 111, 124
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 22
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 22, 23, 31, 32, 33, 34, 35, 36, 37
* spoon.test.reference.CloneReferenceTest.testGetDeclarationAfterClone() at distance(s): 23, 36
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 23, 36
* spoon.test.reference.CloneReferenceTest.testGetDeclarationOfFieldAfterClone() at distance(s): 23, 36
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionListener() at distance(s): 23
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunction() at distance(s): 23
* spoon.test.generics.GenericsTest.testTypeParameterDeclarer() at distance(s): 23
* spoon.test.lambda.LambdaTest.testBuildExecutableReferenceFromLambda() at distance(s): 24
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 24, 25, 37, 38
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 24, 25, 26, 27, 28, 51, 52, 53
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 24, 131, 132, 133
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 24, 25, 27, 37, 38
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 24, 30, 31, 32
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 24, 49, 59
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 24, 49
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 25, 26, 27, 28, 29, 52, 53, 54
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 25, 38, 39, 40, 41
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 25, 31, 32, 33, 34, 42, 43, 48, 55
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 25, 26, 27, 35, 36, 37, 38
* spoon.test.imports.ImportTest.testGetImportKindReturnRightValue() at distance(s): 25
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 25, 26, 27, 29, 30, 31, 32
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 26, 27, 29
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnType() at distance(s): 26, 29
* spoon.test.lambda.LambdaTest.testGetOverriddenMethodWithFunction() at distance(s): 26
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 26, 27
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldByReflection() at distance(s): 26, 27
* spoon.test.method.MethodTest.testGetAllMethods() at distance(s): 26
* spoon.test.ctType.CtTypeTest.testIsSubTypeOf() at distance(s): 27
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 27
* spoon.generating.RoleHandlersGenerator.process() at distance(s): 27
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnTypeRef() at distance(s): 27, 30
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 27, 28, 29, 30, 31, 32
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 27, 28, 40, 41
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 28
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 28, 29, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 49
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 28
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 29
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 29
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 30, 31, 32, 33
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 30, 31, 32, 33
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 30, 31, 33, 43, 44
* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 30
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 30, 31, 32, 33, 45
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 30, 31, 36, 37, 49, 50, 51
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 30
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 30, 31, 32, 33
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 30, 31, 32, 33
* spoon.test.query_function.VariableReferencesTest.testPotentialVariableAccessFromStaticMethod() at distance(s): 31
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 32
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 33
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameLocalVariableToSameName() at distance(s): 33
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccessInInnerClass() at distance(s): 36
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 39, 40, 41, 42
* spoon.test.prettyprinter.PrinterTest.testChangeAutoImportModeWorks() at distance(s): 40
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.importsFromMultipleTypesSupported() at distance(s): 40
* spoon.test.compilation.CompilationTest.testExoticClassLoader() at distance(s): 41
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 46, 47, 59, 60
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 46, 47, 48, 49
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 47, 67
* spoon.test.prettyprinter.QualifiedThisRefTest.testPrintCtFieldAccessWorkEvenWhenParentNotInitialized() at distance(s): 48
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 49, 59, 60, 72, 73, 74
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeReferences() at distance(s): 50
* spoon.test.prettyprinter.QualifiedThisRefTest.testQualifiedThisRef() at distance(s): 50
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 54, 55, 56, 67, 68, 69
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 56, 61, 62, 63, 64, 65, 66, 67, 73, 74, 75, 76, 79, 80, 81, 82, 83, 84, 85
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 57, 58, 59, 60, 61, 62
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 61
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 61, 99
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 83, 84
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 66
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 73
* spoon.test.reference.VariableAccessTest.testDeclaringTypeOfALambdaReferencedByParameterReference() at distance(s): 74
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 75, 76, 77, 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 76
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReferenceAutoImport() at distance(s): 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 78
* spoon.test.executable.ExecutableRefTest.testOverridingMethod() at distance(s): 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReferenceAutoImport() at distance(s): 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 78
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 79, 80, 81, 82, 83, 84
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 79
* spoon.test.filters.FilterTest.testOverriddenMethodFromAbstractClass() at distance(s): 79
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 79, 80, 81, 82, 83, 84
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 79
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 79, 80, 81, 82, 83, 84
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 79, 80, 81, 82, 83, 84
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 81
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 84
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 84, 86, 87, 88, 89, 90, 99, 100, 101, 103, 104, 105, 106, 116, 117
* spoon.test.imports.ImportTest.testImportWithGenerics() at distance(s): 84
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 87, 88, 90, 100
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 89
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 89
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameterWithImports() at distance(s): 89
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 89, 104
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 90
* spoon.test.refactoring.MethodsRefactoringTest.testSubInheritanceHierarchyFunction() at distance(s): 90
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 92
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 92
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 92
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageFullQualified() at distance(s): 92
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 95, 101, 105, 106, 110, 111, 112, 113, 114
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 95, 101, 105, 106, 110, 111, 112, 113, 114
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 95, 101, 105, 106, 110, 111, 112, 113, 114
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 96
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByField() at distance(s): 99
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByLocalVariable() at distance(s): 99
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 102
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameterWithImports() at distance(s): 103
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 103
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 104, 108
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 105
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 107
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInLoop() at distance(s): 108
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInTryCatch() at distance(s): 109
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 117
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 125, 126, 127, 128, 129, 130
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 142


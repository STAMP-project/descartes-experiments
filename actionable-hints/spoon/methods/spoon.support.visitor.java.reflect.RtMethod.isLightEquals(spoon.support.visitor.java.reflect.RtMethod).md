# isLightEquals(spoon.support.visitor.java.reflect.RtMethod)

**Class:** spoon.support.visitor.java.reflect.RtMethod

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/java/reflect/RtMethod.java#L198)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can not be accessed from other classes. 
It has been covered by 161 test method(s) with a minimum stack distance of 6.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return true;
```

The following transformations were also applied and they were detected by the test suite:

```Java
return false;
```





## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredMethods() at distance(s): 6
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerArrayReference() at distance(s): 6
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 6, 8
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerEnum() at distance(s): 6
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredConstructor() at distance(s): 6
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredField() at distance(s): 6, 8
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerGenericsInClass() at distance(s): 6
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotationWithArrays() at distance(s): 7
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 7, 9
* spoon.test.imports.ImportTest.testEqualsImports() at distance(s): 7
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 8, 10, 12, 22
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 8, 10, 12, 14
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 8
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 8, 9, 10, 11
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 8, 10
* spoon.test.reference.TypeReferenceTest.doNotCloseLoader() at distance(s): 9
* spoon.test.enums.EnumsTest.testGetAllMethods() at distance(s): 9
* spoon.test.lambda.LambdaTest.testGetDeclarationOnTypeParameterFromLambda() at distance(s): 10
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 11, 13
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 11, 13
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 12, 14
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 12, 14
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 12, 14
* spoon.test.casts.CastTest.testCast2() at distance(s): 12, 14
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 12, 14, 23, 25
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 12, 14
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 12, 14
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 12, 14
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 12, 14
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 12, 14
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 12, 14
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 12, 14
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 12, 14
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 12, 14
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 12, 14
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 12, 14
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 12, 14
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 12, 14, 21, 23
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 12, 14
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 12, 14, 24
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 12, 14
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 12, 14
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 12, 14
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 12, 14
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 12, 14, 20, 22
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 12, 14
* spoon.test.casts.CastTest.testCast3() at distance(s): 12, 14
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 12, 14
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 12, 14
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 12, 14
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 12, 14
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 12, 14
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 12, 14
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 12, 14
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 12, 14
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 12, 14
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 12, 14
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 12, 14
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 12, 14
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 12, 14
* spoon.test.casts.CastTest.testCast1() at distance(s): 12, 14
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 12, 14
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 12, 14
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 12, 14
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 12, 14
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 14, 16
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 14, 16
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 14, 16
* spoon.test.jdtimportbuilder.ImportBuilderTest.testSimpleStaticImport() at distance(s): 15
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 15
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 15, 17
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 15, 77
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 15, 17
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 15, 17, 19
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 15, 17, 19
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 16, 18
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 16, 90
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 16
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 16, 18, 20, 22
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 16, 18, 20
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 16, 90
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 16, 18
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 16, 18
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 16, 18
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 16
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 16, 18
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 16, 18, 20
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 16, 18
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 16, 90
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 17, 19, 21
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 18, 20, 26, 27
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 19, 27, 28, 32, 33
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 19, 27, 28, 32, 33
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 19, 27, 28, 32, 33
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 19, 27, 28, 32, 33
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 19, 27, 28, 32, 33
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 19, 85, 91, 92, 93, 95, 101, 102, 103, 104, 105, 120
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 19, 27, 28, 32, 33
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 21
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 21, 22, 23, 24
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 21, 23, 31, 32, 33, 34
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 21, 23
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 21, 23, 25
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 22, 23, 24, 25
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldByReflection() at distance(s): 23
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnType() at distance(s): 24
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 24
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 25, 27, 28, 31, 33, 38, 39
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnTypeRef() at distance(s): 25
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 25
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 26, 27
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 26, 27
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 26, 27
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 26
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 26, 27
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 26, 27
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 27, 29
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 27, 28
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 27, 28, 66
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 27, 28
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 27, 28, 34
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 27, 28
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 27, 28, 34, 47, 48
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 27, 28
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 27, 28
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 27, 28, 34, 47, 48
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 27, 28
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 27, 28, 40, 42
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 27, 28
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 28, 29, 46, 59, 60
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 29, 30
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 29, 30
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 30, 31, 33, 46, 47
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 31, 32, 34, 47, 48
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 33, 46, 47
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 35, 37
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 36
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeReferences() at distance(s): 38
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 43
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 43, 45
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 51, 64, 65
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 54, 55, 56, 57
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 55
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 56, 69, 70
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 57
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 58, 60, 62, 70, 71, 79, 81
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 63, 65, 69, 71, 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 71
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 72, 74
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 76, 77, 78, 79
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 76, 77, 78, 79
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 76, 77, 78, 79
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 76, 77, 78, 79
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 80, 83
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 84, 86, 96, 100, 102
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 84
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 91, 102, 108, 110
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 91, 102, 108, 110
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 91, 102, 108, 110
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 122, 123, 124, 125
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 127


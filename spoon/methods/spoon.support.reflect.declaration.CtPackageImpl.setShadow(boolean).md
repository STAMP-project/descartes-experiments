# setShadow(boolean)

**Class:** spoon.support.reflect.declaration.CtPackageImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/reflect/declaration/CtPackageImpl.java#L269)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 266 test method(s) with a minimum stack distance of 4.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return null;
```





## Observed test methods

* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredMethods() at distance(s): 4, 9, 12, 13, 14
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerArrayReference() at distance(s): 4, 9, 11, 12, 13, 14, 15, 16
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerClass() at distance(s): 4, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerInterface() at distance(s): 4, 9, 11, 12, 14, 16, 18, 20
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerEnum() at distance(s): 4, 11, 12
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredConstructor() at distance(s): 4, 9, 11, 12, 13, 14
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testDeclaredField() at distance(s): 4, 9, 11, 12, 13, 14, 16, 18
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerAnnotation() at distance(s): 4, 6, 11, 13, 14, 15, 17
* spoon.support.visitor.java.JavaReflectionTreeBuilderTest.testScannerGenericsInClass() at distance(s): 4, 9, 11, 13, 14, 16, 18
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 5, 12, 13, 14, 15, 16, 21, 23, 24, 25, 26, 28, 30, 31, 32, 68, 72, 73, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 104, 106, 108
* spoon.test.interfaces.InterfaceTest.testDefaultMethodInConsumer() at distance(s): 5, 12, 15, 17
* spoon.test.api.MetamodelTest.testGetterSetterFroRole() at distance(s): 5, 12, 13, 14, 16, 21, 28, 29, 30, 32, 78, 85, 86, 87, 89
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotationWithArrays() at distance(s): 5, 10
* spoon.test.parent.SetParentTest.testContract() at distance(s): 5, 10, 13, 15, 17, 19, 21
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 5, 10, 12, 13, 14, 15, 17, 18, 19
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 5, 12, 13, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27
* spoon.test.imports.ImportTest.testEqualsImports() at distance(s): 5, 10, 12, 14, 16
* spoon.test.annotation.AnnotationTest.testSpoonManageRecursivelyDefinedAnnotation() at distance(s): 5, 12, 13, 14, 15, 16, 17, 19, 21
* spoon.test.type.TypeTest.testShadowType() at distance(s): 5, 6, 13, 14, 15, 16
* spoon.test.generics.GenericsTest.testIsSameSignatureWithGenerics() at distance(s): 5, 12, 15, 17
* spoon.test.imports.ImportTest.testGetImportKindReturnRightValue() at distance(s): 5, 10, 12, 19, 27, 29
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 5, 13, 15
* spoon.test.generics.GenericsTest.testWildCardonShadowClass() at distance(s): 6, 13, 14, 16, 18, 20
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 6, 8, 10, 11, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34
* spoon.test.parent.ParentContractTest.testContract() at distance(s): 6, 13, 15, 17
* spoon.test.replace.ReplaceParametrizedTest.testContract() at distance(s): 6, 13, 14, 15, 17
* spoon.test.secondaryclasses.ClassesTest.testAnonymousClass() at distance(s): 6, 11, 16
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 6, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 6, 10, 11, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 45, 46, 47, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 6, 11, 16, 18, 20
* spoon.test.annotation.AnnotationTest.testAccessAnnotationValue() at distance(s): 6, 13, 15, 16
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 6, 11, 13, 15, 16
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 6, 7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
* spoon.test.SpoonTestHelpers.getAllMetamodelMethods(spoon.reflect.declaration.CtType) at distance(s): 6, 13, 14, 16, 18
* spoon.test.annotation.AnnotationTest.testAnnotationValueReflection() at distance(s): 6, 11, 14, 16, 18
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 6, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22
* spoon.test.reference.ExecutableReferenceGenericTest.testReferencesBetweenConstructorsInOtherClass() at distance(s): 7, 15, 17
* spoon.test.reference.TypeReferenceTest.doNotCloseLoader() at distance(s): 7, 12, 14, 15, 17, 21, 29, 31
* spoon.test.lambda.LambdaTest.testLambdaMethod() at distance(s): 7, 14, 17, 19
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionListener() at distance(s): 7, 12, 16, 17, 21, 23, 25, 27
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunction() at distance(s): 7, 12, 16, 17, 21, 23, 25, 27
* spoon.test.enums.EnumsTest.testGetAllMethods() at distance(s): 7, 12, 14, 15, 16, 17, 19, 21
* spoon.test.model.TypeTest.superclassTest() at distance(s): 7, 14
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses() at distance(s): 8, 10, 13, 17, 20, 25, 29
* spoon.test.compilation.CompilationTest.testSingleClassLoader() at distance(s): 8, 10, 13
* spoon.test.lambda.LambdaTest.testGetDeclarationOnTypeParameterFromLambda() at distance(s): 8, 13, 15, 16, 18, 20
* spoon.reflect.declaration.CtTypeInformationTest.testClassTypingContextContinueScanning() at distance(s): 8, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35
* spoon.test.reference.TypeReferenceTest.testIsSubTypeSuperClassNull() at distance(s): 8
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 9, 11, 16, 18, 19, 20, 21, 22, 23, 28, 29, 30, 31, 33, 34, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49, 50, 51, 53, 55
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 33, 34, 35, 36, 37, 39, 41, 44, 64, 69, 71, 72, 74
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 33, 34, 35, 36, 37, 39, 41
* spoon.test.trycatch.TryCatchTest.testTryCatchVariableGetType() at distance(s): 9, 10, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 46, 53
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 29, 30, 31, 32, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 50, 51, 52, 54, 56
* spoon.test.template.testclasses.SimpleTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 9, 10, 16, 17, 18, 19, 20, 21, 22, 24, 25, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49, 50, 51, 53, 55
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 9, 16, 19, 20, 21, 27, 28, 29, 32, 33, 35, 36, 37, 38, 39, 43
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 33, 34, 35, 36, 37, 39, 41
* spoon.test.trycatch.TryCatchTest.testExceptionJava7() at distance(s): 9, 10, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 45, 46, 47, 48, 50, 51, 52, 54, 56
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 32, 33, 34, 35, 36, 37, 39, 41
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 45, 46, 47, 48, 50, 51, 52, 54, 56
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 27, 28, 29, 32, 33, 35, 36, 37, 38, 39, 43
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 33, 34, 35, 36, 37, 39, 41, 44
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 33, 34, 35, 36, 37, 38, 39, 41, 43, 44, 45, 47, 48, 49, 50, 51, 53
* spoon.test.template.testclasses.NtonCodeTemplate.apply(spoon.reflect.declaration.CtType) at distance(s): 9, 10, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 29, 31, 32, 33, 34, 35, 36, 38, 42
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 9, 10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 30, 31, 33, 34, 35, 36, 37, 39, 41
* spoon.test.snippets.SnippetTest.testCompileStatementWithReturn() at distance(s): 9, 14, 16, 17, 18, 19, 20, 21, 22
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 39
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 10, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 47, 50, 51, 53
* spoon.test.casts.CastTest.testCast2() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 39
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23, 26, 28, 29, 30, 31, 33, 34, 35, 41, 43
* spoon.test.intercession.IntercessionTest.testInsertIfIntercession() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.serializable.SerializableTest.testSerialCtStatement() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.intercession.RemoveTest.testRemoveAllStatements() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.model.BlockTest.testIterationStatements() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.ctType.CtTypeTest.testHasMethodOnNull() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.strings.StringLiteralTest.testSnippetFullClass() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.snippets.SnippetTest.testSnippetFullClass() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.intercession.IntercessionTest.testEqualConstructor() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23, 52, 60, 62
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 10, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 46, 49, 51
* spoon.test.variable.AccessTest.testAccessToStringOnPostIncrement() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 10, 15, 17, 18, 19, 20, 22, 23, 24, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36
* spoon.test.trycatch.TryCatchTest.testCatchOrder() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.exceptions.ExceptionTest.testExceptionInSnippet() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 10, 17, 18, 19, 20, 21, 22, 43, 50, 51, 53, 54, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 76, 78
* spoon.test.ctType.CtTypeTest.testHasMethodInDirectMethod() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.intercession.IntercessionTest.testInsertBegin() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.casts.CastTest.testCast3() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.trycatch.TryCatchTest.testFullyQualifiedException() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.generics.GenericsTest.testDiamond1() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 10, 17, 18, 19, 20, 21, 22, 43, 50, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90
* spoon.test.snippets.SnippetTest.testCompileSnippetWithContext() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.snippets.SnippetTest.testSnippetWihErrors() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.intercession.IntercessionTest.testInsertEnd() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.type.TypeTest.testTypeAccessOnPrimitive() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.model.BlockTest.testAddEmptyBlock() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.snippets.SnippetTest.testCompileSnippetSeveralTimes() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 10, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 39
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 10, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 43, 50, 51, 53, 58, 63
* spoon.test.casts.CastTest.testCast1() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.model.TypeTest.testGetUsedTypesForTypeInRootPackage() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 10, 11, 17, 18, 19, 20, 21, 22, 23, 26, 27, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 44, 49, 51, 52, 53, 54, 56, 57, 58, 59, 60, 62, 63, 64, 66, 68
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.intercession.IntercessionTest.testInsertAfter() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.ctType.CtTypeTest.testHasMethodNotHasMethod() at distance(s): 10, 15, 17, 18, 19, 20, 21, 22, 23
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 10, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 43, 50, 51, 53
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 39
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 11, 16, 18, 19, 21, 24, 32, 34, 86, 88, 126, 134, 136
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
* spoon.test.parameters.ParameterTest.testMultiParameterLambdaTypeReference() at distance(s): 11, 18, 21, 23
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 11, 19, 21
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
* spoon.test.lambda.LambdaTest.testEqualsLambdaParameterRef() at distance(s): 11, 18, 21, 23
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 12, 17, 19, 20, 21, 22, 23, 24, 25, 26
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 12, 17, 19, 20, 21, 22, 23, 24, 25, 26, 34, 42, 44
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 12, 17, 22, 27
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 12, 17, 19, 20, 21, 22, 23, 24, 25, 26
* spoon.test.jdtimportbuilder.ImportBuilderTest.testSimpleStaticImport() at distance(s): 13, 18, 20
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 13, 18, 21, 23, 25, 41, 49, 51
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithSimpleImport() at distance(s): 13, 20, 24
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 13, 18, 20, 21, 22, 23, 24, 25, 26, 28, 36, 38
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 13, 18, 21, 23, 25, 75, 76, 77, 80, 82, 83, 84, 85, 86, 87, 89
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 13, 20, 21, 23, 25, 28, 30
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 13, 18, 20, 23, 25, 81, 89, 91
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 13, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 13, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 33, 35
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 39, 47, 49
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 88, 89, 93, 95, 96, 97, 98, 99
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 28, 78, 86, 88
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 84, 92, 94
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 88, 89, 93, 95, 96, 97, 98, 99
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 39, 47, 49
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 82, 90, 92
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 82, 90, 92
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 14, 19, 21, 22, 23, 24, 26, 28, 78, 86, 88, 102, 109
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 30, 69, 70, 77, 78, 79, 80, 82, 84
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 33
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 14, 19, 21, 22, 24, 26, 28, 78, 86, 88
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 88, 96, 98
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 14, 19, 21, 22, 23, 24, 25, 26, 27, 28, 88, 89, 93, 95, 96, 97, 98, 99
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 15, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40, 48, 50
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionNoClasspath() at distance(s): 16, 24, 26
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 17, 22, 24, 25, 26, 27, 29, 30, 34, 36, 37, 39, 40, 41, 42, 56, 64, 66, 68, 78, 79, 83, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 123, 125, 126, 128, 130, 132
* spoon.test.lambda.LambdaTest.testBuildExecutableReferenceFromLambda() at distance(s): 18, 23, 28, 31
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 19, 24, 26, 27, 28, 29, 31, 32, 33, 39, 41
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 19, 24, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 19, 21, 24, 26, 27, 28, 29, 31, 32, 33, 39, 41
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 20, 21, 28, 29, 30, 31, 33
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnType() at distance(s): 20, 21, 22, 23, 25, 26, 27, 28, 29, 31, 32, 33
* spoon.test.lambda.LambdaTest.testGetOverriddenMethodWithFunction() at distance(s): 20, 27, 28, 30, 32
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 20, 21, 24, 28, 29, 30, 31, 33
* spoon.test.method.MethodTest.testGetAllMethods() at distance(s): 20, 28, 30
* spoon.test.ctType.CtTypeTest.testIsSubTypeOf() at distance(s): 21, 29, 31
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 21, 29, 31
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnTypeRef() at distance(s): 21, 22, 23, 24, 26, 27, 28, 29, 30, 32, 33, 34
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41
* spoon.test.filters.FilterTest.testAnnotationFilter() at distance(s): 21, 28, 30, 31, 32
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldByReflection() at distance(s): 21, 26
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 22, 30, 32
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 22, 30, 32
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 22, 29, 32, 34, 48, 56, 58, 60
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 22, 27, 29, 30, 31, 32, 34, 35, 36, 42, 44
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 23, 33, 38, 40, 41, 42, 43, 44, 45, 46, 47
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 23, 31, 33
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 23, 31, 33
* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 24, 32, 34
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 24, 32, 34
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 25, 27, 30, 32, 33, 34, 35, 37, 38, 39, 45, 47
* spoon.test.query_function.VariableReferencesTest.testPotentialVariableAccessFromStaticMethod() at distance(s): 25, 33, 35
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 26, 34, 36
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 27, 35, 37
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameLocalVariableToSameName() at distance(s): 27, 35, 37
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccessInInnerClass() at distance(s): 30, 38, 40
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeReferences() at distance(s): 32, 36, 37, 41, 44, 52, 54
* spoon.test.prettyprinter.PrinterTest.testChangeAutoImportModeWorks() at distance(s): 34, 42, 44
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.importsFromMultipleTypesSupported() at distance(s): 34, 42, 44
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 34, 35, 36, 39, 41, 42, 43, 44, 45, 46, 48
* spoon.test.compilation.CompilationTest.testExoticClassLoader() at distance(s): 35, 43, 45
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 37, 44, 49, 50, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 71, 73
* spoon.reflect.ast.AstCheckerTest.testPushToStackChanges() at distance(s): 40, 47, 49, 51
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 41, 46, 48, 49, 50, 51, 53, 54, 55, 61, 63
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 41, 49, 51, 61, 69, 71
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 41, 46, 48, 49, 50, 51, 52, 53, 54, 55
* spoon.test.prettyprinter.QualifiedThisRefTest.testPrintCtFieldAccessWorkEvenWhenParentNotInitialized() at distance(s): 42, 50, 52
* spoon.test.prettyprinter.QualifiedThisRefTest.testQualifiedThisRef() at distance(s): 44, 52, 54
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 55, 60, 62, 65, 67, 69
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 55, 63, 65, 93, 100, 103, 105
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 57, 64, 66, 67, 68, 69
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 59, 61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 60, 68, 70
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 67, 75, 77
* spoon.test.reference.VariableAccessTest.testDeclaringTypeOfALambdaReferencedByParameterReference() at distance(s): 68, 73, 78, 81
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 69, 70, 74, 76, 78, 79, 80, 81
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 70, 75, 77, 78, 79, 80, 81, 82, 84, 86
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReferenceAutoImport() at distance(s): 72, 80, 82
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 72, 80, 82
* spoon.test.executable.ExecutableRefTest.testOverridingMethod() at distance(s): 72, 80, 82
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 72, 80, 82
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReferenceAutoImport() at distance(s): 72, 80, 82
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 72, 80, 82
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 72, 80, 82
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 73, 81, 83
* spoon.test.filters.FilterTest.testOverriddenMethodFromAbstractClass() at distance(s): 73, 81, 83
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 73, 81, 83
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 75, 83, 85
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 78, 86, 88
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 78, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 120, 121, 123, 125
* spoon.test.imports.ImportTest.testImportWithGenerics() at distance(s): 78, 86, 88
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 82, 84, 87, 89, 90, 91, 92, 94, 96, 102, 104
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 83, 91, 93
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 83, 91, 93
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameterWithImports() at distance(s): 83, 91, 93
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 83, 91, 93, 98, 105, 106, 108, 110
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 84, 92, 94
* spoon.test.refactoring.MethodsRefactoringTest.testSubInheritanceHierarchyFunction() at distance(s): 84, 92, 94
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 86, 94, 96
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 86, 94, 96
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 86, 94, 96
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageFullQualified() at distance(s): 86, 94, 96
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 88, 125, 126, 127, 130, 134, 135, 136, 137, 139
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 89, 94, 95, 96, 97, 99, 100, 101, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 89, 94, 95, 96, 97, 99, 100, 101, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 89, 94, 95, 96, 97, 99, 100, 101, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 90, 98, 100
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByField() at distance(s): 93, 101, 103
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByLocalVariable() at distance(s): 93, 101, 103
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 96, 104, 106
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameterWithImports() at distance(s): 97, 105, 107
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 97, 105, 107
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 98, 102, 105, 106, 108, 109, 110, 112, 114
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 99, 100, 107, 109
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 101, 109, 111
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInLoop() at distance(s): 102, 110, 112
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInTryCatch() at distance(s): 103, 111, 113
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 111, 112, 119, 121
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 136, 137, 144, 146


# setSourceOutputDirectory(java.io.File)

**Class:** spoon.support.compiler.jdt.JDTBasedSpoonCompiler

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/compiler/jdt/JDTBasedSpoonCompiler.java#L281)

This method is **pseudo-tested**.


It can be accessed from other classes and it is directly covered by the test suite. 
It has been covered by 755 test method(s).

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 1, 3, 4, 5, 7
* spoon.test.staticFieldAccess.StaticAccessTest.testProcessAndCompile() at distance(s): 1, 3, 5
* spoon.test.lambda.LambdaTest.setUp() at distance(s): 2, 5
* spoon.test.methodreference.MethodReferenceTest.setUp() at distance(s): 2, 5
* spoon.test.pkg.PackageTest.testAnnotationOnPackage() at distance(s): 2, 5
* spoon.test.interfaces.InterfaceTest.setUp() at distance(s): 2, 5
* spoon.test.imports.ImportTest.testNewInnerClassDefinesInItsClassAndSuperClass() at distance(s): 3, 5
* spoon.test.trycatch.TryCatchTest.testMultiTryCatchWithCustomExceptions() at distance(s): 3, 5
* spoon.test.reference.TypeReferenceTest.doNotCloseLoader() at distance(s): 3, 5
* spoon.test.generics.GenericsTest.testAccessToGenerics() at distance(s): 3, 5
* spoon.test.prettyprinter.LinesTest.setup() at distance(s): 3, 5
* spoon.test.reference.TypeReferenceTest.testGetAllExecutablesForInterfaces() at distance(s): 3, 5
* spoon.test.jar.JarTest.testFile() at distance(s): 3, 5
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoringValidationCheck() at distance(s): 3, 5
* spoon.test.compilation.CompilationTest.testCompilationInEmptyDir() at distance(s): 3, 5
* spoon.test.template.TemplateTest.testTemplateWithWrongUsedStringParam() at distance(s): 3, 5
* spoon.test.imports.ImportTest.testMissingImport() at distance(s): 3, 5
* spoon.test.jar.JarTest.testResource() at distance(s): 3, 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.superInvocationWithEnclosingInstance() at distance(s): 3, 5
* spoon.test.template.TemplateTest.testCheckBoundTemplate() at distance(s): 3, 5
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInAClassPackage() at distance(s): 3, 5
* spoon.test.trycatch.TryCatchTest.testCompileMultiTryCatchWithCustomExceptions() at distance(s): 3, 5, 6, 7
* spoon.test.exceptions.ExceptionTest.testExceptionIfNotCompilable() at distance(s): 3, 5
* spoon.test.template.TemplateTest.testTemplateC1() at distance(s): 3, 5
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 3, 5
* spoon.test.reference.TypeReferenceTest.loadReferencedClassFromClasspath() at distance(s): 3, 5
* spoon.test.path.PathTest.setup() at distance(s): 3, 5
* spoon.test.signature.SignatureTest.testBugSignature() at distance(s): 3, 5
* spoon.test.intercession.insertBefore.InsertMethodsTest.setup() at distance(s): 3, 5
* spoon.test.template.TemplateTest.testTemplateInterfaces() at distance(s): 3, 5
* spoon.test.exceptions.ExceptionTest.testExceptionInvalidAPI() at distance(s): 3, 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 3, 5
* spoon.test.reference.ExecutableReferenceGenericTest.setUp() at distance(s): 3, 5
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassAvailableInLibrary() at distance(s): 3, 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.printerCanPrintInvocationWithoutException() at distance(s): 3, 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 3, 5
* spoon.test.replace.ReplaceTest.setup() at distance(s): 3, 5
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 3, 5, 8
* spoon.test.parent.ParentTest.setup() at distance(s): 3, 5
* spoon.test.imports.ImportScannerTest.testMultiCatchImport() at distance(s): 3, 5
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 3, 5
* spoon.test.exceptions.ExceptionTest.testExceptionDuplicateClass() at distance(s): 3, 5
* spoon.test.staticFieldAccess.StaticAccessTest.setUp() at distance(s): 3, 5
* spoon.test.parent.NullParentTest.setup() at distance(s): 3, 5
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 3, 5
* spoon.test.prettyprinter.QualifiedThisRefTest.setup() at distance(s): 3, 5
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 3, 5
* spoon.test.properties.PropertiesTest.testNonExistingDirectory() at distance(s): 3, 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 3, 5
* spoon.test.prettyprinter.PrinterTest.testPrettyPrinter() at distance(s): 3, 5
* spoon.test.parent.TopLevelTypeTest.setup() at distance(s): 3, 5
* spoon.test.imports.ImportTest.testAnotherMissingImport() at distance(s): 3, 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 3, 5
* spoon.test.jar.JarTest.testJar() at distance(s): 3, 5
* spoon.test.intercession.insertBefore.InsertMethodsTest.insertBeforeAndUpdateParent() at distance(s): 3, 5
* spoon.test.pkg.PackageTest.testPackage() at distance(s): 3, 5
* spoon.test.loop.LoopTest.testAnnotationInForLoop() at distance(s): 4, 6
* spoon.test.limits.utils.InternalTest.testStaticFinalFieldInAnonymousClass() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteAStatementInConstructor() at distance(s): 4, 6
* spoon.test.replace.ReplaceTest.testReplaceIntegerReference() at distance(s): 4, 6
* spoon.test.invocations.InvocationTest.testTargetNullForStaticMethod() at distance(s): 4, 6
* spoon.test.processing.ProcessingTest.testInsertEnd() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldInAnonymousClass() at distance(s): 4, 6
* spoon.test.serializable.SerializableTest.testSerialFile() at distance(s): 4, 6
* spoon.test.model.TypeTest.testTypeInfoIsInterface() at distance(s): 4, 6
* spoon.test.constructorcallnewclass.NewClassTest.testMoreThan9NewClass() at distance(s): 4, 6
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 4, 5, 6, 7
* spoon.testing.CtPackageAssertTest.testEqualityBetweenTwoCtPackageWithDifferentTypes() at distance(s): 4, 6
* spoon.testing.CtPackageAssertTest.testEqualityBetweenTwoCtPackage() at distance(s): 4, 6
* spoon.test.model.TypeTest.testGetAllExecutables() at distance(s): 4, 6
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 4, 5, 7
* spoon.test.visibility.VisibilityTest.testMethodeWithNonAccessibleTypeArgument() at distance(s): 4, 6
* spoon.test.filters.FilterTest.setup() at distance(s): 4, 6
* spoon.test.fieldaccesses.FieldAccessTest.testTargetedAccessPosition() at distance(s): 4, 6
* spoon.test.filters.FilterTest.filteredElementsAreOfTheCorrectType() at distance(s): 4, 6
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 4, 5, 7
* spoon.test.prettyprinter.QualifiedThisRefTest.testCloneThisAccess() at distance(s): 4, 6
* spoon.test.parent.ParentTest.testParentOfCtVariableReference() at distance(s): 4, 6
* spoon.test.secondaryclasses.ClassesTest.testClassWithInternalPublicClassOrInterf() at distance(s): 4, 6
* spoon.test.serializable.SerializableTest.testSerializationModelStreamer() at distance(s): 4, 6
* spoon.test.fieldaccesses.FieldAccessTest.testModelBuildingFieldAccesses() at distance(s): 4, 6
* spoon.test.initializers.InitializerTest.testModelBuildingInitializer() at distance(s): 4, 6
* spoon.test.fieldaccesses.FieldAccessTest.testBCUBug20140402() at distance(s): 4, 6
* spoon.test.type.TypeTest.testTypeAccessOfArrayObjectInFullyQualifiedName() at distance(s): 4, 5, 7
* spoon.test.replace.ReplaceTest.testReplaceExecutableReferenceByAnotherOne() at distance(s): 4, 6
* spoon.test.constructorcallnewclass.NewClassTest.testNewClassInEnumeration() at distance(s): 4, 6
* spoon.test.strings.StringTest.testModelBuildingInitializer() at distance(s): 4, 6
* spoon.test.position.PositionTest.testPositionGeneric() at distance(s): 4, 6
* spoon.test.arrays.ArraysTest.testArrayReferences() at distance(s): 4, 6
* spoon.test.position.PositionTest.testPositionInterface() at distance(s): 4, 6
* spoon.test.eval.EvalTest.testStringConcatenation() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testNotTargetedExpression() at distance(s): 4, 6
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 4, 5, 7
* spoon.test.targeted.TargetedExpressionTest.testCastWriteWithGenerics() at distance(s): 4, 6
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.useFullyQualifiedNamesInCtElementImpl_toString() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testInstanceOfMapEntryGeneric() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testGenericWithExtendsInDeclaration() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteAStatementInMethod() at distance(s): 4, 6
* spoon.test.trycatch.TryCatchTest.testTryWithOneResource() at distance(s): 4, 6
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation() at distance(s): 4, 5, 7
* spoon.test.delete.DeleteTest.testDeleteStatementInCase() at distance(s): 4, 6
* spoon.testing.AbstractAssertTest.testTransformationFromCtElementWithProcessor() at distance(s): 4, 6, 7
* spoon.test.generics.GenericsTest.testMethodTypingContext() at distance(s): 4, 6
* spoon.test.ctBodyHolder.CtBodyHolderTest.testConstructor() at distance(s): 4, 6
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoCtElementWithTheSameSignatureButNotTheSameContent() at distance(s): 4, 6, 7
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInvInInnerClass() at distance(s): 4, 6
* spoon.test.trycatch.TryCatchTest.testModelBuildingInitializer() at distance(s): 4, 6
* spoon.test.processing.ProcessingTest.testInsertBegin() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testTypeParameterReference() at distance(s): 4, 6
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 4, 5, 7
* spoon.test.type.TypeTest.testIntersectionTypeReferenceInGenericsAndCasts() at distance(s): 4, 5, 7
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 4, 5, 6, 7
* spoon.test.factory.FieldFactoryTest.testCreateFromSource() at distance(s): 4, 6
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 4, 5, 7
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 4, 5, 7
* spoon.test.reference.VariableAccessTest.testVariableAccessDeclarationInAnonymousClass() at distance(s): 4, 6
* spoon.testing.CtElementAssertTest.testEqualityBetweenACtElementAndAString() at distance(s): 4, 6, 7
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 4, 5, 7
* spoon.test.methodreference.MethodReferenceTest.testCompileMethodReferenceGeneratedBySpoon() at distance(s): 4, 7
* spoon.test.factory.FactoryTest.testClone() at distance(s): 4, 6
* spoon.test.imports.ImportScannerTest.testComputeMinimalImportsInClass() at distance(s): 4, 6
* spoon.reflect.declaration.CtTypeInformationTest.setUp() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testGenericInField() at distance(s): 4, 6
* spoon.test.variable.AccessTest.testCanVisitVariableAccessAndSubClasses() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testDeclarationOfTypeParameterReference() at distance(s): 4, 6
* spoon.LauncherTest.testInitEnvironmentDefault() at distance(s): 4, 5
* spoon.test.targeted.TargetedExpressionTest.testTargetOfFieldAccess() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testClassTypingContext() at distance(s): 4, 6
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithStatement() at distance(s): 4, 6
* spoon.test.type.TypeTest.testTypeReferenceInGenericsAndCasts() at distance(s): 4, 5, 7
* spoon.test.secondaryclasses.ClassesTest.testAnonymousClass() at distance(s): 4, 6
* spoon.test.position.PositionTest.testPositionClass() at distance(s): 4, 6
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoDifferentCtElement() at distance(s): 4, 6, 7
* spoon.test.generics.GenericsTest.testIsGenericsMethod() at distance(s): 4, 6
* spoon.test.fieldaccesses.FieldAccessTest.testTypeDeclaredInAnonymousClass() at distance(s): 4, 5, 7
* spoon.test.factory.ConstructorFactoryTest.testCreate() at distance(s): 4, 6
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessInAnonymousClass() at distance(s): 4, 6
* spoon.test.variable.AccessFullyQualifiedFieldTest.testCheckAssignmentContracts() at distance(s): 4, 6
* spoon.test.position.PositionTest.testPositionMethod() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testDiamond2() at distance(s): 4, 6
* spoon.test.replace.ReplaceTest.testReplaceAParameterReferenceToFieldReference() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteACaseOfASwitch() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testGenericMethodCallWithExtend() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testCtThisAccess() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testModelBuildingGenericConstructor() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testClassTypingContextMethodSignature() at distance(s): 4, 6
* spoon.test.trycatch.TryCatchTest.testTryWithResources() at distance(s): 4, 6
* spoon.test.control.ControlTest.testModelBuildingDoWhile() at distance(s): 4, 6
* spoon.test.factory.AnnotationFactoryTest.testAnnotate() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteMethod() at distance(s): 4, 6
* spoon.test.imports.ImportTest.testFullQualifiedNameImport() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteAStatementInAnonymousExecutable() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteBodyOfAMethod() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfStaticFieldAccess() at distance(s): 4, 6
* spoon.testing.CtPackageAssertTest.testEqualityBetweenTwoDifferentCtPackage() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccess() at distance(s): 4, 6
* spoon.test.position.PositionTest.testPositionAbstractMethod() at distance(s): 4, 6
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 4, 5, 7
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnTypeRef() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testBugComparableComparator() at distance(s): 4, 6
* spoon.test.fieldaccesses.FieldAccessTest.testBUG20160112() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInvInAnonymousClass() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteChainOfAssignment() at distance(s): 4, 6
* spoon.test.position.PositionTest.testPositionAnnotation() at distance(s): 4, 6
* spoon.test.varargs.VarArgsTest.testModelBuildingInitializer() at distance(s): 4, 6
* spoon.test.model.TypeTest.testGetUsedTypes() at distance(s): 4, 6
* spoon.test.replace.ReplaceTest.testReplaceAllTypeRefenceWithGenerics() at distance(s): 4, 6
* spoon.test.reference.VariableAccessTest.testSuperAccess() at distance(s): 4, 6
* spoon.test.method.MethodTest.testClone() at distance(s): 4, 6
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldOnType() at distance(s): 4, 6
* spoon.test.ctBodyHolder.CtBodyHolderTest.testWhileWithBlock() at distance(s): 4, 6
* spoon.test.refactoring.MethodsRefactoringTest.testSubInheritanceHierarchyFunction() at distance(s): 4, 6
* spoon.test.model.SwitchCaseTest.testSwitchStatementOnAString() at distance(s): 4, 6
* spoon.test.casts.CastTest.testCase4() at distance(s): 4, 6
* spoon.test.model.AnonymousExecutableTest.testStatements() at distance(s): 4, 6
* spoon.test.constructorcallnewclass.NewClassTest.setUp() at distance(s): 4, 6
* spoon.test.limits.utils.InternalTest.testInternalClasses() at distance(s): 4, 6
* spoon.test.refactoring.MethodsRefactoringTest.testAllMethodsSameSignatureFunction() at distance(s): 4, 6
* spoon.test.filters.FilterTest.intersectionOfTwoFilters() at distance(s): 4, 6
* spoon.test.parent.ParentTest.testParentOfPrimitiveReference() at distance(s): 4, 6
* spoon.test.eval.EvalTest.testDoNotSimplify() at distance(s): 4, 6
* spoon.test.parent.ParentTest.testParentOfGenericInTypeReference() at distance(s): 4, 6
* spoon.test.variable.AccessTest.testCanVisitFieldAccessAndSubClasses() at distance(s): 4, 6
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 4, 5, 6, 7
* spoon.test.secondaryclasses.ClassesTest.testTopLevel() at distance(s): 4, 6
* spoon.test.secondaryclasses.ClassesTest.testInnerClassContruction() at distance(s): 4, 6
* spoon.LauncherTest.testInitEnvironment() at distance(s): 4, 5
* spoon.test.pkg.PackageTest.testPrintPackageInfoWhenNothingInPackage() at distance(s): 4, 5, 6
* spoon.test.position.PositionTest.testPositionField() at distance(s): 4, 6
* spoon.test.filters.FilterTest.unionOfTwoFilters() at distance(s): 4, 6
* spoon.test.enums.EnumsTest.testEnumWithoutField() at distance(s): 4, 6
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoCtElement() at distance(s): 4, 6, 7
* spoon.test.enums.EnumsTest.testModelBuildingEnum() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteAClassTopLevel() at distance(s): 4, 6
* spoon.test.refactoring.MethodsRefactoringTest.testExecutableReferenceFilter() at distance(s): 4, 6
* spoon.test.reflect.visitor.ReferenceQueryTest.getAllTypeReferencesInEnum() at distance(s): 4, 6
* spoon.test.ctBodyHolder.CtBodyHolderTest.testForWithBlock() at distance(s): 4, 6
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessInLambda() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteAStatementInStaticAnonymousExecutable() at distance(s): 4, 6
* spoon.test.type.TypeTest.testTypeAccessForDotClass() at distance(s): 4, 5, 7
* spoon.test.initializers.InitializerTest.testModelBuildingStaticInitializer() at distance(s): 4, 6
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 4, 5, 7
* spoon.test.delete.DeleteTest.testDeleteConditionInACondition() at distance(s): 4, 6
* spoon.test.ctBodyHolder.CtBodyHolderTest.testMethod() at distance(s): 4, 6
* spoon.test.executable.ExecutableRefTest.testGetActualClassTest() at distance(s): 4, 6
* spoon.test.secondaryclasses.ClassesTest.testIsAnonymousMethodInCtClass() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteReturn() at distance(s): 4, 6
* spoon.test.control.ControlTest.testModelBuildingFor() at distance(s): 4, 6
* spoon.test.factory.FieldFactoryTest.testCreate() at distance(s): 4, 6
* spoon.test.variable.AccessTest.testCanVisitArrayAccessAndSubClasses() at distance(s): 4, 6
* spoon.test.filters.FilterTest.testFieldAccessFilter() at distance(s): 4, 6
* spoon.test.trycatch.TryCatchTest.testRethrowingExceptionsJava7() at distance(s): 4, 6
* spoon.test.imports.ImportScannerTest.testComputeImportsInClass() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testTypeParameterDeclarer() at distance(s): 4, 6
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 4, 7
* spoon.test.generics.GenericsTest.testModelBuildingTree() at distance(s): 4, 6
* spoon.test.reference.TypeReferenceTest.testInvocationWithFieldAccessInNoClasspath() at distance(s): 4, 5, 7
* spoon.test.executable.ExecutableRefTest.testSameTypeInConstructorCallBetweenItsObjectAndItsExecutable() at distance(s): 4, 5, 7
* spoon.test.filters.FilterTest.classCastExceptionIsNotThrown() at distance(s): 4, 6
* spoon.test.eval.EvalTest.testArrayLength() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfInv() at distance(s): 4, 6
* spoon.test.ctElement.MetadataTest.testMetadata() at distance(s): 4, 6
* spoon.test.ctClass.CtClassTest.getConstructor() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testGenericTypeReference() at distance(s): 4, 6
* spoon.test.factory.FactoryTest.testFactoryOverriding() at distance(s): 4, 6, 7
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testisGeneric() at distance(s): 4, 6
* spoon.test.reference.AnnotationFieldReferenceTest.testAnnotationFieldReference() at distance(s): 4, 6
* spoon.test.model.TypeTest.testGetDeclaredOrIheritedFieldByReflection() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testStaticTargetsOfInv() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testCtSuperAccess() at distance(s): 4, 6
* spoon.test.ctBodyHolder.CtBodyHolderTest.testTryCatch() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testBugCommonCollection() at distance(s): 4, 6
* spoon.test.position.PositionTest.testPositionStatement() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteAnnotationOnAClass() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testMethodTypingContextAdaptMethod() at distance(s): 4, 6
* spoon.test.parent.ParentTest.testParentOfCtExecutableReference() at distance(s): 4, 6
* spoon.test.enums.EnumsTest.testGetAllMethods() at distance(s): 4, 6
* spoon.test.query_function.VariableReferencesTest.testPotentialVariableAccessFromStaticMethod() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testModelBuildingSimilarSignatureMethods() at distance(s): 4, 6
* spoon.test.delete.DeleteTest.testDeleteParameterOfMethod() at distance(s): 4, 6
* spoon.test.targeted.TargetedExpressionTest.testTargetsOfFieldAccessInInnerClass() at distance(s): 4, 6
* spoon.test.loop.LoopTest.testForeachShouldHaveAlwaysABlockInItsBody() at distance(s): 4, 6
* spoon.test.model.TypeTest.superclassTest() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testCtTypeReference_getSuperclass() at distance(s): 4, 6
* spoon.test.generics.GenericsTest.testTypeParameterReferenceAsActualTypeArgument() at distance(s): 4, 6
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 4, 5, 6, 7
* spoon.test.compilation.CompilationTest.testURLClassLoader() at distance(s): 5
* spoon.test.comment.CommentTest.testJavaDocCommentOnMac() at distance(s): 5
* spoon.test.jdtimportbuilder.ImportBuilderTest.testSimpleStaticImport() at distance(s): 5
* spoon.test.visibility.VisibilityTest.testFullyQualifiedNameOfTypeReferenceWithGeneric() at distance(s): 5, 8
* spoon.test.lambda.LambdaTest.testBuildExecutableReferenceFromLambda() at distance(s): 5, 7
* spoon.test.generics.GenericsTest.testGenericsInQualifiedNameInConstructorCall() at distance(s): 5, 6
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfAbstractClass() at distance(s): 5
* spoon.test.compilation.CompilationTest.testExoticClassLoader() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testCorrectEnumParent() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testAnnotationOnMethodWithPrimitiveReturnTypeInNoClasspath() at distance(s): 5
* spoon.test.generics.GenericsTest.testIsSameSignatureWithReferencedGenerics() at distance(s): 5
* spoon.test.comparison.EqualTest.testEqualsMultitype() at distance(s): 5
* spoon.test.reference.CloneReferenceTest.testGetDeclarationAfterClone() at distance(s): 5
* spoon.test.generics.GenericsTest.testWildCardonShadowClass() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testPersistenceProperty() at distance(s): 5
* spoon.test.reference.VariableAccessTest.testDeclarationOfVariableReference() at distance(s): 5
* spoon.test.template.TemplateArrayAccessTest.testArrayAccess() at distance(s): 5
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameterWithImports() at distance(s): 5
* spoon.test.constructorcallnewclass.ConstructorCallTest.testCoreConstructorCall() at distance(s): 5
* spoon.test.comparison.EqualTest.testEqualsComment() at distance(s): 5
* spoon.test.imports.ImportScannerTest.testComputeImportsInClassWithSameName() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnParameterInMethod() at distance(s): 5
* spoon.test.ctElement.ElementTest.testGetFactory() at distance(s): 5
* spoon.test.compilation.CompilationTest.testNewInstance() at distance(s): 5
* spoon.test.api.NoClasspathTest.testIssue1747() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnLocalVariableInMethod() at distance(s): 5
* spoon.test.api.NoClasspathTest.testBug20141021() at distance(s): 5
* spoon.test.prettyprinter.PrinterTest.testChangeAutoImportModeWorks() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testSpoonSpoonResult() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testStaticClasses() at distance(s): 5
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotationParameterTypes() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.statelessFactory() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInNewInstance() at distance(s): 5
* spoon.test.generics.GenericsTest.testInvocationGenerics() at distance(s): 5, 6, 8
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByStatement() at distance(s): 5
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessWithoutAnyImport() at distance(s): 5
* spoon.test.imports.ImportTest.testShouldNotCreateAutoreference() at distance(s): 5, 8
* spoon.test.module.TestModule.testGetParentOfRootPackageOfModule() at distance(s): 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 5
* spoon.support.compiler.jdt.JDTBatchCompilerTest.testCompileGeneratedJavaFile() at distance(s): 5
* spoon.test.factory.FactoryTest.testIncrementalModel() at distance(s): 5
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testInnerAnnotationsWithArray() at distance(s): 5
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 5
* spoon.test.annotation.AnnotationLoopTest.testAnnotationDeclaredInForInit() at distance(s): 5, 7
* spoon.test.api.APITest.testInvalidateCacheOfCompiler() at distance(s): 5
* spoon.test.ctBlock.TestCtBlock.testAddStatementInCase() at distance(s): 5
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 5
* spoon.test.generics.GenericsTest.testIsGenericTypeEqual() at distance(s): 5
* spoon.test.filters.FilterTest.testSubInheritanceHierarchyResolver() at distance(s): 5
* spoon.test.position.PositionTest.defaultConstructorPositionTest() at distance(s): 5, 7
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_if() at distance(s): 5
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 5
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 5, 8
* spoon.test.visibility.VisibilityTest.testName() at distance(s): 5, 6
* spoon.test.modifiers.TestModifiers.testMethodWithVarargsDoesNotBecomeTransient() at distance(s): 5
* spoon.test.compilationunit.TestCompilationUnit.testIsoEncodingIsSupported() at distance(s): 5
* spoon.test.refactoring.RefactoringTest.testTransformedInstanceofAfterATransformation() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testPackageInNoClasspath() at distance(s): 5
* spoon.test.compilation.CompilationTest.compileTest() at distance(s): 5
* spoon.test.filters.FilterTest.testElementMapFunction() at distance(s): 5
* spoon.reflect.ast.AstCheckerTest.testPushToStackChanges() at distance(s): 5
* spoon.test.variable.AccessTest.testVariableAccessInNoClasspath() at distance(s): 5
* spoon.test.filters.CUFilterTest.testSingleExcludeWithoutFilter() at distance(s): 5
* spoon.test.reflect.meta.MetaModelTest.elementAnnotationAdaptedRoleTest() at distance(s): 5
* spoon.test.module.TestModule.testDirectiveOrders() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.noTreeSetInSpoon() at distance(s): 5
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 5
* spoon.test.api.APITest.testPrintNotAllSourcesWithFilter() at distance(s): 5
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 5
* spoon.test.generics.GenericsTest.testConstructorCallGenerics() at distance(s): 5, 6, 8
* spoon.test.casts.CastTest.testTypeAnnotationOnCast() at distance(s): 5, 7
* spoon.test.pkg.PackageTest.testGetFQNInNoClassPath() at distance(s): 5
* spoon.test.filters.FilterTest.testOverriddenMethodFromSubClassOfInterface() at distance(s): 5
* spoon.test.labels.TestLabels.testLabelsAreDetected() at distance(s): 5
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 5
* spoon.test.ctType.CtTypeTest.testIsSubTypeOf() at distance(s): 5, 7
* spoon.test.reference.VariableAccessTest.testReferences() at distance(s): 5, 7
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithSimpleImport() at distance(s): 5
* spoon.test.reference.VariableAccessTest.testDeclaringTypeOfALambdaReferencedByParameterReference() at distance(s): 5
* spoon.test.filters.FilterTest.testQueryInQuery() at distance(s): 5
* spoon.test.template.TemplateTest.testTemplateInvocationSubstitution() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testRepeatableAnnotationAreManaged() at distance(s): 5
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInStatements() at distance(s): 5
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses() at distance(s): 5
* spoon.test.compilationunit.GetBinaryFilesTest.testExistingButNotBuiltBinary() at distance(s): 5
* spoon.test.filters.FilterTest.testInvalidQueryStepFailurePolicyIgnore() at distance(s): 5
* spoon.test.reference.ElasticsearchStackoverflowTest.testStackOverflow() at distance(s): 5
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 5, 8
* spoon.test.reference.TypeReferenceTest.testTypeReferenceWithGenerics() at distance(s): 5
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 5, 8
* spoon.test.literal.LiteralTest.testFactoryLiternal() at distance(s): 5
* spoon.test.targeted.TargetedExpressionTest.testStaticTargetsOfInvNoClasspath() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testModelBuildingAnnotationBoundUsage() at distance(s): 5
* spoon.test.variable.AccessTest.testFieldWriteDeclaredInTheSuperclass() at distance(s): 5, 6
* spoon.test.parameters.ParameterTest.testGetParameterReferenceInLambdaNoClasspath() at distance(s): 5
* spoon.test.filters.FilterTest.testOverriddenMethodFromAbstractClass() at distance(s): 5
* spoon.test.filters.FilterTest.testReuseOfBaseQuery() at distance(s): 5
* spoon.test.template.TemplateTest.testSimpleTemplate() at distance(s): 5
* spoon.test.ctType.CtTypeTest.testHasMethodInSuperClass() at distance(s): 5
* spoon.test.ctBlock.TestCtBlock.testAddStatementInBlock() at distance(s): 5
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorClass() at distance(s): 5, 6, 8
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationBeforeExceptionInSignatureOfMethod() at distance(s): 5
* spoon.test.logging.LogTest.testAllLevelsForLogs() at distance(s): 5
* spoon.test.exceptions.ExceptionTest.testUnionCatchExceptionInsideLambdaInNoClasspath() at distance(s): 5
* spoon.test.visitor.VisitorTest.testRecursiveDescent() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnConstructor() at distance(s): 5
* spoon.test.type.TypeTest.test() at distance(s): 5
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber() at distance(s): 5, 7
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testSpecPackage() at distance(s): 5
* spoon.test.methodreference.MethodReferenceTest.testGetGenericExecutableReference() at distance(s): 5, 7
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticStarredImportFromInterface() at distance(s): 5
* spoon.test.api.MetamodelTest.testGetterSetterFroRole() at distance(s): 5
* spoon.test.parameters.ParameterTest.testParameterInNoClasspath() at distance(s): 5
* spoon.test.compilation.CompilationTest.testClassLoader() at distance(s): 5
* spoon.reflect.declaration.UnknownDeclarationTest.testUnknownCalls() at distance(s): 5
* spoon.test.signature.SignatureTest.testNullSignature() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotationNotRepeatableNotArrayAnnotation() at distance(s): 5
* spoon.test.imports.ImportTest.testStaticImportForInvocationInNoClasspath() at distance(s): 5, 6
* spoon.test.filters.FilterTest.testOverridingMethodFromAbstractClass() at distance(s): 5
* spoon.test.comparison.EqualTest.testEqualsActualTypeRef() at distance(s): 5
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorName() at distance(s): 5, 6, 8
* spoon.test.filters.CUFilterTest.testSingleExcludeWithFilter() at distance(s): 5
* spoon.test.type.TypeTest.testTypeAccessForTypeAccessInInstanceOf() at distance(s): 5
* spoon.test.compilation.CompilationTest.testSingleClassLoader() at distance(s): 5
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 5
* spoon.test.factory.FactoryTest.testClassAccessCreatedFromFactories() at distance(s): 5, 7
* spoon.test.filters.FilterTest.testCtScannerListener() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInClassDeclaration() at distance(s): 5
* spoon.test.condition.ConditionalTest.testBlockInConditionAndLoop() at distance(s): 5, 7
* spoon.test.exceptions.ExceptionTest.testExceptionNoFile() at distance(s): 5
* spoon.test.reference.ExecutableReferenceTest.testSpecifyGetAllExecutablesMethod() at distance(s): 5
* spoon.test.snippets.SnippetTest.testIssue981() at distance(s): 5
* spoon.test.template.TemplateClassAccessTest.testClassAccessTest() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testGetAnnotationOuter() at distance(s): 5
* spoon.test.literal.LiteralTest.testLiteralInForEachWithNoClasspath() at distance(s): 5
* spoon.test.compilationunit.GetBinaryFilesTest.testMultiClassInSingleFile() at distance(s): 5
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 5, 6, 8
* spoon.test.reference.VariableAccessTest.testReferenceToLocalVariableDeclaredInLoop() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotationWithArrays() at distance(s): 5
* spoon.test.modifiers.TestModifiers.testCtModifiableAddRemoveReturnCtModifiable() at distance(s): 5
* spoon.test.annotation.AnnotationValuesTest.testValuesOnJava7Annotation() at distance(s): 5, 7
* spoon.test.reference.VariableAccessTest.testReferencesInInitExpression() at distance(s): 5, 7
* spoon.test.interfaces.TestInterfaceWithoutSetup.testModifierFromInterfaceFieldAndMethod() at distance(s): 5
* spoon.test.api.APITest.testOutputOfSpoon() at distance(s): 5
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testGetAnnotationFromParameter() at distance(s): 5
* spoon.test.comment.CommentTest.testCommentsInResourcesWithWindowsEOL() at distance(s): 5, 6
* spoon.test.filters.FilterTest.testFilterChildrenWithoutFilterQueryStep() at distance(s): 5
* spoon.test.filters.FilterTest.testQueryStepScannWithConsumer() at distance(s): 5
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessNoClasspath() at distance(s): 5
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 5, 8
* spoon.test.executable.ExecutableRefTest.methodTest() at distance(s): 5, 7
* spoon.test.generics.GenericsTest.testGenericsInConstructorCall() at distance(s): 5, 7
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 5, 8
* spoon.reflect.visitor.CtVisitorTest.testMethodsInVisitor() at distance(s): 5
* spoon.test.parent.ParentTest.testParentOfCtPackageReference() at distance(s): 5
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameLocalVariableToSameName() at distance(s): 5, 7
* spoon.test.lambda.LambdaTest.testTypeAccessInLambdaNoClassPath() at distance(s): 5
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 5
* spoon.test.filters.FilterTest.testEarlyTerminatingQuery() at distance(s): 5
* spoon.test.generics.GenericsTest.testDiamondComplexGenericsRxJava() at distance(s): 5, 8
* spoon.test.reference.TypeReferenceTest.testTypeReferenceSpecifiedInClassDeclarationInNoClasspathWithGenerics() at distance(s): 5
* spoon.test.ctType.CtTypeParameterTest.testTypeSame() at distance(s): 5, 7
* spoon.test.template.TemplateTest.createTypeFromTemplate() at distance(s): 5
* spoon.test.variable.AccessFullyQualifiedFieldTest.testPrivateStaticImportShouldNotBeImportedInSameClass() at distance(s): 5, 6, 8
* spoon.test.annotation.AnnotationTest.testCreateRepeatableAnnotation() at distance(s): 5
* spoon.LauncherTest.testLauncherInEmptyWorkingDir() at distance(s): 5
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByField() at distance(s): 5, 6, 8
* spoon.test.template.TemplateTest.testSubstituteInnerClass() at distance(s): 5
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithSimpleImportNoAutoimport() at distance(s): 5
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocation() at distance(s): 5
* spoon.test.reference.CloneReferenceTest.testGetDeclarationOfFieldAfterClone() at distance(s): 5
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeReferences() at distance(s): 5
* spoon.test.filters.FilterTest.testElementMapFunctionOtherContracts() at distance(s): 5
* spoon.test.sourcePosition.SourcePositionTest.equalPositionsHaveSameHashcode() at distance(s): 5, 7
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameterWithImports() at distance(s): 5
* spoon.test.position.PositionTest.testSourcePosition() at distance(s): 5
* spoon.test.prettyprinter.PrinterTest.testPrintingOfOrphanFieldReference() at distance(s): 5, 7
* spoon.test.imports.ImportScannerTest.testTargetTypeNull() at distance(s): 5
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitution() at distance(s): 5
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 5, 6, 8
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnPackage() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotationTypeAndFieldOnField() at distance(s): 5
* spoon.test.processing.ProcessingTest.testInitPropertiesWithWrongType() at distance(s): 5
* spoon.test.api.APITest.testAddProcessorMethodInSpoonAPI() at distance(s): 5
* spoon.test.intercession.IntercessionContractTest.data() at distance(s): 5
* spoon.test.targeted.TargetedExpressionTest.testClassDeclaredInALambda() at distance(s): 5, 7
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 5
* spoon.test.filters.FilterTest.testOverriddenMethodsFromSubClassOfAbstractClass() at distance(s): 5
* spoon.test.pkg.PackageTest.testRenamePackageAndPrettyPrintNoclasspath() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotationWithDefaultArrayValue() at distance(s): 5
* spoon.test.replace.ReplaceTest.testReplaceBlockTry() at distance(s): 5, 7
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 5
* spoon.test.signature.SignatureTest.testArgumentNotNullForExecutableReference() at distance(s): 5
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 5
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeParameters() at distance(s): 5, 7
* spoon.test.modifiers.TestModifiers.testSetVisibility() at distance(s): 5
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 5, 8
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameter() at distance(s): 5
* spoon.test.filters.FilterTest.testInvalidQueryStep() at distance(s): 5
* spoon.test.filters.FilterTest.testElementMapFunctionNull() at distance(s): 5
* spoon.test.template.TemplateTest.substituteStringLiteral() at distance(s): 5
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 5
* spoon.processing.ProcessingTest.testSpoonTagger() at distance(s): 5
* spoon.test.type.TypeTest.testPolyTypBindingInTernaryExpression() at distance(s): 5
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 5
* spoon.test.reference.VariableAccessTest.testDeclarationArray() at distance(s): 5, 7
* spoon.test.api.NoClasspathTest.testGetStaticDependency() at distance(s): 5
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 5, 8
* spoon.test.annotation.AnnotationTest.annotationOverrideFQNIsOK() at distance(s): 5
* spoon.test.executable.ExecutableTest.testInfoInsideAnonymousExecutable() at distance(s): 5
* spoon.test.reflect.meta.MetaModelTest.elementAnnotationRoleTest() at distance(s): 5
* spoon.test.processing.ProcessingTest.testProcessorWithNoArgumentsInConstructor() at distance(s): 5
* spoon.test.signature.SignatureTest.testNullSignatureInUnboundVariable() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 5
* spoon.test.fieldaccesses.FieldAccessTest.testIncrementationOnAVarIsAUnaryOperator() at distance(s): 5, 7
* spoon.test.enums.EnumsTest.testAnnotationsOnEnum() at distance(s): 5, 6
* spoon.test.pkg.PackageTest.testRenameRootPackage() at distance(s): 5
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 5, 6
* spoon.test.prettyprinter.PrinterTest.testFQNModeWriteFQNConstructorInCtVisitor() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessor() at distance(s): 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 5
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 5, 8
* spoon.test.generics.GenericsTest.testNewClassGenerics() at distance(s): 5, 6, 8
* spoon.test.constructorcallnewclass.ConstructorCallTest.setUp() at distance(s): 5
* spoon.test.generics.GenericsTest.testGenericsOnLocalType() at distance(s): 5, 7
* spoon.test.api.NoClasspathTest.test() at distance(s): 5
* spoon.test.type.TypeTest.testIntersectionTypeOnTopLevelType() at distance(s): 5, 7
* spoon.test.filters.FilterTest.testFunctionQueryStep() at distance(s): 5
* spoon.test.compilation.CompilationTest.compileCommandLineTest() at distance(s): 5, 6
* spoon.test.invocations.InvocationTest.testTypeOfStaticInvocation() at distance(s): 5, 6
* spoon.test.compilationunit.TestCompilationUnit.testGetUnitTypeWorksWithDeclaredType() at distance(s): 5
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 5
* spoon.test.filters.FilterTest.testOverridingMethodFromInterface() at distance(s): 5
* spoon.test.factory.TypeFactoryTest.testCreateTypeRef() at distance(s): 5
* spoon.test.filters.FilterTest.testFilterQueryStep() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnMethod() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnClass() at distance(s): 5
* spoon.processing.ProcessingTest.testInterruptAProcessor() at distance(s): 5
* spoon.test.generics.GenericsTest.testRecursiveTypeAdapting() at distance(s): 5, 7
* spoon.test.generics.GenericsTest.testName() at distance(s): 5, 6
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameter() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 5
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 5
* spoon.test.arrays.ArraysTest.testCtNewArrayWitComments() at distance(s): 5
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 5
* spoon.test.methodreference.MethodReferenceTest.testReferenceBuilderWithComplexGenerics() at distance(s): 5, 7
* spoon.test.imports.ImportTest.testEqualsImports() at distance(s): 5
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 5
* spoon.test.generics.GenericsTest.testGetDeclarationOfTypeParameterReference() at distance(s): 5
* spoon.test.ctCase.SwitchCaseTest.insertAfterStatementInSwitchCaseWithoutException() at distance(s): 5, 7
* spoon.test.filters.FilterTest.testParentFunction() at distance(s): 5
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 5, 8
* spoon.test.executable.ExecutableRefTest.testOverridingMethod() at distance(s): 5, 7
* spoon.test.annotation.AnnotationTest.testModelBuildingAnnotationBound() at distance(s): 5
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testSpoonManageRecursivelyDefinedAnnotation() at distance(s): 5
* spoon.test.module.TestModule.testCompleteModuleInfoContentNoClasspath() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfParametersInTypeAnnotation() at distance(s): 5
* spoon.test.api.APITest.testDestinationOfSpoon() at distance(s): 5
* spoon.test.arrays.ArraysTest.testCtNewArrayInnerCtNewArray() at distance(s): 5
* spoon.testing.FileAssertTest.testEqualsBetweenTwoSameFile() at distance(s): 5, 6, 8
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInTryCatch() at distance(s): 5, 6, 8
* spoon.test.annotation.AnnotationTest.testDefaultValueInAnnotationsForAnnotationFields() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 5
* spoon.test.pkg.PackageTest.testRenamePackageAndPrettyPrintWithProcessor() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInReturnTypeInMethod() at distance(s): 5
* spoon.test.reflect.meta.MetaModelTest.elementAnnotationRoleHandlerTest() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotationIntrospection() at distance(s): 5
* spoon.test.field.FieldTest.testFieldImplicitTarget() at distance(s): 5, 7
* spoon.test.template.TemplateTest.substituteSubString() at distance(s): 5
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessorWithGlobalAnnotation() at distance(s): 5
* spoon.test.filters.FilterTest.testLineFilter() at distance(s): 5, 7
* spoon.test.api.APITest.testBasicAPIUsage() at distance(s): 5
* spoon.test.condition.ConditionalTest.testConditionalWithAssignment() at distance(s): 5, 7
* spoon.test.pkg.PackageTest.testRenameRootPackageWithNullOrEmpty() at distance(s): 5
* spoon.test.generics.GenericsTest.testMethodsWithGenericsWhoExtendsObject() at distance(s): 5, 6
* spoon.test.visibility.VisibilityTest.testInvocationVisibilityInFieldDeclaration() at distance(s): 5
* spoon.test.compilationunit.TestCompilationUnit.testCompilationUnitDeclaredTypes() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnField() at distance(s): 5
* spoon.test.template.TemplateTest.testTemplateArrayAccess() at distance(s): 5
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRefactorWrongUsage() at distance(s): 5, 7
* spoon.test.filters.FilterTest.testOverridingMethodFromSubClassOfInterface() at distance(s): 5
* spoon.test.support.ResourceTest.testFilteringFolder() at distance(s): 5
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionNoClasspath() at distance(s): 5
* spoon.test.filters.FilterTest.testElementMapConsumableFunction() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAccessAnnotationValue() at distance(s): 5
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 5
* spoon.test.filters.FilterTest.testQueryBuilderWithFilterChain() at distance(s): 5
* spoon.LauncherTest.testLLauncherBuildModelReturnAModel() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testTypeReferenceSpecifiedInClassDeclarationInNoClasspath() at distance(s): 5
* spoon.test.filters.CUFilterTest.testWithoutFilters() at distance(s): 5
* spoon.test.invocations.InvocationTest.testIssue1753() at distance(s): 5
* spoon.test.template.TemplateTest.testFieldAccessNameSubstitutionInInnerClass() at distance(s): 5
* spoon.test.reference.ExecutableReferenceTest.testCallMethodOfClassNotPresent() at distance(s): 5, 6
* spoon.test.arrays.ArraysTest.testInitializeWithNewArray() at distance(s): 5
* spoon.test.imports.ImportTest.testImportStaticAndFieldAccess() at distance(s): 5
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunctionListener() at distance(s): 5, 7
* spoon.test.reference.ExecutableReferenceTest.testCreateReferenceForAnonymousExecutable() at distance(s): 5
* spoon.test.SpoonTestHelpers.getAllInstantiableMetamodelInterfaces() at distance(s): 5
* spoon.test.imports.ImportTest.testAccessPath() at distance(s): 5, 8
* spoon.test.generics.GenericsTest.testIsSameSignatureWithMethodGenerics() at distance(s): 5
* spoon.test.module.TestModule.testModuleInfoWithComments() at distance(s): 5
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverride() at distance(s): 5, 7
* spoon.test.fieldaccesses.FieldAccessTest.testFieldWriteWithPlusEqualsOperation() at distance(s): 5, 7
* spoon.test.eval.EvalTest.testVisitorPartialEvaluator_binary() at distance(s): 5
* spoon.test.executable.ExecutableRefTest.constructorTest() at distance(s): 5, 7
* spoon.test.interfaces.TestInterfaceWithoutSetup.testInterfacePrettyPrinting() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testReplaceAnnotationValue() at distance(s): 5
* spoon.test.refactoring.RefactoringTest.testThisInConstructor() at distance(s): 5
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageFullQualified() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testRecursiveTypeReferenceInGenericType() at distance(s): 5
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithNoImport() at distance(s): 5
* spoon.test.module.TestModule.testGetModuleAfterChangingItsName() at distance(s): 5
* spoon.test.type.TypeTest.testShadowType() at distance(s): 5
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testRecursiveTypeReference() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotatedElementTypes() at distance(s): 5
* spoon.test.factory.FactoryTest.testCtModel() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testToStringEqualityBetweenTwoGenericTypeDifferent() at distance(s): 5
* spoon.test.filters.FilterTest.testOverriddenMethodFromInterface() at distance(s): 5
* spoon.test.imports.ImportTest.testSuperInheritanceHierarchyFunction() at distance(s): 5, 7
* spoon.test.generics.GenericsTest.testTypeAdapted() at distance(s): 5, 7
* spoon.test.constructor.ConstructorTest.setUp() at distance(s): 5, 6
* spoon.test.generics.GenericsTest.testIsSameSignatureWithGenerics() at distance(s): 5
* spoon.reflect.visitor.CtScannerTest.testScannerContract() at distance(s): 5
* spoon.test.reference.ExecutableReferenceTest.testHashcodeWorksWithReference() at distance(s): 5
* spoon.test.filters.FilterTest.testReflectionBasedTypeFilter() at distance(s): 5
* spoon.test.reference.VariableAccessTest.testMultipleDeclarationsOfLocalVariable() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testFieldAndMethodInAnnotation() at distance(s): 5, 7
* spoon.test.imports.ImportAndExtendWithPackageNameTest.testBuildModel() at distance(s): 5
* spoon.test.replace.ReplaceTest.testReplaceAPackageReferenceByAnotherOne() at distance(s): 5
* spoon.test.javadoc.JavaDocTest.testJavadocNotPresentInAST() at distance(s): 5
* spoon.test.filters.FilterTest.testBoundQuery() at distance(s): 5
* spoon.test.filters.FilterTest.testReuseOfQuery() at distance(s): 5
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessDeclaredInADefaultClass() at distance(s): 5
* spoon.test.executable.ExecutableTest.testBlockInExecutable() at distance(s): 5, 7
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.importsFromMultipleTypesSupported() at distance(s): 5
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathExecutableReferenceExpression() at distance(s): 5, 6
* spoon.test.module.TestModule.testModuleInfoShouldBeCorrectlyPrettyPrinted() at distance(s): 5
* spoon.test.imports.ImportTest.testGetImportKindReturnRightValue() at distance(s): 5
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 5
* spoon.test.imports.ImportTest.testImportWithGenerics() at distance(s): 5
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessOnUnknownType() at distance(s): 5
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 5, 8
* spoon.test.trycatch.TryCatchTest.testCatchWithExplicitFinalVariable() at distance(s): 5
* spoon.test.filters.FilterTest.testClassCastExceptionOnForEach() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testArgumentOfAInvocationIsNotATypeAccess() at distance(s): 5
* spoon.test.generics.GenericsTest.testGetExecDeclarationOfEnumSetOf() at distance(s): 5
* spoon.test.annotation.AnnotationValuesTest.testAnnotationPrintAnnotation() at distance(s): 5
* spoon.test.imports.ImportTest.testImportStaticAndFieldAccessWithImport() at distance(s): 5
* spoon.test.secondaryclasses.ClassesTest.testAnonymousClassInStaticField() at distance(s): 5, 7
* spoon.test.annotation.AnnotationValuesTest.testValuesOnJava8Annotation() at distance(s): 5, 7
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessAutoExplicit() at distance(s): 5, 7
* spoon.reflect.visitor.CtInheritanceScannerMethodsTest.testMethodsInInheritanceScanner() at distance(s): 5
* spoon.test.method.MethodTest.testSearchMethodWithGeneric() at distance(s): 5, 7
* spoon.reflect.ast.CloneTest.testCloneMethodsDeclaredInAST() at distance(s): 5
* spoon.test.refactoring.RefactoringTest.testThisInConstructorAfterATransformation() at distance(s): 5
* spoon.test.parameters.ParameterTest.testMultiParameterLambdaTypeReference() at distance(s): 5
* spoon.testing.AbstractAssertTest.testTransformationWithProcessorInstantiated() at distance(s): 5, 6, 8
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnParameter() at distance(s): 5
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 5, 6
* spoon.test.processing.ProcessingTest.testInitPropertiesWithStringType() at distance(s): 5
* spoon.test.template.TemplateArrayAccessTest.testArrayLengthAccess() at distance(s): 5
* spoon.test.generics.GenericsTest.testClassContextOnInnerClass() at distance(s): 5, 7
* spoon.test.template.TemplateTest.testExtensionDecoupledSubstitutionVisitor() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testGetTypeDeclaration() at distance(s): 5
* spoon.test.query_function.VariableReferencesTest.setup() at distance(s): 5
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.printClassCreatedWithSpoon() at distance(s): 5
* spoon.test.lambda.LambdaTest.testFieldAccessInLambdaNoClassPath() at distance(s): 5
* spoon.test.api.APITest.testPrintNotAllSourcesWithNames() at distance(s): 5
* spoon.test.literal.LiteralTest.testBuildLiternal() at distance(s): 5, 7
* spoon.test.targeted.TargetedExpressionTest.testStaticTargetsOfFieldAccessNoClasspath() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInCast() at distance(s): 5
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 5
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 5
* spoon.test.factory.TypeFactoryTest.testGetClassInAnInterface() at distance(s): 5, 7
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 5, 8
* spoon.test.filters.FilterTest.testQueryWithOptionalNumberOfInputs() at distance(s): 5
* spoon.test.methodreference.MethodReferenceTest.testGetGenericMethodFromReference() at distance(s): 5, 7
* spoon.test.field.FieldTest.testGetDefaultExpression() at distance(s): 5
* spoon.test.prettyprinter.PrinterTest.testListPrinter() at distance(s): 5
* spoon.test.compilationunit.TestCompilationUnit.testAddDeclaredTypeInCU() at distance(s): 5
* spoon.test.position.PositionTest.getPositionOfImplicitBlock() at distance(s): 5
* spoon.test.fieldaccesses.FieldAccessTest.testGetReference() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testRepeatSameAnnotationOnLocalVariable() at distance(s): 5
* spoon.test.reference.VariableAccessTest.testParameterReferenceInConstructorNoClasspath() at distance(s): 5
* spoon.test.compilation.CompilationTest.testURLClassLoaderWithOtherResourcesThanOnlyFiles() at distance(s): 5
* spoon.test.condition.ConditionalTest.testConditional() at distance(s): 5, 7
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathSuperExecutable() at distance(s): 5
* spoon.test.template.TemplateTest.testObjectIsNotParamTemplate() at distance(s): 5
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsReturnsTheRightNumber() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.unboxTest() at distance(s): 5
* spoon.test.ctBlock.TestCtBlock.testRemoveStatement() at distance(s): 5
* spoon.reflect.visitor.CtScannerTest.testScan() at distance(s): 5
* spoon.test.compilation.CompilationTest.testNewInstanceFromExistingClass() at distance(s): 5, 7
* spoon.test.api.FileSystemFolderTest.testLauncherWithWrongPathAsInput() at distance(s): 5
* spoon.test.jdtimportbuilder.ImportBuilderTest.testInternalImportWhenNoClasspath() at distance(s): 5
* spoon.test.reference.ExecutableReferenceTest.testInvokeEnumMethod() at distance(s): 5
* spoon.test.ctType.CtTypeTest.testHasMethodInDefaultMethod() at distance(s): 5
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 5
* spoon.test.literal.LiteralTest.testEscapedString() at distance(s): 5
* spoon.test.processing.ProcessingTest.testInitProperties() at distance(s): 5
* spoon.testing.FileAssertTest.testEqualsBetweenTwoDifferentFile() at distance(s): 5, 6, 8
* spoon.test.parent.ParentTest.testHasParent() at distance(s): 5
* spoon.test.api.APITest.testSourceClasspathDoesNotAcceptDotClass() at distance(s): 5
* spoon.test.generics.GenericsTest.testWildcard() at distance(s): 5, 7
* spoon.test.fieldaccesses.FieldAccessTest.testTypeOfFieldAccess() at distance(s): 5, 7
* spoon.test.annotation.AnnotationTest.testWritingAnnotParamArray() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testIgnoreEnclosingClassInActualTypes() at distance(s): 5, 7
* spoon.test.compilationunit.TestCompilationUnit.testGetUnitTypeWorksWithCreatedObjects() at distance(s): 5
* spoon.test.lambda.LambdaTest.testFieldAccessInLambdaNoClassPathExternal1Example() at distance(s): 5
* spoon.test.compilationunit.GetBinaryFilesTest.testAnonymousClasses() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testAnonymousClassesHaveAnEmptyStringForItsNameInNoClasspath() at distance(s): 5
* spoon.test.annotation.AnnotationTest.annotationAddValue() at distance(s): 5
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInLoop() at distance(s): 5, 6, 8
* spoon.test.targeted.TargetedExpressionTest.testInitializeFieldAccessInNoclasspathMode() at distance(s): 5
* spoon.test.ctType.CtTypeParameterTest.testTypeErasure() at distance(s): 5, 7
* spoon.test.template.TemplateTest.testSubstitutionInsertAllNtoN() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testSubTypeAnonymous() at distance(s): 5, 7
* spoon.test.modifiers.TestModifiers.testGetModifiersHelpers() at distance(s): 5
* spoon.test.compilationunit.TestCompilationUnit.testNewlyCreatedCUWouldGetAPartialPosition() at distance(s): 5
* spoon.test.condition.ConditionalTest.testNoBlockInConditionAndLoop() at distance(s): 5, 7
* spoon.test.pkg.PackageTest.testRenamePackageAndPrettyPrint() at distance(s): 5
* spoon.test.filters.FilterTest.testNameFilterWithGenericType() at distance(s): 5
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 5
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByLocalVariable() at distance(s): 5, 6, 8
* spoon.test.filters.FilterTest.testInvocationFilterWithExecutableInLibrary() at distance(s): 5
* spoon.test.comparison.EqualTest.testEqualsEmptyException() at distance(s): 5
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotationInterfacePreserveMethods() at distance(s): 5
* spoon.test.ctClass.CtClassTest.testSpoonShouldInferImplicitPackageInNoClasspath() at distance(s): 5
* spoon.test.compilationunit.TestCompilationUnit.testGetUnitTypeWorksWithDeclaredPackage() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testNullReferenceSubtype() at distance(s): 5
* spoon.test.ctCase.SwitchCaseTest.insertBeforeStatementInSwitchCaseWithoutException() at distance(s): 5, 7
* spoon.test.field.FieldTest.testAddFieldsAtTop() at distance(s): 5, 7
* spoon.test.method.MethodTest.testGetAllMethods() at distance(s): 5
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameter() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInExtendsImplementsOfAClass() at distance(s): 5
* spoon.test.template.TemplateTest.testStatementTemplateRootSubstitution() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testConstructorCallInNoClasspath() at distance(s): 5
* spoon.test.variable.AccessTest.testStackedAssignments() at distance(s): 5, 7
* spoon.test.annotation.AnnotationTest.testRepeatableAnnotationAreManagedWithArrays() at distance(s): 5
* spoon.test.annotation.AnnotationTest.testAnnotationValueReflection() at distance(s): 5
* spoon.test.variable.AccessTest.testRHS() at distance(s): 5, 7
* spoon.test.pkg.PackageTest.testGetFQNSimple() at distance(s): 5
* spoon.reflect.ast.CloneTest.testCloneCastConditional() at distance(s): 5
* spoon.test.constructor.ConstructorTest.testTransformationOnConstructorWithInsertBegin() at distance(s): 5, 8
* spoon.test.compilationunit.GetBinaryFilesTest.testSingleBinary() at distance(s): 5
* spoon.test.executable.ExecutableTest.testGetReference() at distance(s): 5, 7
* spoon.test.reference.TypeReferenceTest.testEqualityTypeReference() at distance(s): 5, 7
* spoon.test.processing.ProcessingTest.testProcessorNotFoundThrowAnException() at distance(s): 5, 6
* spoon.test.annotation.AnnotationTest.testCreateAnnotation() at distance(s): 5
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 5
* spoon.test.compilationunit.GetBinaryFilesTest.testNestedTypes() at distance(s): 5
* spoon.test.method_overriding.MethodOverriddingTest.testMethodOverrideByReference() at distance(s): 5, 7
* spoon.test.filters.FilterTest.testEmptyQuery() at distance(s): 5
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 5, 8
* spoon.test.reference.ExecutableReferenceTest.testLambdaNoClasspath() at distance(s): 5
* spoon.test.reference.TypeReferenceTest.testUnknownSuperClassWithSameNameInNoClasspath() at distance(s): 5
* spoon.test.comment.CommentTest.testInLineComment() at distance(s): 6, 7
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(java.io.File) at distance(s): 6
* spoon.test.api.APITest.testOverrideOutputWriter() at distance(s): 6
* spoon.test.imports.ImportTest.testImportOfInvocationOfStaticMethod() at distance(s): 6
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReferenceAutoImport() at distance(s): 6, 9
* spoon.test.comment.CommentTest.testCombinedPackageInfoComment() at distance(s): 6, 7
* spoon.test.comment.CommentTest.testCodeFactory() at distance(s): 6, 7
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 6, 9
* spoon.test.comment.CommentTest.testJavaDocCommentOnUnix() at distance(s): 6, 7
* spoon.test.api.APITest.testDuplicateFilePlusFolder() at distance(s): 6, 7
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticField() at distance(s): 6, 9
* spoon.test.api.APITest.testDuplicateFolder() at distance(s): 6, 7
* spoon.test.comment.CommentTest.testJavaDocEmptyCommentAndTag() at distance(s): 6, 7
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReference() at distance(s): 6, 9
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstants() at distance(s): 6, 9
* spoon.test.comment.CommentTest.testInsertNewComment() at distance(s): 6, 7
* spoon.test.comment.CommentTest.testWildComments() at distance(s): 6, 7
* spoon.test.comment.CommentTest.testRemoveComment() at distance(s): 6, 7
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReference() at distance(s): 6, 9
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberField() at distance(s): 6, 9
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 6, 9
* spoon.test.api.APITest.testOneLinerIntro() at distance(s): 6
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 6, 9
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 6, 9
* spoon.test.api.APITest.testDuplicateEntry() at distance(s): 6, 7
* spoon.test.imports.ImportTest.testNotImportExecutableType() at distance(s): 6
* spoon.test.imports.ImportTest.testImportOfInvocationOfPrivateClass() at distance(s): 6
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReferenceAutoImport() at distance(s): 6, 9
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 6
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 6, 9
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 6, 9
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 6, 9
* spoon.test.comment.CommentTest.testCoreFactory() at distance(s): 6, 7
* spoon.test.comment.CommentTest.testCommentsInComment1And2() at distance(s): 6, 7
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticField() at distance(s): 6, 9
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccess() at distance(s): 6, 9
* spoon.test.comment.CommentTest.testBlockComment() at distance(s): 6, 7
* spoon.test.api.APITest.testNotValidInput() at distance(s): 6, 7
* spoon.MavenLauncherTest.mavenLauncherTestWithVerySimpleProject() at distance(s): 7
* spoon.MavenLauncherTest.mavenLauncherOnDirectoryWithoutPomTest() at distance(s): 7
* spoon.MavenLauncherTest.mavenLauncherOnANotExistingFileTest() at distance(s): 7
* spoon.MavenLauncherTest.multiModulesProjectTest() at distance(s): 7
* spoon.MavenLauncherTest.spoonMavenLauncherTest() at distance(s): 7


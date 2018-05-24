# getLineNumberMapping()

**Class:** spoon.reflect.visitor.DefaultJavaPrettyPrinter

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/DefaultJavaPrettyPrinter.java#L1986)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 162 test method(s) with a minimum stack distance of 2.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return null;
```





## Observed test methods

* spoon.test.prettyprinter.DefaultPrettyPrinterTest.printClassCreatedWithSpoon() at distance(s): 2
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 10
* spoon.test.api.APITest.testPrintNotAllSourcesWithFilter() at distance(s): 10
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 10
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 10
* spoon.test.api.APITest.testPrintNotAllSourcesWithNames() at distance(s): 10
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 10
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 11
* spoon.test.reference.TypeReferenceTest.testAnnotationOnMethodWithPrimitiveReturnTypeInNoClasspath() at distance(s): 21
* spoon.test.reference.TypeReferenceTest.testPackageInNoClasspath() at distance(s): 21
* spoon.test.targeted.TargetedExpressionTest.testStaticTargetsOfInvNoClasspath() at distance(s): 21
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 21
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessNoClasspath() at distance(s): 21, 33
* spoon.test.reference.TypeReferenceTest.testTypeReferenceSpecifiedInClassDeclarationInNoClasspathWithGenerics() at distance(s): 21
* spoon.test.api.NoClasspathTest.test() at distance(s): 21
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 21, 39
* spoon.test.reference.TypeReferenceTest.testTypeReferenceSpecifiedInClassDeclarationInNoClasspath() at distance(s): 21
* spoon.test.reference.TypeReferenceTest.testArgumentOfAInvocationIsNotATypeAccess() at distance(s): 21
* spoon.test.targeted.TargetedExpressionTest.testStaticTargetsOfFieldAccessNoClasspath() at distance(s): 21
* spoon.test.reference.TypeReferenceTest.testInvocationWithFieldAccessInNoClasspath() at distance(s): 21
* spoon.test.reference.TypeReferenceTest.testAnonymousClassesHaveAnEmptyStringForItsNameInNoClasspath() at distance(s): 21
* spoon.test.targeted.TargetedExpressionTest.testInitializeFieldAccessInNoclasspathMode() at distance(s): 21
* spoon.test.compilation.CompilationTest.compileCommandLineTest() at distance(s): 22
* spoon.test.methodreference.MethodReferenceTest.testNoClasspathExecutableReferenceExpression() at distance(s): 22
* spoon.test.api.APITest.testDuplicateFilePlusFolder() at distance(s): 23
* spoon.test.api.APITest.testDuplicateFolder() at distance(s): 23
* spoon.test.api.APITest.testDuplicateEntry() at distance(s): 23
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 27, 33
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 27, 33
* spoon.processing.ProcessingTest.testSpoonTagger() at distance(s): 27
* spoon.test.pkg.PackageTest.testRenamePackageAndPrettyPrintWithProcessor() at distance(s): 27
* spoon.test.interfaces.TestInterfaceWithoutSetup.testInterfacePrettyPrinting() at distance(s): 27
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses() at distance(s): 33, 39
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 33, 39, 45
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 38, 44
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 38, 44
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 38, 44
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 38, 44
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 39, 45
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReferenceAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticField() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReference() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstants() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReference() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberField() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 39
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReferenceAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticField() at distance(s): 39
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccess() at distance(s): 39
* spoon.test.variable.AccessTest.testFieldWriteDeclaredInTheSuperclass() at distance(s): 40
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameterWithImports() at distance(s): 44
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 44
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 44, 50
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation() at distance(s): 44
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameterWithImports() at distance(s): 44
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameter() at distance(s): 44
* spoon.test.methodreference.MethodReferenceTest.setUp() at distance(s): 44
* spoon.test.imports.ImportTest.testDeepNestedStaticPathWithTypedParameter() at distance(s): 44
* spoon.test.arrays.ArraysTest.testCtNewArrayWitComments() at distance(s): 44
* spoon.test.arrays.ArraysTest.testCtNewArrayInnerCtNewArray() at distance(s): 44
* spoon.test.pkg.PackageTest.testAnnotationOnPackage() at distance(s): 44
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 44
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 44
* spoon.test.imports.ImportTest.testNestedAccessPathWithTypedParameter() at distance(s): 44
* spoon.test.comment.CommentTest.testJavaDocCommentOnMac() at distance(s): 45
* spoon.test.visibility.VisibilityTest.testFullyQualifiedNameOfTypeReferenceWithGeneric() at distance(s): 45
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 45
* spoon.test.imports.ImportTest.testShouldNotCreateAutoreference() at distance(s): 45
* spoon.test.api.APITest.testInvalidateCacheOfCompiler() at distance(s): 45
* spoon.test.modifiers.TestModifiers.testMethodWithVarargsDoesNotBecomeTransient() at distance(s): 45
* spoon.test.refactoring.RefactoringTest.testTransformedInstanceofAfterATransformation() at distance(s): 45
* spoon.test.type.TypeTest.testTypeAccessOfArrayObjectInFullyQualifiedName() at distance(s): 45
* spoon.test.reference.ExecutableReferenceTest.testSuperClassInGetAllExecutables() at distance(s): 45
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 45, 51
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 45
* spoon.test.ctType.CtTypeTest.testHasMethodInSuperClass() at distance(s): 45
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 45, 51
* spoon.test.parameters.ParameterTest.testParameterInNoClasspath() at distance(s): 45
* spoon.test.type.TypeTest.testTypeAccessForTypeAccessInInstanceOf() at distance(s): 45
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 45
* spoon.test.type.TypeTest.testIntersectionTypeReferenceInGenericsAndCasts() at distance(s): 45
* spoon.test.api.APITest.testOutputOfSpoon() at distance(s): 45
* spoon.test.type.TypeTest.testTypeReferenceInGenericsAndCasts() at distance(s): 45
* spoon.test.api.APITest.testAddProcessorMethodInSpoonAPI() at distance(s): 45
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 45
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 45, 51
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 45, 51
* spoon.test.api.NoClasspathTest.testGetStaticDependency() at distance(s): 45
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 45
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 45
* spoon.test.constructorcallnewclass.ConstructorCallTest.setUp() at distance(s): 45
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 45, 51
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 45
* spoon.test.api.APITest.testDestinationOfSpoon() at distance(s): 45
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 45
* spoon.test.imports.ImportTest.testAccessPath() at distance(s): 45
* spoon.test.refactoring.RefactoringTest.testThisInConstructor() at distance(s): 45
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageFullQualified() at distance(s): 45, 51
* spoon.test.reference.TypeReferenceTest.testRecursiveTypeReferenceInGenericType() at distance(s): 45
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 45
* spoon.test.reference.TypeReferenceTest.testRecursiveTypeReference() at distance(s): 45
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.importsFromMultipleTypesSupported() at distance(s): 45
* spoon.test.type.TypeTest.testTypeAccessForDotClass() at distance(s): 45
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 45
* spoon.test.imports.ImportTest.testImportWithGenerics() at distance(s): 45
* spoon.test.trycatch.TryCatchTest.testCatchWithExplicitFinalVariable() at distance(s): 45
* spoon.test.refactoring.RefactoringTest.testThisInConstructorAfterATransformation() at distance(s): 45
* spoon.test.ctType.CtTypeTest.testHasMethodInDefaultMethod() at distance(s): 45
* spoon.test.api.APITest.testSourceClasspathDoesNotAcceptDotClass() at distance(s): 45
* spoon.test.modifiers.TestModifiers.testGetModifiersHelpers() at distance(s): 45
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 45
* spoon.test.generics.GenericsTest.testGenericsInQualifiedNameInConstructorCall() at distance(s): 46, 52
* spoon.test.generics.GenericsTest.testInvocationGenerics() at distance(s): 46, 52
* spoon.test.visibility.VisibilityTest.testName() at distance(s): 46
* spoon.test.generics.GenericsTest.testConstructorCallGenerics() at distance(s): 46, 52
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 46
* spoon.test.comment.CommentTest.testCommentsInResourcesWithWindowsEOL() at distance(s): 46
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByField() at distance(s): 46
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 46
* spoon.test.enums.EnumsTest.testAnnotationsOnEnum() at distance(s): 46
* spoon.test.generics.GenericsTest.testNewClassGenerics() at distance(s): 46, 52
* spoon.test.invocations.InvocationTest.testTypeOfStaticInvocation() at distance(s): 46
* spoon.test.generics.GenericsTest.testName() at distance(s): 46, 52
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInTryCatch() at distance(s): 46
* spoon.test.generics.GenericsTest.testMethodsWithGenericsWhoExtendsObject() at distance(s): 46, 52
* spoon.test.constructor.ConstructorTest.setUp() at distance(s): 46
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInLoop() at distance(s): 46
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByLocalVariable() at distance(s): 46
* spoon.test.comment.CommentTest.testInLineComment() at distance(s): 47
* spoon.test.comment.CommentTest.testCombinedPackageInfoComment() at distance(s): 47
* spoon.test.comment.CommentTest.testCodeFactory() at distance(s): 47
* spoon.test.comment.CommentTest.testJavaDocCommentOnUnix() at distance(s): 47
* spoon.test.trycatch.TryCatchTest.testCompileMultiTryCatchWithCustomExceptions() at distance(s): 47, 53
* spoon.test.comment.CommentTest.testJavaDocEmptyCommentAndTag() at distance(s): 47
* spoon.test.comment.CommentTest.testInsertNewComment() at distance(s): 47
* spoon.test.comment.CommentTest.testWildComments() at distance(s): 47
* spoon.test.comment.CommentTest.testRemoveComment() at distance(s): 47
* spoon.test.comment.CommentTest.testCoreFactory() at distance(s): 47
* spoon.test.comment.CommentTest.testCommentsInComment1And2() at distance(s): 47
* spoon.test.comment.CommentTest.testBlockComment() at distance(s): 47
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 50
* spoon.test.annotation.AnnotationTest.testSpoonSpoonResult() at distance(s): 51
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 51, 57
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 51
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 51, 57
* spoon.test.generics.GenericsTest.testDiamondComplexGenericsRxJava() at distance(s): 51
* spoon.test.annotation.AnnotationTest.testAnnotationTypeAndFieldOnField() at distance(s): 51
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 51, 57
* spoon.test.executable.ExecutableRefTest.testSameTypeInConstructorCallBetweenItsObjectAndItsExecutable() at distance(s): 51
* spoon.test.reference.TypeReferenceTest.testUnknownSuperClassWithSameNameInNoClasspath() at distance(s): 51
* spoon.test.variable.AccessFullyQualifiedFieldTest.testPrivateStaticImportShouldNotBeImportedInSameClass() at distance(s): 52
* spoon.test.variable.AccessTest.testVariableAccessInNoClasspath() at distance(s): 57
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 57
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 73, 84, 90, 100, 111


# isImportedInMethodImports(spoon.reflect.reference.CtExecutableReference)

**Class:** spoon.reflect.visitor.ImportScannerImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/ImportScannerImpl.java#L459)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 72 test method(s) with a minimum stack distance of 18.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return false;
```

The following transformations were also applied and they were detected by the test suite:

```Java
return true;
```





## Observed test methods

* spoon.test.api.APITest.testOneLinerIntro() at distance(s): 18
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 19, 24, 30, 42, 44, 50, 63, 68, 74, 86, 88, 94
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 19, 24, 30, 63, 68, 74
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 20, 25, 26, 31, 33, 42
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 22
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 24, 32, 37, 80, 88, 93
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 24, 32, 35, 37, 80, 88, 91, 93
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 24, 27, 30, 32, 34, 35, 36, 37, 39, 41, 44, 45, 46, 50, 51, 53, 54, 62, 65, 67, 68, 70, 72, 73, 74, 75, 77, 79, 82, 83, 84, 88, 89, 90, 91, 92, 100, 103, 105, 126, 128
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 24, 68
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 24, 32, 37, 80, 88, 93
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports() at distance(s): 28
* spoon.test.imports.ImportScannerTest.testComputeImportsInClass() at distance(s): 29
* spoon.test.imports.ImportTest.testImportOfInvocationOfStaticMethod() at distance(s): 30
* spoon.test.imports.ImportScannerTest.testComputeMinimalImportsInClass() at distance(s): 30
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 32
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 32, 76
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 32, 33, 42, 43, 44, 45, 47, 57, 59, 76, 77, 91
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 34, 36, 42, 44, 68, 76
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 34, 46
* spoon.test.imports.ImportTest.testNotImportExecutableType() at distance(s): 36
* spoon.test.variable.AccessFullyQualifiedFieldTest.testPrivateStaticImportShouldNotBeImportedInSameClass() at distance(s): 38, 88
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 39
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 43, 47, 48, 52
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 46, 47, 51, 52, 53, 57, 58, 59, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 83, 85, 86, 89, 91, 93, 95
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 48, 54, 56, 92, 98, 100
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 55, 58, 99, 102
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 55, 58, 99, 102
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 57, 62, 63, 68
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 58, 62, 63, 64, 68, 69, 70, 71, 72, 75, 76, 77, 79, 80, 81, 82, 84, 86, 87, 88, 89, 90, 93, 96, 99, 101, 103, 105, 106, 112, 113, 129
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 58, 63, 70, 72, 75, 77, 80, 81, 84, 86, 89, 93
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 62, 67, 68, 73, 75, 76
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 62, 68, 70
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 62, 68, 70
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 62, 68, 70
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 62, 69
* spoon.test.visibility.VisibilityTest.testFullyQualifiedNameOfTypeReferenceWithGeneric() at distance(s): 64, 69
* spoon.test.processing.ProcessingTest.testCallProcessorWithMultipleTypes() at distance(s): 64, 69
* spoon.test.processing.ProcessingTest.testProcessorWithGenericType() at distance(s): 64, 69
* spoon.test.generics.GenericsTest.testGenericsInQualifiedNameInConstructorCall() at distance(s): 65, 70, 77, 78
* spoon.test.generics.GenericsTest.testInvocationGenerics() at distance(s): 65, 70, 77, 78
* spoon.test.generics.GenericsTest.testConstructorCallGenerics() at distance(s): 65, 70, 77, 78
* spoon.test.generics.GenericsTest.testNewClassGenerics() at distance(s): 65, 70, 77, 78
* spoon.test.generics.GenericsTest.testName() at distance(s): 65, 70, 77, 78
* spoon.test.generics.GenericsTest.testMethodsWithGenericsWhoExtendsObject() at distance(s): 65, 70, 77, 78
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 68, 70
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccess() at distance(s): 70
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 71, 72
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberField() at distance(s): 71
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticField() at distance(s): 71
* spoon.test.refactoring.RefactoringTest.testTransformedInstanceofAfterATransformation() at distance(s): 76, 96
* spoon.test.methodreference.MethodReferenceTest.setUp() at distance(s): 76
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 76, 96
* spoon.test.refactoring.RefactoringTest.testThisInConstructor() at distance(s): 76, 96
* spoon.test.refactoring.RefactoringTest.testThisInConstructorAfterATransformation() at distance(s): 76, 96
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 76, 77, 78, 80, 81, 82, 83, 86
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 77, 78, 81, 86
* spoon.test.parameters.ParameterTest.testParameterInNoClasspath() at distance(s): 77, 81, 90, 102, 103
* spoon.test.comment.CommentTest.testInLineComment() at distance(s): 79
* spoon.test.comment.CommentTest.testCombinedPackageInfoComment() at distance(s): 79
* spoon.test.comment.CommentTest.testCodeFactory() at distance(s): 79
* spoon.test.comment.CommentTest.testJavaDocCommentOnUnix() at distance(s): 79
* spoon.test.comment.CommentTest.testJavaDocEmptyCommentAndTag() at distance(s): 79
* spoon.test.comment.CommentTest.testInsertNewComment() at distance(s): 79
* spoon.test.comment.CommentTest.testWildComments() at distance(s): 79
* spoon.test.comment.CommentTest.testRemoveComment() at distance(s): 79
* spoon.test.comment.CommentTest.testCoreFactory() at distance(s): 79
* spoon.test.comment.CommentTest.testCommentsInComment1And2() at distance(s): 79
* spoon.test.comment.CommentTest.testBlockComment() at distance(s): 79
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 88
* spoon.test.variable.AccessTest.testVariableAccessInNoClasspath() at distance(s): 90
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 90, 92, 101, 103, 107, 109, 117, 119, 124, 128, 130, 135, 141, 151, 162
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 95


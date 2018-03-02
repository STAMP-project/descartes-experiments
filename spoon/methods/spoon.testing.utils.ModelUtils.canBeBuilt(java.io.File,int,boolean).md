# canBeBuilt(java.io.File,int,boolean)

**Class:** spoon.testing.utils.ModelUtils

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/testing/utils/ModelUtils.java#L108)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 63 test method(s) with a minimum stack distance of 2.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 2
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 2
* spoon.test.type.TypeTest.testTypeAccessOfArrayObjectInFullyQualifiedName() at distance(s): 2
* spoon.test.template.TemplateReplaceReturnTest.testReturnReplaceTemplate() at distance(s): 2
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 2
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation() at distance(s): 2
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 2
* spoon.test.type.TypeTest.testIntersectionTypeReferenceInGenericsAndCasts() at distance(s): 2
* spoon.test.template.TemplateEnumAccessTest.testEnumAccessTest() at distance(s): 2
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 2
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 2
* spoon.test.methodreference.MethodReferenceTest.testCompileMethodReferenceGeneratedBySpoon() at distance(s): 2
* spoon.test.type.TypeTest.testTypeReferenceInGenericsAndCasts() at distance(s): 2
* spoon.test.pkg.PackageTest.testAddAnnotationToPackage() at distance(s): 2
* spoon.test.type.TypeTest.testTypeAccessForDotClass() at distance(s): 2
* spoon.test.template.TemplateReplaceReturnTest.testNoReturnReplaceTemplate() at distance(s): 2
* spoon.test.lambda.LambdaTest.testCompileLambdaGeneratedBySpoon() at distance(s): 2
* spoon.test.reference.TypeReferenceTest.testInvocationWithFieldAccessInNoClasspath() at distance(s): 2
* spoon.test.executable.ExecutableRefTest.testSameTypeInConstructorCallBetweenItsObjectAndItsExecutable() at distance(s): 2
* spoon.test.visibility.VisibilityTest.testFullyQualifiedNameOfTypeReferenceWithGeneric() at distance(s): 3
* spoon.test.generics.GenericsTest.testInvocationGenerics() at distance(s): 3
* spoon.test.imports.ImportTest.testShouldNotCreateAutoreference() at distance(s): 3
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 3
* spoon.test.generics.GenericsTest.testConstructorCallGenerics() at distance(s): 3
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 3
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 3
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 3
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 3
* spoon.test.generics.GenericsTest.testDiamondComplexGenericsRxJava() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testPrivateStaticImportShouldNotBeImportedInSameClass() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByField() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 3
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 3
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 3
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImported() at distance(s): 3
* spoon.test.generics.GenericsTest.testNewClassGenerics() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInTryCatch() at distance(s): 3
* spoon.test.imports.ImportTest.testAccessPath() at distance(s): 3
* spoon.test.refactoring.MethodsRefactoringTest.testCtParameterRemoveRefactoring() at distance(s): 3
* spoon.test.template.TemplateTest.substituteTypeAccessReference() at distance(s): 3
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInLoop() at distance(s): 3
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenShadowedByLocalVariable() at distance(s): 3
* spoon.test.constructor.ConstructorTest.testTransformationOnConstructorWithInsertBegin() at distance(s): 3
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 3
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReferenceAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticField() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitFieldReference() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstants() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReference() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberField() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAmbiguousImplicitFieldReferenceAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccessAutoImport() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticField() at distance(s): 4
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticClassAccess() at distance(s): 4


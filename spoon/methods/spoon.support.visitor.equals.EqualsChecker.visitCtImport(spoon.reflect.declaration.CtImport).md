# visitCtImport(spoon.reflect.declaration.CtImport)

**Class:** spoon.support.visitor.equals.EqualsChecker

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/equals/EqualsChecker.java#L261)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 30 test method(s) with a minimum stack distance of 13.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.imports.ImportTest.testEqualsImports() at distance(s): 13
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 14, 64, 70
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 14, 28
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 14, 31, 64, 70, 87
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 14, 32, 58, 76
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 14, 47, 52, 85
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.importsFromMultipleTypesSupported() at distance(s): 14
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 14, 24, 26, 28, 31, 38, 40, 41, 43, 58, 72, 75
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 14, 64, 70
* spoon.test.imports.ImportTest.testmportInCu() at distance(s): 19
* spoon.test.prettyprinter.LinesTest.testIdenticalPrettyPrinter() at distance(s): 19
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 23
* spoon.test.imports.ImportTest.testNestedStaticPathWithTypedParameterWithImports() at distance(s): 23, 25, 57
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 24, 26, 64
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 24, 26, 58, 64
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 31, 32, 75, 76
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 33, 47, 77, 91
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 34, 35, 36, 37, 50, 51
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 35, 37, 69
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 41, 43, 87
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 47, 91
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReference() at distance(s): 52, 70
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 54, 57, 58, 63, 79
* spoon.test.pkg.PackageTest.testAnnotationInPackageInfoWhenTemplatesCompiled() at distance(s): 57
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 57
* spoon.test.imports.ImportTest.testJavaLangIsConsideredAsImportedButNotForSubPackages() at distance(s): 58
* spoon.test.javadoc.JavaDocTest.testJavaDocReprint() at distance(s): 58
* spoon.test.imports.ImportTest.testMultipleCU() at distance(s): 64
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 66, 70
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 72


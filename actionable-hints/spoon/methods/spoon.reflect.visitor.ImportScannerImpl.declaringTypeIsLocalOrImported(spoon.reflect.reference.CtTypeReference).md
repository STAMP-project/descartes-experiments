# declaringTypeIsLocalOrImported(spoon.reflect.reference.CtTypeReference)

**Class:** spoon.reflect.visitor.ImportScannerImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/ImportScannerImpl.java#L379)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `true`


It can not be accessed from other classes. 
It has been covered by 25 test method(s) with a minimum stack distance of 12.

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

* spoon.test.fieldaccesses.FieldAccessTest.testGetReference() at distance(s): 12
* spoon.test.imports.ImportTest.testImportStaticAndFieldAccessWithImport() at distance(s): 14
* spoon.test.api.APITest.testOneLinerIntro() at distance(s): 15
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 22, 25, 27, 31, 32, 36, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 53, 57, 58, 60, 62, 63, 65, 69, 70, 74, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 91, 95, 96, 100, 123
* spoon.test.imports.ImportTest.testImportOfInvocationOfStaticMethod() at distance(s): 25
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 25, 26, 28
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 27, 30, 31
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 27, 32, 83, 88
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 27, 31, 37, 39, 41, 43, 71, 75
* spoon.test.imports.ImportScannerTest.testComputeImportsInClass() at distance(s): 28
* spoon.test.prettyprinter.QualifiedThisRefTest.testQualifiedThisRef() at distance(s): 29
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 30, 51, 55, 74, 95, 99
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 30, 31, 74, 75
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 31, 32, 33, 34, 65, 66
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 31, 32, 33, 34, 47, 48
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 35, 37, 39, 40, 44, 45, 48, 52, 57, 79, 81, 83, 84, 88, 89, 92, 96, 101
* spoon.test.prettyprinter.LinesTest.testCompileWhenUsingLinesArgument() at distance(s): 40, 42, 74
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 40, 41, 42, 43, 45, 47, 86, 87, 91
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 46
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 59, 61
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 59, 65, 68, 69, 73
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 65
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 65
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 65
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 70, 73, 82, 83


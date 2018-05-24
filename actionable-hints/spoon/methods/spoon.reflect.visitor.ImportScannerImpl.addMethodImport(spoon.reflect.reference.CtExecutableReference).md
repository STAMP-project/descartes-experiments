# addMethodImport(spoon.reflect.reference.CtExecutableReference)

**Class:** spoon.reflect.visitor.ImportScannerImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/ImportScannerImpl.java#L429)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 19 test method(s) with a minimum stack distance of 21.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return false;
```

```Java
return true;
```





## Observed test methods

* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 21, 26, 30, 31, 35, 38, 40, 42, 43, 44, 46, 47, 48, 52, 56, 59, 61, 64, 68, 69, 73, 76, 78, 80, 81, 82, 84, 85, 86, 90, 94, 99, 122
* spoon.test.imports.ImportTest.testImportOfInvocationOfStaticMethod() at distance(s): 24
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 24
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava3NoCollision() at distance(s): 26, 31, 82, 87
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 26
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 26, 31, 82, 87
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 26, 30, 36, 38, 40, 42, 70, 74
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameCollision() at distance(s): 26, 31, 82, 87
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 30, 74
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithStaticInheritedImport() at distance(s): 31, 33, 65
* spoon.test.jdtimportbuilder.ImportBuilderTest.testWithImportFromItf() at distance(s): 31, 33, 47
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 36, 38, 39, 44, 47, 51, 56, 80, 82, 83, 88, 91, 95, 100
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 40, 42, 44, 46, 86, 90
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 50, 94
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 64, 72
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 64
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 64
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 64
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 69, 81


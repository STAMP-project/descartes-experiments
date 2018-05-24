# classNamePresentInJavaLang(spoon.reflect.reference.CtTypeReference)

**Class:** spoon.reflect.visitor.ImportScannerImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/ImportScannerImpl.java#L510)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 14 test method(s) with a minimum stack distance of 13.

## Transformations


The body of this method has been replaced by the following instuctions and no transformation was detected by the test suite:

```Java
return false;
```

```Java
return true;
```





## Observed test methods

* spoon.test.fieldaccesses.FieldAccessTest.testGetReference() at distance(s): 13
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 26, 28, 32, 33, 37, 40, 42, 44, 45, 46, 48, 49, 50, 54, 63, 64, 66, 70, 71, 75, 78, 80, 82, 83, 84, 86, 87, 88, 92, 101, 124
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.autoImportUsesFullyQualifiedNameWhenImportedNameAlreadyPresent() at distance(s): 26, 27, 29
* spoon.test.variable.AccessFullyQualifiedFieldTest.testStaticImportWithAutoImport() at distance(s): 31, 52, 56, 75, 96, 100
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 31, 32, 75, 76
* spoon.test.imports.ImportTest.testStaticMethodWithDifferentClassSameNameJava7NoCollision() at distance(s): 33, 89
* spoon.test.prettyprinter.PrinterTest.testRuleCanBeBuild() at distance(s): 36, 40, 41, 45, 49, 53, 58, 80, 84, 85, 89, 93, 97, 102
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 41, 42, 43, 44, 46, 48, 87, 88, 92
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testAnnotationInChildWithConstantsAutoImport() at distance(s): 60, 62
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testImplicitStaticFieldReferenceAutoImport() at distance(s): 60, 66, 69, 70, 74
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousMemberFieldAutoImport() at distance(s): 66
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 66
* spoon.test.staticFieldAccess2.ImplicitStaticFieldReferenceTest.testChildOfGenericsWithAmbiguousStaticFieldAutoImport() at distance(s): 66
* spoon.test.visibility.VisibilityTest.testVisibilityOfClassesNamedByClassesInJavaLangPackage() at distance(s): 71, 83, 84


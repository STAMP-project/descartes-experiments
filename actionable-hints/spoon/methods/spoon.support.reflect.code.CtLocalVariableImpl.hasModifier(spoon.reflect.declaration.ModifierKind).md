# hasModifier(spoon.reflect.declaration.ModifierKind)

**Class:** spoon.support.reflect.code.CtLocalVariableImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/reflect/code/CtLocalVariableImpl.java#L117)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 30 test method(s) with a minimum stack distance of 12.

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

* spoon.test.field.FieldTest.testFieldImplicitTarget() at distance(s): 12
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessNoClasspath() at distance(s): 16, 20, 61
* spoon.test.eval.EvalTest.testVisitorPartialEvaluatorScanner() at distance(s): 26, 30, 35
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 29, 32, 33, 41, 51
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 32, 35, 38, 41, 44, 50, 53, 59, 70, 73, 76, 79, 82, 88, 91, 97
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 38
* spoon.test.reference.VariableAccessTest.testMultipleDeclarationsOfLocalVariable() at distance(s): 38
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 39, 42, 49, 78
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 77, 79, 80, 81, 82, 83, 86, 88, 90
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 46, 49, 50, 52, 58, 61, 67
* spoon.test.prettyprinter.PrinterTest.testFQNModeWriteFQNConstructorInCtVisitor() at distance(s): 48, 57
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 54
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 57, 66
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 60, 63, 69, 71, 74
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 64, 67, 70, 73, 76, 79, 82, 83, 86, 88, 91, 94, 97, 99, 110, 139
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 67, 70, 73, 76, 79, 91, 94
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 71, 82
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 73, 74, 76, 77, 82, 85, 93
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 73, 83, 86, 90
* spoon.test.filters.FilterTest.testFunctionQueryStep() at distance(s): 75, 77, 79, 81, 84
* spoon.test.reference.VariableAccessTest.testReferenceToLocalVariableDeclaredInLoop() at distance(s): 77
* spoon.test.generics.GenericsTest.testDiamondComplexGenericsRxJava() at distance(s): 79
* spoon.test.generics.GenericsTest.testGenericsInQualifiedNameInConstructorCall() at distance(s): 80
* spoon.test.generics.GenericsTest.testInvocationGenerics() at distance(s): 80
* spoon.test.generics.GenericsTest.testConstructorCallGenerics() at distance(s): 80
* spoon.test.generics.GenericsTest.testNewClassGenerics() at distance(s): 80
* spoon.test.generics.GenericsTest.testName() at distance(s): 80
* spoon.test.generics.GenericsTest.testMethodsWithGenericsWhoExtendsObject() at distance(s): 80
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 119
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 122


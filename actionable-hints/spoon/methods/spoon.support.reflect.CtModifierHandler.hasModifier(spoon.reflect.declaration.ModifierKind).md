# hasModifier(spoon.reflect.declaration.ModifierKind)

**Class:** spoon.support.reflect.CtModifierHandler

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/reflect/CtModifierHandler.java#L72)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 9 test method(s) with a minimum stack distance of 3.

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

* spoon.test.modifiers.TestModifiers.testSetVisibility() at distance(s): 3
* spoon.test.method.MethodTest.testClone() at distance(s): 3
* spoon.test.initializers.InitializerTest.testModelBuildingInitializer() at distance(s): 16
* spoon.test.template.TemplateTest.testAnotherFieldAccessNameSubstitution() at distance(s): 19
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 27, 33, 45
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 73
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface() at distance(s): 75
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 110
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 113


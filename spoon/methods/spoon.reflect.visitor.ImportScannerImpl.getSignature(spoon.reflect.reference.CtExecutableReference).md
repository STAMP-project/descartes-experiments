# getSignature(spoon.reflect.reference.CtExecutableReference)

**Class:** spoon.reflect.visitor.ImportScannerImpl

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/ImportScannerImpl.java#L471)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `&quot;&quot;`, `&quot;A&quot;`


It can not be accessed from other classes. 
It has been covered by 4 test method(s) with a minimum stack distance of 56.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return "";
```

```Java
return "A";
```

The following transformations were also applied and they were detected by the test suite:

```Java
return null;
```





## Observed test methods

* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNAndStaticImport() at distance(s): 56, 100
* spoon.test.variable.AccessFullyQualifiedFieldTest.testNoFQNWhenUsedInInnerClassAndShadowedByLocalVariable() at distance(s): 56, 100
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testIssue1501() at distance(s): 72
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 73, 74, 82, 86, 90, 94


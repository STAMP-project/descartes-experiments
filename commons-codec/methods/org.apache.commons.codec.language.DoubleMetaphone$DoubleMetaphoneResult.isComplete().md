# isComplete()

**Class:** org.apache.commons.codec.language.DoubleMetaphone$DoubleMetaphoneResult

[[View code]](https://github.com/apache/commons-codec/blob/588602694fa1d19e433f9e2705aed9ccb0b404ba/src/main/java//org/apache/commons/codec/language/DoubleMetaphone.java#L1005)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 14 test method(s) with a minimum stack distance of 2.

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

* org.apache.commons.codec.language.DoubleMetaphoneTest.assertDoubleMetaphoneAlt(java.lang.String,java.lang.String) at distance(s): 2
* org.apache.commons.codec.language.DoubleMetaphoneTest.testSetMaxCodeLength() at distance(s): 2
* org.apache.commons.codec.language.DoubleMetaphoneTest.testDoubleMetaphone() at distance(s): 3, 4, 5
* org.apache.commons.codec.language.DoubleMetaphone2Test.testDoubleMetaphoneAlternate() at distance(s): 3
* org.apache.commons.codec.language.DoubleMetaphoneTest.testIsDoubleMetaphoneEqualExtended3() at distance(s): 3
* org.apache.commons.codec.language.DoubleMetaphoneTest.testCodec184() at distance(s): 3
* org.apache.commons.codec.language.DoubleMetaphone2Test.testDoubleMetaphonePrimary() at distance(s): 3
* org.apache.commons.codec.language.DoubleMetaphoneTest.testIsDoubleMetaphoneEqualWithMATCHES() at distance(s): 3
* org.apache.commons.codec.language.DoubleMetaphoneTest.doubleMetaphoneNotEqualTest(boolean) at distance(s): 3, 4
* org.apache.commons.codec.language.DoubleMetaphoneTest.doubleMetaphoneEqualTest(java.lang.String[][],boolean) at distance(s): 3, 4
* org.apache.commons.codec.StringEncoderAbstractTest.testLocaleIndependence() at distance(s): 4
* org.apache.commons.codec.language.DoubleMetaphoneTest.testCCedilla() at distance(s): 4
* org.apache.commons.codec.language.DoubleMetaphoneTest.testNTilde() at distance(s): 4
* org.apache.commons.codec.StringEncoderComparatorTest.testComparatorWithDoubleMetaphone() at distance(s): 10


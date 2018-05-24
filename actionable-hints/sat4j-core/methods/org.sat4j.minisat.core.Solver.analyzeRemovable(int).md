# analyzeRemovable(int)

**Class:** org.sat4j.minisat.core.Solver

[[View code]](https://gitlab.ow2.org/sat4j/sat4j/blob/09e9173e400ea6c1794354ca54c36607c53391ff/org.sat4j.core/src/main/java//org/sat4j/minisat/core/Solver.java#L919)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can not be accessed from other classes. 
It has been covered by 31 test method(s) with a minimum stack distance of 9.

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

* org.sat4j.minisat.constraints.TestXor.twoLargeOppositeParity() at distance(s): 9
* org.sat4j.ModelIteratorTest.testInternalEnumerationOnExampleForRomain() at distance(s): 9
* org.sat4j.minisat.constraints.TestXor.twoOppositeParity() at distance(s): 9
* org.sat4j.ModelIteratorTest.testGlobalTimeoutCounter() at distance(s): 10
* org.sat4j.BugSAT109.testSubModelIterator() at distance(s): 10
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMostOne() at distance(s): 11
* org.sat4j.ModelIteratorTest.testSpecificValues() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testAtMostOne() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesProductEncoding.testAtMostOneWith8Vars() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtLeast2() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtMost2() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactly2() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testAtMostOneWith8Vars() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testExactly2() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtMostOne() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtLeast2() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testExactlyOne() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMost4With11Vars() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMostOneWith8Vars() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testExactlyOne() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testExactlyOne() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactly4With11Vars() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactlyOne() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testAtMostOne() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMost2() at distance(s): 11
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testAtMostOneWith8Vars() at distance(s): 11
* org.sat4j.minisat.core.TestMaxSatDecorator.test() at distance(s): 12
* org.sat4j.tools.TestAllMUSesAndCheckTest.testExample3IJCAICedric() at distance(s): 13, 17, 19
* org.sat4j.tools.TestAllMUSesAndCheckTest.testExample3CADECedric() at distance(s): 13, 17
* org.sat4j.tools.TestAllMUSes.testExample3IJCAICedric() at distance(s): 14, 18, 20
* org.sat4j.tools.TestAllMUSes.testExample3CADECedric() at distance(s): 14, 18


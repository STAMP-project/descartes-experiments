# incActivity(double)

**Class:** org.sat4j.minisat.constraints.cnf.LearntWLClause

[[View code]](https://gitlab.ow2.org/sat4j/sat4j/blob/09e9173e400ea6c1794354ca54c36607c53391ff/org.sat4j.core/src/main/java//org/sat4j/minisat/constraints/cnf/LearntWLClause.java#L94)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 125 test method(s) with a minimum stack distance of 7.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* org.sat4j.minisat.constraints.TestXor.twoLargeOppositeParity() at distance(s): 7
* org.sat4j.BugSAT50.test3() at distance(s): 7
* org.sat4j.ModelIteratorTest.testInternalEnumerationOnExampleForRomain() at distance(s): 7
* org.sat4j.minisat.constraints.TestXor.twoOppositeParity() at distance(s): 7
* org.sat4j.minisat.AbstractM2Test.testJNH14() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH37() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT2() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH9() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH48() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH26() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH49() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi3() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi15() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH15() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT16() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH27() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi1() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT1() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH38() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH16() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT2() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH39() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH50() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT1() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH6() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH23() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH34() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi18() at distance(s): 8
* org.sat4j.ModelIteratorTest.testGlobalTimeoutCounter() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH35() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH12() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH46() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT3() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH7() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH47() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH24() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT4() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi17() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH13() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH8() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH25() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH36() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi16() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH20() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH43() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT12() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT5() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT7() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH4() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT6() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT8() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH21() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi23() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH32() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH10() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH33() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT6() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH44() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH5() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT11() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH45() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH22() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT10() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT7() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH11() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT8() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi5() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testHole7() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH40() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH17() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT15() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH1() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH28() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testHole6() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH41() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT14() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi20() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH29() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT5() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi6() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH18() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH2() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi21() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH30() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT9() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT3() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi4() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50UNSAT4() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testIi11() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH31() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH19() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH42() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testAim50SAT13() at distance(s): 8
* org.sat4j.minisat.AbstractM2Test.testJNH3() at distance(s): 8
* org.sat4j.ModelIteratorTest.testSpecificValues() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testAtMostOne() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesProductEncoding.testAtMostOneWith8Vars() at distance(s): 9
* org.sat4j.AbstractXplainTest.testGlobalInconsistencyIndex() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtLeast2() at distance(s): 9
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistency() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtMost2() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactly2() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testAtMostOneWith8Vars() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testExactly2() at distance(s): 9
* org.sat4j.AbstractXplainTest.testTheCaseOfTwoMUSes() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtMostOne() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtLeast2() at distance(s): 9
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistencyIndex() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testExactlyOne() at distance(s): 9
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistencyIIIndex() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMost4With11Vars() at distance(s): 9
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistencyII() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testExactlyOne() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testExactlyOne() at distance(s): 9
* org.sat4j.BugSAT117ModelIterator.testIt() at distance(s): 9
* org.sat4j.AbstractXplainTest.testGlobalInconsistency() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactly4With11Vars() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testAtMostOne() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMost2() at distance(s): 9
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testAtMostOneWith8Vars() at distance(s): 9
* org.sat4j.minisat.core.TestMaxSatDecorator.test() at distance(s): 10
* org.sat4j.tools.TestAllMUSesAndCheckTest.testExample3IJCAICedric() at distance(s): 11, 17
* org.sat4j.tools.TestAllMUSesAndCheckTest.testExample3CADECedric() at distance(s): 11, 15
* org.sat4j.tools.TestAllMUSes.testExample3IJCAICedric() at distance(s): 12, 18
* org.sat4j.tools.TestAllMUSes.testExample3CADECedric() at distance(s): 12, 16


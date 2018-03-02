# newLearnedClause(org.sat4j.specs.Constr,int)

**Class:** org.sat4j.minisat.restarts.Glucose21Restarts

[[View code]](https://gitlab.ow2.org/sat4j/sat4j/blob/09e9173e400ea6c1794354ca54c36607c53391ff/org.sat4j.core/src/main/java//org/sat4j/minisat/restarts/Glucose21Restarts.java#L73)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 81 test method(s) with a minimum stack distance of 5.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* org.sat4j.minisat.constraints.TestXor.twoLargeOppositeParity() at distance(s): 5
* org.sat4j.ModelIteratorTest.testInnerModelIterator() at distance(s): 5
* org.sat4j.ModelIteratorTest.testInternalEnumerationOnExampleForRomain() at distance(s): 5
* org.sat4j.minisat.constraints.TestXor.twoOppositeParity() at distance(s): 5
* org.sat4j.ModelIteratorTest.testInnerModelIteratorWithOneCard() at distance(s): 5
* org.sat4j.minisat.constraints.TestXor.checkNumberOfSolutionWithCards() at distance(s): 6
* org.sat4j.minisat.core.BugReset.problemTest() at distance(s): 6
* org.sat4j.tools.BackboneTest.testCaseWithUnsatProblem() at distance(s): 6
* org.sat4j.ModelIteratorTest.testInplicantCoverIterator() at distance(s): 6
* org.sat4j.core.JsonReaderTest.testJsonOutput() at distance(s): 6
* org.sat4j.ModelIteratorTest.testGlobalTimeoutCounter() at distance(s): 6
* org.sat4j.minisat.constraints.TestXor.checkNumberOfSolutionWithClauses() at distance(s): 6
* org.sat4j.SingleSolutionTest.testHasNoSingleSolutionUNSAT() at distance(s): 6
* org.sat4j.SingleSolutionTest.testHasNoSingleSolution() at distance(s): 6, 7
* org.sat4j.BugSAT109.testSubModelIterator() at distance(s): 6
* org.sat4j.BugSAT107.testOptimalSolutionfound() at distance(s): 7
* org.sat4j.BugSAT95.testOptimalSolutionWithMinOneIsSatisfiablePlusModel() at distance(s): 7
* org.sat4j.BugSAT107.testNonOptimalSolutionfound() at distance(s): 7
* org.sat4j.SingleSolutionTest.testHasASingleSolution() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMostOne() at distance(s): 7
* org.sat4j.ModelIteratorTest.testSpecificValues() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testAtMostOne() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesProductEncoding.testAtMostOneWith8Vars() at distance(s): 7
* org.sat4j.AbstractXplainTest.testGlobalInconsistencyIndex() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtLeast2() at distance(s): 7
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistency() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtMost2() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactly2() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testAtMostOneWith8Vars() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testExactly2() at distance(s): 7
* org.sat4j.AbstractXplainTest.testTheCaseOfTwoMUSes() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtMostOne() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testAtLeast2() at distance(s): 7
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistencyIndex() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesBinaryEncoding.testExactlyOne() at distance(s): 7
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistencyIIIndex() at distance(s): 7
* org.sat4j.BugSAT107.testNoSolutionfound() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMost4With11Vars() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMostOneWith8Vars() at distance(s): 7
* org.sat4j.AbstractXplainTest.testAlmostGlobalInconsistencyII() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testExactlyOne() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesCommanderEncoding.testExactlyOne() at distance(s): 7
* org.sat4j.AbstractXplainTest.testGlobalInconsistency() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactly4With11Vars() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testExactlyOne() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testAtMostOne() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesSequentialEncoding.testAtMost2() at distance(s): 7
* org.sat4j.tools.TestClausalCardinalitiesLadderEncoding.testAtMostOneWith8Vars() at distance(s): 7
* org.sat4j.BugSAT95.testOptimalSolutionWithMinOneFindModel() at distance(s): 8
* org.sat4j.BugSAT95.testOptimalSolutionWithFullClauseSelectorIsSatisfiablePlusModel() at distance(s): 8
* org.sat4j.tools.BackboneTest.testFilter() at distance(s): 8
* org.sat4j.minisat.core.TestMaxSatDecorator.test() at distance(s): 8
* org.sat4j.BugSAT95.testOptimalSolutionWithFullClauseSelectorFindModel() at distance(s): 9
* org.sat4j.tools.TestAllMUSesAndCheckTest.testExample3IJCAICedric() at distance(s): 9, 10, 13, 15
* org.sat4j.tools.TestAllMUSesAndCheckTest.testSimpleCase() at distance(s): 9, 13
* org.sat4j.tools.TestAllMUSesAndCheckTest.testTheCaseOfTwoMUSes() at distance(s): 9, 10, 13, 15
* org.sat4j.tools.TestAllMUSesAndCheckTest.testExample3CADECedric() at distance(s): 9, 10, 13
* org.sat4j.tools.TestAllMUSesGroupTest.testSimpleCaseWithGroups4() at distance(s): 10
* org.sat4j.tools.TestAllMUSes.testExample3IJCAICedric() at distance(s): 10, 14, 16
* org.sat4j.tools.TestAllMUSesAndCheckTest.testAlmostGlobalInconsistency() at distance(s): 10, 15
* org.sat4j.tools.TestAllMUSesGroupTest.testSimpleCase() at distance(s): 10, 14
* org.sat4j.tools.TestAllMUSesAndCheckTest.testGlobalInconsistencyIndex() at distance(s): 10, 15
* org.sat4j.tools.TestAllMUSes.testExample3CADECedric() at distance(s): 10, 14
* org.sat4j.tools.TestAllMUSesAndCheckTest.testAlmostGlobalInconsistencyIndex() at distance(s): 10, 15
* org.sat4j.tools.TestAllMUSesAndCheckTest.testAlmostGlobalInconsistencyII() at distance(s): 10, 15
* org.sat4j.tools.TestAllMUSes.testSimpleCase() at distance(s): 10, 14
* org.sat4j.tools.TestAllMUSes.testTheCaseOfTwoMUSes() at distance(s): 10, 14, 16
* org.sat4j.tools.TestAllMUSesAndCheckTest.testAlmostGlobalInconsistencyIIIndex() at distance(s): 10, 15
* org.sat4j.tools.TestAllMUSesAndCheckTest.testGlobalInconsistency() at distance(s): 10, 15
* org.sat4j.minisat.core.Bug275101.testMaxSAtIteratorIfSat() at distance(s): 11
* org.sat4j.minisat.core.Bug275101.testMaxSAtIterator() at distance(s): 11
* org.sat4j.tools.TestAllMUSesAndCheckTest.testExample1CADECedric() at distance(s): 13
* org.sat4j.tools.TestAllMSSes.testSimpleCasePermut() at distance(s): 14
* org.sat4j.tools.TestAllMUSes.testExample1CADECedric() at distance(s): 14
* org.sat4j.tools.TestAllMUSesGroupTest.testSimpleCaseWithGroups() at distance(s): 14
* org.sat4j.tools.TestAllMUSes.testGlobalInconsistency() at distance(s): 16
* org.sat4j.tools.TestAllMUSes.testAlmostGlobalInconsistency() at distance(s): 16
* org.sat4j.tools.TestAllMUSes.testAlmostGlobalInconsistencyII() at distance(s): 16
* org.sat4j.tools.TestAllMUSes.testGlobalInconsistencyIndex() at distance(s): 16
* org.sat4j.tools.TestAllMUSes.testAlmostGlobalInconsistencyIndex() at distance(s): 16
* org.sat4j.tools.TestAllMUSes.testAlmostGlobalInconsistencyIIIndex() at distance(s): 16


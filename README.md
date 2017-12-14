# Descartes Experiments

This is an open-science repository that contains the output obtained from
executing [PITest](http://pitest.org) with a different mutation engine named
[Descartes](https://github.com/STAMP-project/pitest-descartes) that implements [exterme mutation](http://dl.acm.org/citation.cfm?doid=2896941.2896944) operators.

The repository contains a folder for each project studied. Each folder contains
a set of markdown files. One of them contains a summary and there is one file
devoted to each method analyzed. 

The summary file for each project classifies the analyzed methods in **strong 
pseudo tested** and **weak pseudo-tested**. A **strong pseudo-tested** method
is such that no extreme mutant applied was detected by the test suite. On the 
other hand, a **weak psuedo-tested** method would have both, detected and 
non-detected extreme mutants.

For each method, the folder contains a file that includes the tests
covering the method, the minimum stack distance from each test to the method
the mutants applied and whether those mutants were detected or not.

There are also two sections in which developers can give us feedback and even
include some commits that might be related and influenced by the given output.


## Projects

| Project                                   | Commit                                     |
|-------------------------------------------|--------------------------------------------|
| [Apache Flink Core](/flink-core/index.md) | [740f711c4ec9c4b7cdefd01c9f64857c345a68a1](https://github.com/apache/flink/tree/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core) |
| [SAT4J Core](/org.sat4j.core/index.md)    |  53b9d4dc175caf8c829a958e21ea221bf0bf3b2b  |

## Selected methods

We have selected 5 methods by project and they have been exposed in the 
[`selected-methods` folder](./selected-methods). Thy is selection has been made
in a way that there is at least a method covered directly by a test, a method,
covered indirectly, a strong and a weak pseudo tested method, a method covered
by only one test case, a method covered by more than one test case and a method
covered by a considerable number (with respect to other methods, trying to reach
more than 100 test cases if possible) of test cases.

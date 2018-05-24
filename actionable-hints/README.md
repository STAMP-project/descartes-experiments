# Actionable Hints

This folder contains a set of human-readable reports on a curated set of 
findings made using extreme mutation techniques. The main purpose of these
reports is to exchange with developers. The information of the extreme mutation
results has been augmented with data that includes, for example, the stack
distance between the mutated method and each test case. All data has been 
structure so it can be useful for developers to understand the issues and be 
able to take actions on them.

For each project there is a folder that contains a set of markdown files. 
One of these files is a project summary. Each of the rest files are devoted to 
describe the methods we have found to have potential testing issues.

Each method has been classified as **pseudo-tested** or **partially-tested**. 
A **pseudo-tested** method is one for which no extreme mutation has been detected.
A **partially-tested** method has mixed results, only some transformations were
detected.

For each method, the folder contains a file that includes the tests
covering the method, the minimum stack distance from each test to the method
the mutants applied and whether those mutants were detected or not.

Some additional information about how these methods are covered by the test
suite is provided [here](interplay_report/index.md).

## Projects

* [JOpt Simple](jopt-simple/index.md)
* [Apache Commons Cli](commons-cli/index.md)
* [SAT4J Core](sat4j-core/index.md)
* [Apache Flink Core](flink-core/index.md)
* [Spoon](spoon/index.md)
* [AuthzForce Core PDP Engine](authzforce-core/index.md)
* [Apache Commons Codec](commons-codec/index.md)
* [Apache Commons Collections](commons-collections/index.md)
* [XWiki Commons - Velocity](xwiki-commons-velocity/index.md)
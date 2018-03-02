# Descartes Experiments

This is an open-science repository that contains the output obtained from
executing [PITest](http://pitest.org) with a different mutation engine named
[Descartes](https://github.com/STAMP-project/pitest-descartes) that implements [exterme mutation](http://dl.acm.org/citation.cfm?doid=2896941.2896944) operators.

The repository contains a folder for each project studied. Each folder contains
a set of markdown files. One of them contain a summary and there is one file
devoted to each method spotted with a potential testing issue. 


Each method has been classified as ***pseudo-tested** or **partially-tested**. 
A **pseudo-tested** method is one for wich no extreme mutation has been detected.
A **partially-tested** method has mixed results, only some transformations were
detected.

For each method, the folder contains a file that includes the tests
covering the method, the minimum stack distance from each test to the method
the mutants applied and whether those mutants were detected or not.

Some additional information about how these methods are covered by the test
suite is provied [here](interplay_report/index.md).


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
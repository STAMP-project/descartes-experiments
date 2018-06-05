- [X] [org.sat4j.reader.LecteurDimacs.ajouterClauses(char)](methods/org.sat4j.reader.LecteurDimacs.ajouterClauses(char).md)
    > Relevant as it adds constraints to a problem instance loaded from a file.

- [ ] [org.sat4j.tools.encoding.Policy.setAtMostOneEncoding(org.sat4j.tools.encoding.EncodingStrategy)](methods/org.sat4j.tools.encoding.Policy.setAtMostOneEncoding(org.sat4j.tools.encoding.EncodingStrategy).md)
- [ ] [org.sat4j.reader.LecteurDimacs.checkFormat()](methods/org.sat4j.reader.LecteurDimacs.checkFormat().md)
    > It verifies if the problem specification has the right prefix. It is not so relevant but a test case of a malformed problem is missing at the moment.

- [X] [org.sat4j.core.VecInt.shrink(int)](methods/org.sat4j.core.VecInt.shrink(int).md)
    > It is a very simple method but the class is widely used in the code base and external projects.

- [ ] [org.sat4j.minisat.constraints.cnf.UnitClause.get(int)](methods/org.sat4j.minisat.constraints.cnf.UnitClause.get(int).md)
    > The first legal values that can be returned start at 2. The return values are positions in internal arrays with empty values.

- [X] [org.sat4j.tools.Backbone$Backboner.removeVarNotPresentAndSatisfiedLits(int[],org.sat4j.specs.IVecInt,int)](methods/org.sat4j.tools.Backbone$Backboner.removeVarNotPresentAndSatisfiedLits(int[],org.sat4j.specs.IVecInt,int).md)
    > The method performs a simplification (optimization). It requires a test to check that the simplification has been done. It is a feature that is not widely used but yet important.

- [ ] [org.sat4j.minisat.core.LBDConflictTimer.reset()](methods/org.sat4j.minisat.core.LBDConflictTimer.reset().md)
    > One could only see the effects if you are using the instance twice and reset. There are contexts where this method could be important but it is not so relevant.
 
- [ ] [org.sat4j.minisat.core.LBDConflictTimer.run()](methods/org.sat4j.minisat.core.LBDConflictTimer.run().md)
    > The effects are hard to observe. More tests actually are needed but, since tt doesn't make the solver incorrect, it is not a priority.

- [ ] [org.sat4j.tools.AbstractClauseSelectorSolver.externalState()](methods/org.sat4j.tools.AbstractClauseSelectorSolver.externalState().md)
    > Very simple code. If nothing is done, the default value is the same being assigned there.

- [ ] [org.sat4j.minisat.core.Counter.inc()](methods/org.sat4j.minisat.core.Counter.inc().md)
- [ ] [org.sat4j.minisat.learning.LimitedLearning.init()](methods/org.sat4j.minisat.learning.LimitedLearning.init().md)
- [ ] [org.sat4j.minisat.restarts.MiniSATRestarts.onBackjumpToRootLevel()](methods/org.sat4j.minisat.restarts.MiniSATRestarts.onBackjumpToRootLevel().md)
- [ ] [org.sat4j.tools.ManyCore.isVerbose()](methods/org.sat4j.tools.ManyCore.isVerbose().md)
- [ ] [org.sat4j.tools.TextOutputTracing.learn(org.sat4j.specs.IConstr)](methods/org.sat4j.tools.TextOutputTracing.learn(org.sat4j.specs.IConstr).md)
- [ ] [org.sat4j.tools.TextOutputTracing.propagating(int)](methods/org.sat4j.tools.TextOutputTracing.propagating(int).md)
- [X] [org.sat4j.minisat.constraints.cnf.WLClause.remove(org.sat4j.specs.UnitPropagationListener)](methods/org.sat4j.minisat.constraints.cnf.WLClause.remove(org.sat4j.specs.UnitPropagationListener).md)
    > Given the role of the class to the project this is a more interesting case. It requires more elaborated tests to observe what's happening.

- [ ] [org.sat4j.core.VecInt.unsafeGet(int)](methods/org.sat4j.core.VecInt.unsafeGet(int).md)
    > Same as a case, before, this class is widely used, so it should be better tested.
    
- [ ] [org.sat4j.minisat.core.GlucoseLCDS.computeLBD(org.sat4j.specs.Constr)](methods/org.sat4j.minisat.core.GlucoseLCDS.computeLBD(org.sat4j.specs.Constr).md)
- [ ] [org.sat4j.minisat.orders.RSATPhaseSelectionStrategy.assignLiteral(int)](methods/org.sat4j.minisat.orders.RSATPhaseSelectionStrategy.assignLiteral(int).md)
- [ ] [org.sat4j.minisat.restarts.LubyRestarts.onRestart()](methods/org.sat4j.minisat.restarts.LubyRestarts.onRestart().md)
- [ ] [org.sat4j.minisat.orders.PhaseCachingAutoEraseStrategy.assignLiteral(int)](methods/org.sat4j.minisat.orders.PhaseCachingAutoEraseStrategy.assignLiteral(int).md)
- [X] [org.sat4j.tools.Backbone.bb()](methods/org.sat4j.tools.Backbone.bb().md)
    > Despite of being a very simple method, it gives access to an instance of an object that is widely used.

- [ ] [org.sat4j.minisat.core.Solver.decayActivities()](methods/org.sat4j.minisat.core.Solver.decayActivities().md)
- [ ] [org.sat4j.minisat.restarts.MiniSATRestarts.newConflict()](methods/org.sat4j.minisat.restarts.MiniSATRestarts.newConflict().md)
- [ ] [org.sat4j.tools.encoding.Policy.setExactlyOneEncoding(org.sat4j.tools.encoding.EncodingStrategy)](methods/org.sat4j.tools.encoding.Policy.setExactlyOneEncoding(org.sat4j.tools.encoding.EncodingStrategy).md)
- [ ] [org.sat4j.minisat.core.Solver.printLearntClausesInfos(java.io.PrintWriter,java.lang.String)](methods/org.sat4j.minisat.core.Solver.printLearntClausesInfos(java.io.PrintWriter,java.lang.String).md)
- [ ] [org.sat4j.reader.DimacsReader.readConstrs()](methods/org.sat4j.reader.DimacsReader.readConstrs().md)
- [ ] [org.sat4j.tools.encoding.Policy.getAdapterFromEncodingName(org.sat4j.tools.encoding.EncodingStrategy)](methods/org.sat4j.tools.encoding.Policy.getAdapterFromEncodingName(org.sat4j.tools.encoding.EncodingStrategy).md)
- [ ] [org.sat4j.minisat.orders.VarOrderHeap.varDecayActivity()](methods/org.sat4j.minisat.orders.VarOrderHeap.varDecayActivity().md)
- [X] [org.sat4j.tools.GateTranslator.gateTrue(int)](methods/org.sat4j.tools.GateTranslator.gateTrue(int).md)
    > The context in which this method is used in the test cases makes it return always null. Different tests are needed.

- [ ] [org.sat4j.tools.TextOutputTracing.learnUnit(int)](methods/org.sat4j.tools.TextOutputTracing.learnUnit(int).md)
- [X] [org.sat4j.tools.ModelIterator.reset()](methods/org.sat4j.tools.ModelIterator.reset().md)
    > Important in some use cases provided by external clients.

- [ ] [org.sat4j.core.Vec.isEmpty()](methods/org.sat4j.core.Vec.isEmpty().md)
- [X] [org.sat4j.tools.GateTranslator.or(int,org.sat4j.specs.IVecInt)](methods/org.sat4j.tools.GateTranslator.or(int,org.sat4j.specs.IVecInt).md)
    > Similar case to the other gate above.

- [ ] [org.sat4j.tools.SearchEnumeratorListener.end(org.sat4j.specs.Lbool)](methods/org.sat4j.tools.SearchEnumeratorListener.end(org.sat4j.specs.Lbool).md)

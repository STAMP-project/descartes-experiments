# visitCtBreak(spoon.reflect.code.CtBreak)

**Class:** spoon.reflect.visitor.CtScanner

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/CtScanner.java#L304)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 58 test method(s) with a minimum stack distance of 34.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.condition.ConditionalTest.testBlockInConditionAndLoop() at distance(s): 34, 70
* spoon.test.condition.ConditionalTest.testNoBlockInConditionAndLoop() at distance(s): 34, 70
* spoon.test.processing.ProcessingTest.testInsertEnd() at distance(s): 35, 41, 64, 70
* spoon.test.processing.ProcessingTest.testInsertBegin() at distance(s): 35, 41, 64, 70
* spoon.test.filters.FilterTest.testLineFilter() at distance(s): 35, 65
* spoon.test.model.SwitchCaseTest.testSwitchStatementOnAString() at distance(s): 35, 64
* spoon.test.model.SwitchCaseTest.testIterationStatements() at distance(s): 35
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 37, 64, 70, 73, 75, 80, 81, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 97, 100
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 39, 40, 90, 91, 107, 108, 125, 126, 130, 131, 142, 143, 147, 148
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 39, 40, 69, 70, 71, 72, 75, 76, 80, 81, 82, 85, 86, 87, 92, 93, 96, 97, 102, 103, 161, 162, 163, 164, 171, 172, 173, 174
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 39, 40, 58, 59, 64, 65, 69, 70, 71, 74, 75, 76, 80, 81, 82, 85, 86, 87, 90, 91, 92, 93, 95, 96, 97, 101, 102, 103, 107, 108, 112, 113, 122, 123, 125, 126, 130, 131, 142, 143, 147, 148, 164, 165, 166, 167, 174, 175, 176, 177
* spoon.test.query_function.VariableReferencesTest.testVariableScopeFunction() at distance(s): 39, 40, 64, 67, 68, 70, 71
* spoon.test.prettyprinter.PrinterTest.testFQNModeWriteFQNConstructorInCtVisitor() at distance(s): 39, 80, 89
* spoon.test.query_function.VariableReferencesTest.testCatchVariableReferenceFunction() at distance(s): 39, 40, 80, 81
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 39, 40, 124, 125, 126, 127, 134, 135, 136, 137
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 39, 40, 64, 65, 68, 80, 81, 82, 90, 91, 107, 108, 125, 126, 130, 131, 142, 143, 147, 148
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 40, 76, 78
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testStaticClasses() at distance(s): 41, 62, 63, 64, 68, 70, 74, 75, 76, 79, 80, 81, 85, 86, 87, 90, 91, 92, 96, 97, 101, 102, 107, 108, 113, 118
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 48, 72, 75, 78, 80, 84, 85, 88, 90
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 49, 75
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath() at distance(s): 51, 57, 59, 62, 68, 70, 133, 134, 135, 142, 143, 144, 145, 146, 153, 154, 155
* spoon.generating.ReplacementVisitorGenerator.process(spoon.reflect.declaration.CtType) at distance(s): 52
* spoon.test.reference.VariableAccessTest.testReferenceToLocalVariableDeclaredInLoop() at distance(s): 60, 80
* spoon.reflect.ast.AstCheckerTest.testPushToStackChanges() at distance(s): 61, 66, 70, 80, 84, 86, 91, 107
* spoon.test.parameters.ParameterTest.testParameterInNoClasspath() at distance(s): 62, 73, 85, 92, 94, 103, 105, 115, 117, 118, 148, 150
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 63, 64, 65, 66, 69, 70, 71, 72, 74, 76, 136, 138, 152, 154, 185, 187, 218, 220, 229, 231, 240, 242, 251, 253, 262, 264, 273, 275, 284, 286
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 63, 64, 69, 70, 74, 75, 76, 80, 81, 85, 86, 91, 92, 98, 103, 107, 109, 113, 114, 120
* spoon.test.architecture.SpoonArchitectureEnforcerTest.noTreeSetInSpoon() at distance(s): 64, 68, 70, 75, 79, 80, 81, 85, 86, 91, 96
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testSpecPackage() at distance(s): 64, 68, 70, 75, 79, 80, 81, 85, 86, 91, 96
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 64, 70, 80, 81, 86, 91, 96
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 64, 66, 68, 70, 72, 75, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 91, 93, 96, 98
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 64, 66, 75, 77, 80, 82, 85, 86, 87, 88, 91, 93
* spoon.test.query_function.VariableReferencesTest.setup() at distance(s): 64, 65
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 65, 67, 69, 76, 78, 81, 83, 86, 87, 88, 89, 92, 94
* spoon.test.ctCase.SwitchCaseTest.insertAfterStatementInSwitchCaseWithoutException() at distance(s): 65, 67
* spoon.test.reference.TypeReferenceTest.testInvocationWithFieldAccessInNoClasspath() at distance(s): 65
* spoon.test.ctCase.SwitchCaseTest.insertBeforeStatementInSwitchCaseWithoutException() at distance(s): 65, 67
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 66, 70, 72, 75, 77, 79, 81, 82, 83, 86, 87, 88, 90, 91, 92, 93, 96, 97, 98, 102, 107
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 67, 73, 83, 84, 89, 94, 99
* spoon.test.api.APITest.testPrintNotAllSourcesWithFilter() at distance(s): 69, 78, 80, 89
* spoon.test.api.APITest.testPrintNotAllSourcesWithNames() at distance(s): 69, 78, 80, 89
* spoon.test.labels.TestLabels.testLabelsAreDetected() at distance(s): 70, 75, 76, 81, 86, 92, 98, 103, 109, 114, 120
* spoon.test.condition.ConditionalTest.testConditionalWithAssignment() at distance(s): 70
* spoon.test.visibility.VisibilityTest.testInvocationVisibilityInFieldDeclaration() at distance(s): 70, 102, 113
* spoon.test.condition.ConditionalTest.testConditional() at distance(s): 70
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 71, 91, 97, 102, 148, 149, 154, 155, 164, 165
* spoon.test.compilation.CompilationTest.testFilterResourcesDir() at distance(s): 74, 82
* spoon.test.reference.TypeReferenceTest.testToStringEqualityBetweenTwoGenericTypeDifferent() at distance(s): 75
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 78, 81, 84, 87, 89, 90, 92, 96, 101
* spoon.reflect.visitor.CtVisitorTest.testMethodsInVisitor() at distance(s): 78, 81, 84, 87, 89, 92
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 78, 81, 84, 87, 89, 90, 92, 96, 101
* spoon.reflect.visitor.CtInheritanceScannerMethodsTest.testMethodsInInheritanceScanner() at distance(s): 78, 81, 84, 87, 89, 92
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 80, 81, 86, 87, 91, 92, 97
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 80, 86, 88, 91, 94, 99
* spoon.test.SpoonTestHelpers.getAllInstantiableMetamodelInterfaces() at distance(s): 80, 86, 91
* spoon.reflect.visitor.CtScannerTest.testScannerContract() at distance(s): 80, 86, 91
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(java.io.File) at distance(s): 81, 87, 92
* spoon.reflect.ast.CloneTest.testCloneMethodsDeclaredInAST() at distance(s): 81, 87, 92, 106, 112, 117


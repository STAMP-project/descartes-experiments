# visitCtContinue(spoon.reflect.code.CtContinue)

**Class:** spoon.reflect.visitor.CtScanner

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/CtScanner.java#L372)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 38 test method(s) with a minimum stack distance of 37.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 37, 74, 80, 83, 86, 89, 91, 97, 100
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameAllLocalVariablesOfRenameTestSubject() at distance(s): 44, 55, 77, 79, 86, 88, 90, 94, 96, 97, 99, 103, 104, 105, 106, 111, 113, 115, 117, 120, 121, 122, 124, 126, 128, 129, 130, 131, 132, 133, 137, 138, 139, 140, 141, 142, 143, 144, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 237, 240
* spoon.test.literal.LiteralTest.testCharLiteralInNoClasspath() at distance(s): 51, 77, 81, 83, 85
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testStaticClasses() at distance(s): 51, 62, 68, 74, 79, 80, 85, 86, 90, 91, 96, 97, 101, 102, 107, 108, 113, 124
* spoon.test.parameters.ParameterTest.testParameterInNoClasspath() at distance(s): 51, 81, 83
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 60, 71, 91, 102, 154, 155, 165, 166
* spoon.reflect.ast.AstCheckerTest.testPushToStackChanges() at distance(s): 61, 70, 80, 91
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 63, 65, 69, 71, 74, 76, 85, 86, 87, 88, 91, 93, 185, 187
* spoon.test.architecture.SpoonArchitectureEnforcerTest.noTreeSetInSpoon() at distance(s): 68, 74, 79, 80, 85, 91, 102
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testSpecPackage() at distance(s): 68, 74, 79, 80, 85, 91, 102
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 68, 70, 74, 76, 79, 80, 81, 82, 85, 87, 91, 93, 102, 104
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 68, 74, 79, 80, 85, 86, 91, 95, 96, 97, 101, 102, 106, 108, 112, 113, 114, 119, 120
* spoon.test.api.APITest.testPrintNotAllSourcesWithFilter() at distance(s): 69, 78, 80, 89
* spoon.test.api.APITest.testPrintNotAllSourcesWithNames() at distance(s): 69, 78, 80, 89
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 70, 76, 79, 81, 82, 85, 87, 90, 91, 93, 96, 102, 104, 113
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 74, 80, 85, 91, 102
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 74, 76, 80, 82, 91, 93
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 75, 77, 81, 83
* spoon.test.reference.TypeReferenceTest.testInvocationWithFieldAccessInNoClasspath() at distance(s): 75, 86, 97
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 77, 83, 88, 94, 105
* spoon.test.refactoring.RefactoringTest.testTransformedInstanceofAfterATransformation() at distance(s): 78, 81, 83, 89, 92, 94, 139, 146, 149, 152, 155, 159, 162, 165, 168, 175, 178
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 78, 81, 89, 90, 92, 101
* spoon.reflect.visitor.CtVisitorTest.testMethodsInVisitor() at distance(s): 78, 81, 89, 92
* spoon.test.refactoring.RefactoringTest.testRefactoringClassChangeAllCtTypeReferenceAssociatedWithClassConcerned() at distance(s): 78, 81, 82, 83, 89, 92, 93, 94, 137, 139, 144, 146, 147, 148, 149, 152, 153, 155, 158, 159, 160, 162, 163, 164, 165, 168, 171, 174, 175, 178
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 78, 81, 89, 90, 92, 101
* spoon.reflect.visitor.CtInheritanceScannerMethodsTest.testMethodsInInheritanceScanner() at distance(s): 78, 81, 89, 92
* spoon.test.refactoring.RefactoringTest.testThisInConstructorAfterATransformation() at distance(s): 78, 81, 83, 89, 92, 94, 139, 146, 149, 152, 155, 159, 162, 165, 168, 175, 178
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 80, 86, 91, 97
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 80, 88, 91, 99
* spoon.test.SpoonTestHelpers.getAllInstantiableMetamodelInterfaces() at distance(s): 80, 91
* spoon.reflect.visitor.CtScannerTest.testScannerContract() at distance(s): 80, 91
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(java.io.File) at distance(s): 81, 92
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRenameLocalVariableToSameName() at distance(s): 81, 92
* spoon.test.refactoring.CtRenameLocalVariableRefactoringTest.testRefactorWrongUsage() at distance(s): 81, 92
* spoon.test.refactoring.RefactoringTest.testThisInConstructor() at distance(s): 81, 83, 92, 94, 137, 144, 147, 148, 153, 155, 158, 160, 163, 164, 171, 174
* spoon.reflect.ast.CloneTest.testCloneMethodsDeclaredInAST() at distance(s): 81, 92, 106, 117
* spoon.test.refactoring.ThisTransformationProcessor.process(spoon.reflect.declaration.CtClass) at distance(s): 83, 94
* spoon.test.labels.TestLabels.testLabelsAreDetected() at distance(s): 114, 120


# visitCtComment(spoon.reflect.code.CtComment)

**Class:** spoon.reflect.visitor.CtScanner

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/CtScanner.java#L885)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 35 test method(s) with a minimum stack distance of 15.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 15, 21, 26, 32, 35, 39, 42, 45, 48, 50, 51, 53, 56, 57, 59, 62, 67, 68, 70, 79
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 15, 21, 26, 27, 39, 42, 45, 48, 50, 51, 53, 56, 57, 59, 62, 63, 67, 68, 70, 79
* spoon.test.template.TemplateTest.testTemplateInheritance() at distance(s): 17, 19, 21, 24, 28, 30, 32, 35, 36, 38, 39, 41, 42, 43, 45, 46, 58, 69, 80, 86
* spoon.test.comment.CommentTest.testInLineComment() at distance(s): 18, 24, 29, 30, 35, 40, 41, 44, 45, 46, 47, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testCommentsInComment1And2() at distance(s): 18, 24, 41, 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testBlockComment() at distance(s): 18, 24, 29, 30, 35, 40, 41, 44, 46, 47, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.generating.CtBiScannerGenerator.process() at distance(s): 19
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 21, 27, 32, 33, 38, 41, 43, 47, 48, 49, 50, 52, 53, 56, 58, 59, 61, 62, 64, 65, 67, 68, 69, 70, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 95, 96, 97, 98, 100, 101, 102, 103, 105, 106, 108, 109, 111, 112, 113, 114, 117, 119, 120, 122, 123, 124, 125, 128, 129, 130, 133, 135, 136, 138, 139, 141, 144, 146, 152, 155, 157, 163, 166
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 21, 26, 39, 42, 45, 48, 50, 51, 53, 54, 56, 57, 59, 62, 63, 65, 67, 68, 70, 71, 73, 74, 76, 79, 80, 82, 84, 85, 87, 90, 91, 93, 94, 95, 96, 97, 98, 102, 106, 107
* spoon.test.module.TestModule.testModuleInfoWithComments() at distance(s): 21
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 23, 34, 40, 45, 51, 74, 85, 91, 96, 102, 106, 108, 111, 113, 114, 119, 123, 124, 125, 126, 128, 131, 132, 136, 137, 139, 141, 142, 143, 144, 148, 149, 153, 154, 156, 159, 161
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceFunction() at distance(s): 23, 34, 40, 45, 51, 53, 59, 64, 65, 66, 69, 70, 75, 76, 77, 80, 81, 82, 86, 87, 91, 92, 93, 97, 98, 102, 103, 104, 108, 114, 142, 143, 144, 155, 156, 157, 162, 163, 164, 166, 167, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 179, 183, 184, 185
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 23, 34, 40, 42, 45, 48, 51, 53, 59, 64, 65, 69, 70, 74, 75, 76, 77, 79, 80, 81, 82, 85, 86, 87, 90, 91, 92, 93, 96, 97, 98, 101, 102, 103, 104, 106, 107, 108, 111, 113, 114, 117, 118, 119, 123, 124, 125, 126, 128, 131, 132, 134, 136, 137, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 153, 154, 156, 158, 159, 160, 161, 165, 166, 167, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 186, 187, 188
* spoon.test.query_function.VariableReferencesTest.testVariableScopeFunction() at distance(s): 23, 34, 40, 45, 51, 62, 65, 70, 73, 76
* spoon.test.query_function.VariableReferencesTest.testCatchVariableReferenceFunction() at distance(s): 23, 34, 40, 45, 51, 64, 74, 75, 81, 86, 92
* spoon.test.query_function.VariableReferencesTest.testLocalVariableReferenceDeclarationFunction() at distance(s): 23, 34, 40, 45, 51, 105, 106, 107, 118, 119, 120, 125, 126, 127, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 146, 147, 148
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 23, 34, 40, 45, 48, 51, 59, 64, 65, 70, 74, 75, 76, 81, 82, 85, 86, 87, 91, 92, 93, 96, 102, 106, 108, 111, 113, 114, 119, 123, 124, 125, 126, 128, 131, 132, 136, 137, 139, 141, 142, 143, 144, 148, 149, 153, 154, 156, 159, 161
* spoon.test.ctType.CtTypeTest.testIsSubTypeOfonTypeReferences() at distance(s): 26, 47, 64
* spoon.test.interfaces.TestInterfaceWithoutSetup.testInterfacePrettyPrinting() at distance(s): 27, 29, 36, 38, 43, 48
* spoon.test.comment.CommentTest.testSnippedWithComments() at distance(s): 32, 49
* spoon.test.arrays.ArraysTest.testCtNewArrayWitComments() at distance(s): 35, 37, 64, 66, 69, 76
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 39, 42, 45, 48, 50, 51, 53, 54, 56, 57, 59, 62, 63, 65, 68, 71, 73, 74, 76, 79, 80, 82, 84, 85, 87, 90, 91, 93, 94, 95, 96, 97, 98, 102, 106, 107
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(java.io.File) at distance(s): 42, 48, 53, 54, 59, 65, 71, 76, 82, 87, 93, 97, 98
* spoon.test.comment.CommentTest.testCombinedPackageInfoComment() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testCodeFactory() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testJavaDocCommentOnUnix() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testJavaDocEmptyCommentAndTag() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testInsertNewComment() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testWildComments() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.comment.CommentTest.testRemoveComment() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 44, 50, 55, 56, 61, 67, 73, 78, 84, 89, 95, 99, 100
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 44, 52, 55, 58, 61, 63, 64, 66, 69, 75, 77, 80, 81, 86, 92, 97, 103, 107, 108, 126, 127, 132, 133, 137, 138, 139, 140, 143, 144, 148, 149, 150, 152, 153, 159, 160, 161, 162, 163, 166, 167, 170, 171, 172, 173, 174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185
* spoon.test.comment.CommentTest.testCoreFactory() at distance(s): 44, 46, 50, 52, 56, 58, 61, 62, 63, 64, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84
* spoon.test.pkg.PackageTest.testPrintPackageInfoWhenNothingInPackage() at distance(s): 48, 50
* spoon.test.query_function.VariableReferencesTest.setup() at distance(s): 48, 59, 65, 70, 76


# visitCtTypeAccess(spoon.reflect.code.CtTypeAccess)

**Class:** spoon.reflect.visitor.CtBiScannerDefault

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/reflect/visitor/CtBiScannerDefault.java#L729)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 66 test method(s) with a minimum stack distance of 9.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessDeclaredInADefaultClass() at distance(s): 9
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 9, 14
* spoon.testing.CtElementAssertTest.testEqualityBetweenTwoDifferentCtElement() at distance(s): 10
* spoon.test.signature.SignatureTest.testLiteralSignature() at distance(s): 13
* spoon.test.ctBlock.TestCtBlock.testAddStatementInCase() at distance(s): 17
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureWithVariableAccess() at distance(s): 17
* spoon.test.fieldaccesses.FieldAccessTest.testIncrementationOnAVarIsAUnaryOperator() at distance(s): 17
* spoon.test.template.TemplateTest.testTemplateMatcher() at distance(s): 22, 24, 25, 26, 28, 48, 52, 53, 54, 55, 56, 57
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 46, 47, 48
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 24, 25, 26, 27, 28, 29, 30, 31, 46, 47
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnParameterInMethod() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 47
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnLocalVariableInMethod() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 47, 48
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInNewInstance() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 47
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInStatements() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 46, 48
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 33, 48, 50
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationBeforeExceptionInSignatureOfMethod() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 33, 48
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInClassDeclaration() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 33, 47, 48
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessor() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 48, 49
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testTernaryParenthesesOnLocalVariable() at distance(s): 25
* spoon.test.annotation.AnnotationTest.testUsageOfParametersInTypeAnnotation() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 47, 48
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInReturnTypeInMethod() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 47
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessorWithGlobalAnnotation() at distance(s): 25, 27
* spoon.test.annotation.AnnotationTest.testAnnotatedElementTypes() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 47, 48
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInCast() at distance(s): 25, 26, 27, 28, 29, 30, 31, 48
* spoon.test.template.TemplateTest.testTemplateMatcherMatchTwoSnippets() at distance(s): 25, 27, 86, 88, 90, 92
* spoon.test.template.TemplateTest.testTemplateMatcherWithWholePackage() at distance(s): 25, 27, 86, 88
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInExtendsImplementsOfAClass() at distance(s): 25, 26, 27, 28, 29, 30, 31, 32, 49
* spoon.test.ctBlock.TestCtBlock.testAddStatementInBlock() at distance(s): 26
* spoon.test.constructor.ConstructorTest.setUp() at distance(s): 26, 27, 28, 30
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 27, 36, 40, 41, 52
* spoon.test.constructor.ConstructorTest.testTransformationOnConstructorWithInsertBegin() at distance(s): 27, 28, 29, 30
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner() at distance(s): 28, 29, 36, 37, 41
* spoon.test.type.TypeTest.testTypeAccessOfArrayObjectInFullyQualifiedName() at distance(s): 28
* spoon.test.type.TypeTest.testTypeAccessForTypeAccessInInstanceOf() at distance(s): 28
* spoon.test.type.TypeTest.testIntersectionTypeReferenceInGenericsAndCasts() at distance(s): 28
* spoon.test.type.TypeTest.testTypeReferenceInGenericsAndCasts() at distance(s): 28
* spoon.test.parent.SetParentTest.testContract() at distance(s): 28, 32
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor() at distance(s): 28, 32, 37, 41
* spoon.test.type.TypeTest.testTypeAccessForDotClass() at distance(s): 28
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 28, 32, 36, 37, 41, 45, 46, 49, 54, 58, 63
* spoon.test.api.MetamodelTest.testGetAllMetamodelInterfacess() at distance(s): 29, 33, 36, 40
* spoon.reflect.ast.CloneTest.testCloneListener() at distance(s): 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 33, 37
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 34, 37, 38, 41
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testStaticClasses() at distance(s): 36, 40
* spoon.test.architecture.SpoonArchitectureEnforcerTest.noTreeSetInSpoon() at distance(s): 36, 40
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 36, 40
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testSpecPackage() at distance(s): 36, 40
* spoon.test.api.MetamodelTest.testGetterSetterFroRole() at distance(s): 36, 40
* spoon.test.intercession.IntercessionContractTest.data() at distance(s): 36, 40
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 36, 40
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 36, 40, 63, 65, 68, 69, 73, 74, 75, 78, 79, 80, 81, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 106, 107, 108, 112, 113, 115, 119, 124, 125, 126, 127, 129, 130, 135, 139, 146, 151, 157, 168, 179, 180, 191, 202
* spoon.test.architecture.SpoonArchitectureEnforcerTest.metamodelPackageRule() at distance(s): 36, 40, 44, 45, 48, 49, 52
* spoon.test.SpoonTestHelpers.getAllInstantiableMetamodelInterfaces() at distance(s): 36, 40
* spoon.reflect.visitor.CtScannerTest.testScannerContract() at distance(s): 36, 40
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(java.io.File) at distance(s): 37, 41
* spoon.reflect.visitor.CtVisitorTest.testMethodsInVisitor() at distance(s): 37, 41
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 37, 41
* spoon.test.imports.ImportTest.testSortingOfImports() at distance(s): 37, 41
* spoon.reflect.visitor.CtInheritanceScannerMethodsTest.testMethodsInInheritanceScanner() at distance(s): 37, 41
* spoon.reflect.ast.CloneTest.testCloneMethodsDeclaredInAST() at distance(s): 37, 41
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 38, 42
* spoon.test.api.MetamodelTest.testRoleOnField() at distance(s): 39, 43, 102, 103, 106, 107, 110
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 40, 55
* spoon.generating.replace.ReplaceScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 44, 45, 46, 47, 48, 49
* spoon.generating.CloneVisitorGenerator.process() at distance(s): 52, 53, 54, 55, 56, 57


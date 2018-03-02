# visitCtArrayTypeReference(spoon.reflect.reference.CtArrayTypeReference)

**Class:** spoon.support.visitor.equals.EqualsChecker

[[View code]](https://github.com/INRIA/spoon/blob/fd878bc71b73fc1da82356eaa6578f760c70f0de/src/main/java//spoon/support/visitor/equals/EqualsChecker.java#L167)

This method is **pseudo-tested**.


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 62 test method(s) with a minimum stack distance of 13.

## Transformations

The body of this method was removed but the test suite was not able to detect the transformation.



## Observed test methods

* spoon.test.ctClass.CtClassTest.getConstructor() at distance(s): 13, 17, 38
* spoon.test.metamodel.MMMethod.overrides(spoon.reflect.declaration.CtMethod) at distance(s): 14
* spoon.test.annotation.AnnotationTest.annotationAddValue() at distance(s): 15
* spoon.test.signature.SignatureTest.testMethodInvocationSignatureStaticFieldsVariables() at distance(s): 18
* spoon.processing.CtGenerationTest.testGenerateRoleHandler() at distance(s): 19, 23, 30, 34, 35, 39
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor() at distance(s): 19, 23, 24, 28, 32, 36, 40, 41, 44, 45, 46, 49, 50, 51, 53, 54, 58, 62, 67
* spoon.test.factory.TypeFactoryTest.reflectionAPI() at distance(s): 21, 25, 29
* spoon.test.reference.TypeReferenceTest.testTypeDeclarationWildcard() at distance(s): 22, 26, 30
* spoon.test.SpoonTestHelpers.isMetamodelRelatedType(spoon.reflect.reference.CtTypeReference) at distance(s): 24, 28, 32
* spoon.test.intercession.IntercessionScanner.visitCtMethod(spoon.reflect.declaration.CtMethod) at distance(s): 26, 30, 34
* spoon.test.imports.ImportTest.testAccessToNestedClass() at distance(s): 29, 33, 34, 38
* spoon.test.imports.ImportTest.testAccessType() at distance(s): 29, 33, 34, 38
* spoon.test.imports.ImportTest.testImportStarredPackageWithNonVisibleClass() at distance(s): 30, 34
* spoon.test.imports.ImportTest.testImportOfAnInnerClassInASuperClassPackageAutoImport() at distance(s): 30, 34
* spoon.test.imports.ImportTest.testCanAccess() at distance(s): 30, 34, 35, 39
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testStaticClasses() at distance(s): 31, 35, 36, 39, 40
* spoon.test.architecture.SpoonArchitectureEnforcerTest.noTreeSetInSpoon() at distance(s): 31, 35, 36, 39, 40
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testSpecPackage() at distance(s): 31, 35, 36, 39, 40
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testInterfacesAreCtScannable() at distance(s): 31, 35
* spoon.reflect.ast.AstCheckerTest.testAvoidSetCollectionSavedOnAST() at distance(s): 31, 35, 36, 39, 40, 98, 102, 106
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testGoodTestClassNames() at distance(s): 31, 35, 38, 50, 51, 52, 53
* spoon.test.visibility.VisibilityTest.testInvocationVisibilityInFieldDeclaration() at distance(s): 31, 35
* spoon.test.imports.ImportTest.testSpoonWithImports() at distance(s): 31, 35, 36, 40
* spoon.test.variable.AccessFullyQualifiedFieldTest.testPrivateStaticImportShouldNotBeImportedInSameClass() at distance(s): 33, 37
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine() at distance(s): 33, 37, 38, 41, 42
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithGeneric() at distance(s): 33, 37
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAClassWithImports() at distance(s): 33, 37
* spoon.test.prettyprinter.DefaultPrettyPrinterTest.testPrintAMethodWithImports() at distance(s): 33, 37
* spoon.test.prettyprinter.PrinterTest.testAutoimportModeDontImportUselessStatic() at distance(s): 34, 38
* spoon.test.architecture.SpoonArchitectureEnforcerTest.statelessFactory() at distance(s): 35, 36, 39, 40
* spoon.test.comment.CommentTest.testDocumentationContract() at distance(s): 35, 36, 39, 40
* spoon.test.api.APITest.testSetterInNodes() at distance(s): 35, 36, 39, 40, 72, 76, 80
* spoon.test.imports.ImportTest.testSortImportPutStaticImportAfterTypeImport() at distance(s): 35, 39
* spoon.test.metamodel.SpoonMetaModel.getRoleOfMethod(spoon.reflect.declaration.CtMethod) at distance(s): 35, 36, 37
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties() at distance(s): 36, 37, 40, 41
* spoon.reflect.declaration.CtTypeInformationTest.testGetSuperclass() at distance(s): 36, 37, 38
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory() at distance(s): 36, 37, 40, 41
* spoon.reflect.declaration.CtTypeInformationTest.testGetAllMethodsWontReturnOverriddenMethod() at distance(s): 37, 38
* spoon.test.imports.ImportTest.testWithInnerEnumDoesNotImportStaticInnerMethods() at distance(s): 39, 83
* spoon.test.template.TemplateInvocationSubstitutionTest.testInvocationSubstitutionByExpression() at distance(s): 45, 49, 53
* spoon.test.reference.VariableAccessTest.testGetDeclarationAfterClone() at distance(s): 45
* spoon.test.prettyprinter.PrinterTest.testPrinterTokenListener() at distance(s): 48, 49, 50, 51, 52
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnParameterInMethod() at distance(s): 49, 50, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationOnLocalVariableInMethod() at distance(s): 49, 50, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInNewInstance() at distance(s): 49, 50, 51, 52, 53
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInStatements() at distance(s): 49, 50, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation() at distance(s): 49, 50, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationBeforeExceptionInSignatureOfMethod() at distance(s): 49, 50, 51, 52, 53, 54, 55
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk() at distance(s): 49, 50, 51, 52, 95, 96
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationWithGenericTypesInClassDeclaration() at distance(s): 49, 50, 52, 53, 54, 55
* spoon.test.annotation.AnnotationTest.testAbstractAllAnnotationProcessor() at distance(s): 49, 50, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testUsageOfParametersInTypeAnnotation() at distance(s): 49, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInReturnTypeInMethod() at distance(s): 49, 50, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInCast() at distance(s): 49, 50, 51, 52, 53
* spoon.test.annotation.AnnotationTest.testUsageOfTypeAnnotationInExtendsImplementsOfAClass() at distance(s): 49, 50, 51, 52, 53, 54
* spoon.test.annotation.AnnotationTest.testAnnotatedElementTypes() at distance(s): 50, 51, 52, 53
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass() at distance(s): 66
* spoon.test.metamodel.SpoonMetaModel.&lt;init&gt;(spoon.reflect.factory.Factory) at distance(s): 77, 81, 85
* spoon.test.prettyprinter.PrinterTest.testJDTBatchCompilerCanBeBuild() at distance(s): 91, 95
* spoon.test.query_function.VariableReferencesTest.testCheckModelConsistency() at distance(s): 110, 114
* spoon.test.query_function.VariableReferencesTest.testVariableReferenceFunction() at distance(s): 110, 114
* spoon.test.query_function.VariableReferencesTest.testParameterReferenceFunction() at distance(s): 110, 114


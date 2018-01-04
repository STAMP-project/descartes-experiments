# Summary
**spoon.support.reflect.reference.CtTypeReferenceImpl.canAccess(spoon.reflect.reference.CtTypeReference)**

This method is **weak pseudo-tested**.
It is covered by 85 test(s). 


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 85 test(s).
* spoon.processing.ProcessingTest.testSpoonTagger()
* spoon.test.comment.CommentTest.testJavaDocCommentOnUnix()
* spoon.test.annotation.AnnotationValuesTest.testAnnotationPrintAnnotation()
* spoon.test.generics.GenericsTest.testInvocationGenerics()
* spoon.test.annotation.AnnotationTest.testSpoonSpoonResult()
* spoon.processing.CtGenerationTest.testGenerateReplacementVisitor()
* spoon.test.generics.GenericsTest.testBugCommonCollection()
* spoon.test.compilationunit.TestCompilationUnit.testAddDeclaredTypeInCU()
* spoon.test.constructor.ConstructorTest.testTypeAnnotationWithConstructorsOnFormalType()
* spoon.test.generics.GenericsTest.testDiamondComplexGenericsRxJava()
* spoon.test.architecture.SpoonArchitectureEnforcerTest.testFactorySubFactory()
* spoon.test.compilation.CompilationTest.testNewInstanceFromExistingClass()
* spoon.test.constructorcallnewclass.ConstructorCallTest.testConstructorCallObjectWithParameters()
* spoon.test.comment.CommentTest.testJavaDocCommentOnMac()
* spoon.test.api.NoClasspathTest.testInheritanceInNoClassPathWithClasses()
* spoon.test.comment.CommentTest.testCoreFactory()
* spoon.test.api.APITest.testDestinationOfSpoon()
* spoon.test.api.APITest.testAddProcessorMethodInSpoonAPI()
* spoon.test.arrays.ArraysTest.testCtNewArrayWitComments()
* spoon.processing.CtGenerationTest.testGenerateCloneVisitor()
* spoon.test.generics.GenericsTest.testCtTypeReference_getSuperclass()
* spoon.test.comment.CommentTest.testBlockComment()
* spoon.test.enums.EnumsTest.testAnnotationsOnEnum()
* spoon.test.fieldaccesses.FieldAccessTest.testGetReference()
* spoon.test.ctClass.CtClassTest.testDefaultConstructorAreOk()
* spoon.test.compilation.CompilationTest.testPrecompile()
* spoon.test.generics.GenericsTest.testClassTypingContext()
* spoon.test.generics.GenericsTest.testConstructorCallGenerics()
* spoon.processing.CtGenerationTest.testGenerateRoleHandler()
* spoon.test.constructorcallnewclass.ConstructorCallTest.testConstructorCallStringWithoutParameters()
* spoon.test.comment.CommentTest.testCodeFactory()
* spoon.test.constructorcallnewclass.ConstructorCallTest.testConstructorCallObjectWithoutParameters()
* spoon.test.annotation.AnnotationTest.testOutputGeneratedByTypeAnnotation()
* spoon.test.arrays.ArraysTest.testArrayReferences()
* spoon.test.comment.CommentTest.testCombinedPackageInfoComment()
* spoon.test.constructorcallnewclass.ConstructorCallTest.testConstructorCallWithGenericArray()
* spoon.test.comment.CommentTest.testInsertNewComment()
* spoon.test.comment.CommentTest.testInLineComment()
* spoon.test.constructor.ConstructorTest.callParamConstructor()
* spoon.reflect.ast.CloneTest.testCloneListener()
* spoon.test.ctClass.CtClassTest.testAllTypeReferencesToALocalTypeShouldNotStartWithNumber()
* spoon.test.generics.GenericsTest.testName()
* spoon.test.api.APITest.testOutputOfSpoon()
* spoon.test.generics.GenericsTest.testGenericsInQualifiedNameInConstructorCall()
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessWithoutAnyImport()
* spoon.test.constructor.ConstructorTest.testTransformationOnConstructorWithInsertBegin()
* spoon.support.compiler.jdt.JDTBatchCompilerTest.testCompileGeneratedJavaFile()
* spoon.processing.CtGenerationTest.testGenerateCtBiScanner()
* spoon.test.filters.FilterTest.testFunctionQueryStep()
* spoon.test.comment.CommentTest.testJavaDocEmptyCommentAndTag()
* spoon.test.casts.CastTest.testTypeAnnotationOnCast()
* spoon.test.api.APITest.testPrintNotAllSourcesWithNames()
* spoon.test.api.APITest.testPrintNotAllSourcesWithFilter()
* spoon.test.constructor.ConstructorTest.testTypeAnnotationOnExceptionDeclaredInConstructors()
* spoon.reflect.visitor.CtScannerTest.testScannerCallsAllProperties()
* spoon.test.api.APITest.testSourceClasspathDoesNotAcceptDotClass()
* spoon.test.constructorcallnewclass.NewClassTest.testCtNewClassInNoClasspath()
* spoon.test.generics.GenericsTest.testInstanceOfMapEntryGeneric()
* spoon.test.fieldaccesses.FieldAccessTest.testTypeDeclaredInAnonymousClass()
* spoon.test.ctClass.CtClassTest.testCloneAnonymousClassInvocationWithAutoimports()
* spoon.test.api.MetamodelTest.testRoleOnField()
* spoon.test.constructorcallnewclass.ConstructorCallTest.testConstructorCallStringWithParameters()
* spoon.test.comment.CommentTest.testWildComments()
* spoon.test.api.APITest.testOneLinerIntro()
* spoon.test.executable.ExecutableRefTest.testSameTypeInConstructorCallBetweenItsObjectAndItsExecutable()
* spoon.test.ctClass.CtClassTest.testParentOfTheEnclosingClassOfStaticClass()
* spoon.test.comment.CommentTest.testCommentsInResourcesWithWindowsEOL()
* spoon.test.ctClass.CtClassTest.testNoClasspathWithSuperClassOfAClassInAnInterface()
* spoon.test.api.APITest.testInvalidateCacheOfCompiler()
* spoon.test.api.APITest.testPrintNotAllSourcesInCommandLine()
* spoon.test.comment.CommentTest.testRemoveComment()
* spoon.test.api.NoClasspathTest.testGetStaticDependency()
* spoon.test.generics.GenericsTest.testMethodsWithGenericsWhoExtendsObject()
* spoon.test.arrays.ArraysTest.testCtNewArrayInnerCtNewArray()
* spoon.test.generics.GenericsTest.testGenericInField()
* spoon.test.constructor.ConstructorTest.testConstructorCallFactory()
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessDeclaredInADefaultClass()
* spoon.test.constructorcallnewclass.ConstructorCallTest.testCoreConstructorCall()
* spoon.test.fieldaccesses.FieldAccessTest.testFieldAccessNoClasspath()
* spoon.test.constructor.ConstructorTest.testTransformationOnConstructorWithInsertBefore()
* spoon.test.ctType.CtTypeTest.testHasMethodInDefaultMethod()
* spoon.test.ctType.CtTypeTest.testHasMethodInSuperClass()
* spoon.test.annotation.AnnotationTest.testAnnotationTypeAndFieldOnField()
* spoon.test.generics.GenericsTest.testNewClassGenerics()
* spoon.test.comment.CommentTest.testCommentsInComment1And2()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

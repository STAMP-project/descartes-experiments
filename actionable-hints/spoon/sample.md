- [ ] [spoon.support.reflect.declaration.CtAnnotationMethodImpl.setFormalCtTypeParameters(java.util.List)](methods/spoon.support.reflect.declaration.CtAnnotationMethodImpl.setFormalCtTypeParameters(java.util.List).md)
- [ ] [spoon.support.visitor.java.JavaReflectionTreeBuilder$7.addArrayReference(spoon.reflect.reference.CtArrayTypeReference)](methods/spoon.support.visitor.java.JavaReflectionTreeBuilder$7.addArrayReference(spoon.reflect.reference.CtArrayTypeReference).md)
- [X] [spoon.support.visitor.equals.EqualsChecker.visitCtImport(spoon.reflect.declaration.CtImport)](methods/spoon.support.visitor.equals.EqualsChecker.visitCtImport(spoon.reflect.declaration.CtImport).md)
    > This class is widely used in the code base. This method relates to a feature that has been recently added and hasn't been directly targeted by tests.

- [ ] [spoon.support.SerializationModelStreamer$1.matches(spoon.reflect.declaration.CtElement)](methods/spoon.support.SerializationModelStreamer$1.matches(spoon.reflect.declaration.CtElement).md)
- [ ] [spoon.template.TemplateMatcher$1.visitCtTypeParameterReference(spoon.reflect.reference.CtTypeParameterReference)](methods/spoon.template.TemplateMatcher$1.visitCtTypeParameterReference(spoon.reflect.reference.CtTypeParameterReference).md)
    > This implementation is being changed completely. It is actually not used the way it is right now.

- [ ] [spoon.support.reflect.declaration.CtMethodImpl.setShadow(boolean)](methods/spoon.support.reflect.declaration.CtMethodImpl.setShadow(boolean).md)
- [X] [spoon.support.visitor.replace.ReplacementVisitor.visitCtConstructor(spoon.reflect.declaration.CtConstructor)](methods/spoon.support.visitor.replace.ReplacementVisitor.visitCtConstructor(spoon.reflect.declaration.CtConstructor).md)
    > This class has been *auto-generated*. It is part of a bootstrap mechanisms for developing Spoon itself. Even when it is a generated code, they are targeted in the test suite, both the parts in charge of the generation and the generated code, as it is intended for heavy use.

- [X] [spoon.reflect.visitor.ImportScannerImpl.visitCtEnum(spoon.reflect.declaration.CtEnum)](methods/spoon.reflect.visitor.ImportScannerImpl.visitCtEnum(spoon.reflect.declaration.CtEnum).md)
    > Related to new features that should be tested.

- [ ] [spoon.support.reflect.declaration.CtAnnotationImpl.setTypeCasts(java.util.List)](methods/spoon.support.reflect.declaration.CtAnnotationImpl.setTypeCasts(java.util.List).md)
- [X] [spoon.reflect.visitor.DefaultJavaPrettyPrinter.visitCtLocalVariableReference(spoon.reflect.reference.CtLocalVariableReference)](methods/spoon.reflect.visitor.DefaultJavaPrettyPrinter.visitCtLocalVariableReference(spoon.reflect.reference.CtLocalVariableReference).md)
    > Several parts of the code depend on this class.

- [X] [spoon.support.reflect.eval.VisitorPartialEvaluator.visitCtAssignment(spoon.reflect.code.CtAssignment)](methods/spoon.support.reflect.eval.VisitorPartialEvaluator.visitCtAssignment(spoon.reflect.code.CtAssignment).md)
    > This class performs a partial evaluation in the AST. Assignments are an important part of the evaluation.

- [ ] [spoon.support.reflect.code.CtLambdaImpl.setThrownTypes(java.util.Set)](methods/spoon.support.reflect.code.CtLambdaImpl.setThrownTypes(java.util.Set).md)
- [ ] [spoon.support.reflect.declaration.CtEnumImpl.setFormalCtTypeParameters(java.util.List)](methods/spoon.support.reflect.declaration.CtEnumImpl.setFormalCtTypeParameters(java.util.List).md)
- [ ] [spoon.support.visitor.replace.ReplacementVisitor$CtLoopBodyReplaceListener.set(spoon.reflect.code.CtStatement)](methods/spoon.support.visitor.replace.ReplacementVisitor$CtLoopBodyReplaceListener.set(spoon.reflect.code.CtStatement).md)
- [ ] [spoon.support.visitor.clone.CloneBuilder.visitCtPackageExport(spoon.reflect.declaration.CtPackageExport)](methods/spoon.support.visitor.clone.CloneBuilder.visitCtPackageExport(spoon.reflect.declaration.CtPackageExport).md)
    > This is a feature related to Java 9. It is brand new and they haven't prepared specific tests for this. It is not a priority right now.

- [ ] [spoon.reflect.visitor.ImportScannerImpl.addFieldImport(spoon.reflect.reference.CtFieldReference)](methods/spoon.reflect.visitor.ImportScannerImpl.addFieldImport(spoon.reflect.reference.CtFieldReference).md)
- [ ] [spoon.support.reflect.cu.position.SourcePositionImpl.getColumn()](methods/spoon.support.reflect.cu.position.SourcePositionImpl.getColumn().md)
- [X] [spoon.support.visitor.java.JavaReflectionVisitorImpl.visitArrayReference(java.lang.Class)](methods/spoon.support.visitor.java.JavaReflectionVisitorImpl.visitArrayReference(java.lang.Class).md)
    > This class is in charge of loading a model of compiled classes, so it plays an important role in the code base.

- [ ] [spoon.support.reflect.code.CtLocalVariableImpl.getVisibility()](methods/spoon.support.reflect.code.CtLocalVariableImpl.getVisibility().md)
- [ ] [spoon.support.reflect.declaration.CtConstructorImpl.setSimpleName(java.lang.String)](methods/spoon.support.reflect.declaration.CtConstructorImpl.setSimpleName(java.lang.String).md)
- [ ] [spoon.reflect.visitor.CtScanner.visitCtComment(spoon.reflect.code.CtComment)](methods/spoon.reflect.visitor.CtScanner.visitCtComment(spoon.reflect.code.CtComment).md)
- [X] [spoon.support.reflect.eval.VisitorPartialEvaluator.visitCtWhile(spoon.reflect.code.CtWhile)](methods/spoon.support.reflect.eval.VisitorPartialEvaluator.visitCtWhile(spoon.reflect.code.CtWhile).md)
    > Role of `VisitorPartialEvaluator`. It should work well for the condition of the `while`.

- [ ] [spoon.processing.AbstractProcessor.init()](methods/spoon.processing.AbstractProcessor.init().md)
- [ ] [spoon.reflect.visitor.ImportScannerImpl.classNamePresentInJavaLang(spoon.reflect.reference.CtTypeReference)](methods/spoon.reflect.visitor.ImportScannerImpl.classNamePresentInJavaLang(spoon.reflect.reference.CtTypeReference).md)
- [ ] [spoon.support.StandardEnvironment.getProcessorProperties(java.lang.String)](methods/spoon.support.StandardEnvironment.getProcessorProperties(java.lang.String).md)
- [X] [spoon.reflect.visitor.filter.LocalVariableReferenceFunction$Context.exit(spoon.reflect.declaration.CtElement)](methods/spoon.reflect.visitor.filter.LocalVariableReferenceFunction$Context.exit(spoon.reflect.declaration.CtElement).md)
    > This class implements a counter. The `exit` method should affect the result.

- [ ] [spoon.support.visitor.clone.CloneBuilder.visitCtBreak(spoon.reflect.code.CtBreak)](methods/spoon.support.visitor.clone.CloneBuilder.visitCtBreak(spoon.reflect.code.CtBreak).md)
- [ ] [spoon.support.reflect.declaration.CtClassImpl.insertAfter(spoon.reflect.code.CtStatement)](methods/spoon.support.reflect.declaration.CtClassImpl.insertAfter(spoon.reflect.code.CtStatement).md)
- [ ] [spoon.support.reflect.declaration.CtAnonymousExecutableImpl.getVisibility()](methods/spoon.support.reflect.declaration.CtAnonymousExecutableImpl.getVisibility().md)
- [X] [spoon.reflect.visitor.CtScanner.scan(spoon.reflect.path.CtRole,java.lang.Object)](methods/spoon.reflect.visitor.CtScanner.scan(spoon.reflect.path.CtRole,java.lang.Object).md)
    > They have several overloads of this method targeting specific types instead of `Object`, but no targeting this particular overload.

- [ ] [spoon.support.reflect.declaration.CtAnnotationTypeImpl.setSuperInterfaces(java.util.Set)](methods/spoon.support.reflect.declaration.CtAnnotationTypeImpl.setSuperInterfaces(java.util.Set).md)
- [ ] [spoon.support.reflect.declaration.CtClassImpl.setLabel(java.lang.String)](methods/spoon.support.reflect.declaration.CtClassImpl.setLabel(java.lang.String).md)
- [X] [spoon.reflect.visitor.CtBiScannerDefault.visitCtNewClass(spoon.reflect.code.CtNewClass)](methods/spoon.reflect.visitor.CtBiScannerDefault.visitCtNewClass(spoon.reflect.code.CtNewClass).md)
    > Auto-generated class with impact.

- [ ] [spoon.support.reflect.declaration.CtModuleImpl.addUsedService(spoon.reflect.declaration.CtUsedService)](methods/spoon.support.reflect.declaration.CtModuleImpl.addUsedService(spoon.reflect.declaration.CtUsedService).md)
    > Not fully supported yet.

- [ ] [spoon.support.reflect.code.CtConstructorCallImpl.setLabel(java.lang.String)](methods/spoon.support.reflect.code.CtConstructorCallImpl.setLabel(java.lang.String).md)
- [ ] [spoon.support.reflect.declaration.CtTypeParameterImpl.setSuperInterfaces(java.util.Set)](methods/spoon.support.reflect.declaration.CtTypeParameterImpl.setSuperInterfaces(java.util.Set).md)
- [ ] [spoon.support.reflect.declaration.CtParameterImpl.setShadow(boolean)](methods/spoon.support.reflect.declaration.CtParameterImpl.setShadow(boolean).md)
- [ ] [spoon.support.visitor.clone.CloneBuilder.visitCtLambda(spoon.reflect.code.CtLambda)](methods/spoon.support.visitor.clone.CloneBuilder.visitCtLambda(spoon.reflect.code.CtLambda).md)
- [ ] [spoon.testing.utils.ModelUtils.canBeBuilt(java.lang.String,int,boolean)](methods/spoon.testing.utils.ModelUtils.canBeBuilt(java.lang.String,int,boolean).md)
- [X] [spoon.reflect.visitor.ImportScannerImpl.visitCtInterface(spoon.reflect.declaration.CtInterface)](methods/spoon.reflect.visitor.ImportScannerImpl.visitCtInterface(spoon.reflect.declaration.CtInterface).md)
- [ ] [spoon.support.reflect.declaration.CtAnnotationMethodImpl.setParameters(java.util.List)](methods/spoon.support.reflect.declaration.CtAnnotationMethodImpl.setParameters(java.util.List).md)
- [ ] [spoon.support.reflect.declaration.CtAnnotationMethodImpl.setBody(spoon.reflect.code.CtStatement)](methods/spoon.support.reflect.declaration.CtAnnotationMethodImpl.setBody(spoon.reflect.code.CtStatement).md)
- [X] [spoon.reflect.visitor.CtBiScannerDefault.visitCtTryWithResource(spoon.reflect.code.CtTryWithResource)](methods/spoon.reflect.visitor.CtBiScannerDefault.visitCtTryWithResource(spoon.reflect.code.CtTryWithResource).md)
- [ ] [spoon.reflect.visitor.CtScanner.visitCtBreak(spoon.reflect.code.CtBreak)](methods/spoon.reflect.visitor.CtScanner.visitCtBreak(spoon.reflect.code.CtBreak).md)
- [X] [spoon.reflect.visitor.CtBiScannerDefault.visitCtConstructorCall(spoon.reflect.code.CtConstructorCall)](methods/spoon.reflect.visitor.CtBiScannerDefault.visitCtConstructorCall(spoon.reflect.code.CtConstructorCall).md)
- [ ] [spoon.support.visitor.java.JavaReflectionVisitorImpl.visitInterfaceReference(java.lang.Class)](methods/spoon.support.visitor.java.JavaReflectionVisitorImpl.visitInterfaceReference(java.lang.Class).md)
- [X] [spoon.support.visitor.MethodTypingContext.getIndexOfTypeParam(spoon.reflect.declaration.CtFormalTypeDeclarer,spoon.reflect.reference.CtTypeReference)](methods/spoon.support.visitor.MethodTypingContext.getIndexOfTypeParam(spoon.reflect.declaration.CtFormalTypeDeclarer,spoon.reflect.reference.CtTypeReference).md)
- [ ] [spoon.support.visitor.clone.CloneBuilder.visitCtCodeSnippetExpression(spoon.reflect.code.CtCodeSnippetExpression)](methods/spoon.support.visitor.clone.CloneBuilder.visitCtCodeSnippetExpression(spoon.reflect.code.CtCodeSnippetExpression).md)
- [ ] [spoon.support.reflect.cu.position.SourcePositionImpl.searchColumnNumber(int)](methods/spoon.support.reflect.cu.position.SourcePositionImpl.searchColumnNumber(int).md)
- [X] [spoon.reflect.visitor.ImportScannerImpl.isInCollisionWithLocalMethod(spoon.reflect.reference.CtExecutableReference)](methods/spoon.reflect.visitor.ImportScannerImpl.isInCollisionWithLocalMethod(spoon.reflect.reference.CtExecutableReference).md)
    > Being the `ImportScannerImpl` this method should play an  important role, as it detects name collisions.
- [ ] [spoon.support.reflect.declaration.CtFieldImpl.setShadow(boolean)](methods/spoon.support.reflect.declaration.CtFieldImpl.setShadow(boolean).md)
- [ ] [spoon.support.reflect.code.CtUnaryOperatorImpl.setLabel(java.lang.String)](methods/spoon.support.reflect.code.CtUnaryOperatorImpl.setLabel(java.lang.String).md)
- [X] [spoon.support.reflect.reference.CtParameterReferenceImpl.fromDeclaringExecutable()](methods/spoon.support.reflect.reference.CtParameterReferenceImpl.fromDeclaringExecutable().md)

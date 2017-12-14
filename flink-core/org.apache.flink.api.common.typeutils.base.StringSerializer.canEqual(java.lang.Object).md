# Summary
**org.apache.flink.api.common.typeutils.base.StringSerializer.canEqual(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 96 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 96 test(s).
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible1() (Distance: 4)
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible2() (Distance: 4)
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible3() (Distance: 4)
* org.apache.flink.api.common.operators.SelectorFunctionKeysTest.testAreCompatible4() (Distance: 4)
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoDirect() (Distance: 4)
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorAutoSerializer() (Distance: 6)
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testValueStateDescriptorAutoSerializer() (Distance: 6)
* org.apache.flink.api.common.state.ReducingStateDescriptorTest.testValueStateDescriptorAutoSerializer() (Distance: 6)
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testCustomFieldNames() (Distance: 7)
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testGetTypeAt() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicTypes() (Distance: 7)
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testGetFlatFields() (Distance: 7)
* org.apache.flink.api.java.typeutils.CompositeTypeTest.testFieldAtStringRef() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testExtractDerivedInputFormatType() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeExtractorInputFormatsTest.testMultiLevelDerivedInputFormatType() (Distance: 7)
* org.apache.flink.api.common.typeinfo.TypeHintTest.testTypeInfoOf() (Distance: 7)
* org.apache.flink.types.BasicTypeInfoTest.testBasicTypeInfoEquality() (Distance: 7)
* org.apache.flink.api.java.typeutils.TypeInfoParserTest.testBasicArrays() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.EitherSerializerTest.testStringDoubleEither() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple2StringDouble() (Distance: 10)
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple1String() (Distance: 10)
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple2StringStringArray() (Distance: 10)
* org.apache.flink.api.common.typeutils.base.StringSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.common.typeinfo.BasicArrayTypeInfoTest.testSerialization()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible8()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclass()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInterface()
* org.apache.flink.api.java.typeutils.runtime.PojoSubclassSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible2()
* org.apache.flink.api.java.typeutils.runtime.PojoGenericTypeSerializerTest.testString()
* org.apache.flink.api.common.typeinfo.BasicTypeInfoTest.testSerialization()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible3()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithBasicTypes()
* org.apache.flink.api.java.typeutils.RowTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWC()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible1()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionWithNoGenericSuperclass()
* org.apache.flink.api.java.typeutils.EitherTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEitherHierarchy()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleSupertype()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsNotInSuperclassWithNonGenericClassAtEnd()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testChainedGenericsNotInSuperclass()
* org.apache.flink.api.java.typeutils.ListTypeInfoTest.testSerialization()
* org.apache.flink.api.common.typeinfo.BasicTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.MultisetTypeInfoTest.testSerialization()
* org.apache.flink.api.common.state.ListStateDescriptorTest.testValueStateDescriptorAutoSerializer()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithCustomTupleInput()
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testRowSerializerWithComplexTypes()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoExtendingTuple()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference4()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValueNested()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSameGenericVariable()
* org.apache.flink.api.java.typeutils.MapTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testRowSerializer()
* org.apache.flink.api.java.typeutils.PojoTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunction()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testRow()
* org.apache.flink.api.common.typeinfo.BasicArrayTypeInfoTest.testHashcodeAndEquals()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithComplexHierarchy()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testExtractKeySelector()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testSubclassOfTuple()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithPrimitiveArray()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoWithGenerics()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericArraySerializerTest.testString()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy2()
* org.apache.flink.api.java.typeutils.runtime.RowSerializerTest.testLargeRowSerializer()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testBasicArray()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testPojoAllPublic()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyEitherGenericType()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible4()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputMismatchWithRawFuntion()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchyWithInference()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testDuplicateValue()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testOriginalTypes()
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithFunctionHierarchy()
* org.apache.flink.api.java.typeutils.PojoTypeExtractionTest.testGenericPojoTypeInference1()
* org.apache.flink.api.java.typeutils.MapTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference1()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleArray()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testNestedTupleGenerics()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible5()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testInputInference3()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testEither()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testGenericsInDirectSuperclass()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testAbstractAndInterfaceTypes()
* org.apache.flink.api.java.typeutils.runtime.PojoSerializerTest.testTuplePojoTestEquality()
* org.apache.flink.api.java.typeutils.TypeInfoFactoryTest.testMyTupleHierarchy()
* org.apache.flink.api.common.typeutils.base.MapSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testFunctionDependingOnInputWithTupleInput()
* org.apache.flink.api.java.typeutils.TupleTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testMissingTupleGenerics()
* org.apache.flink.api.java.typeutils.EitherTypeInfoTest.testSerialization()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testTupleWithTuples()
* org.apache.flink.api.java.typeutils.TypeExtractorTest.testResultTypeQueryable()
* org.apache.flink.api.common.operators.ExpressionKeysTest.testAreCompatible9()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

# Summary
**org.apache.flink.api.java.typeutils.runtime.kryo.KryoSerializer.canEqual(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 35 test(s). It can be directly accessed from tests methods.


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 35 test(s).
* org.apache.flink.api.common.state.MapStateDescriptorTest.testMapStateDescriptorEagerSerializer() (Distance: 6)
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testValueStateDescriptorEagerSerializer() (Distance: 6)
* org.apache.flink.api.common.state.ValueStateDescriptorTest.testVeryLargeDefaultValue() (Distance: 6)
* org.apache.flink.api.common.state.ReducingStateDescriptorTest.testValueStateDescriptorEagerSerializer() (Distance: 6)
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoWithCustomSerializersTest.testJodaTime() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testJavaDequeue() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testJavaList() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testJavaSet() (Distance: 8)
* org.apache.flink.api.java.typeutils.runtime.TupleSerializerTest.testTuple5CustomObjects() (Distance: 10)
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoWithCustomSerializersTest.testCompositeObject()
* org.apache.flink.api.common.state.ListStateDescriptorTest.testValueStateDescriptorEagerSerializer()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testCompositeObject()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoSerializerClassLoadingTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoWithCustomSerializersTest.testSimpleTypesObjects()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericArraySerializerTest.testSimpleTypesObjects()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoWithCustomSerializersTest.testNestedObjects()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoWithCustomSerializersTest.testBeanStyleObjects()
* org.apache.flink.api.java.typeutils.runtime.MultidimensionalArraySerializerTest.testObjectArrays()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testSimpleTypesObjects()
* org.apache.flink.api.java.typeutils.runtime.PojoGenericTypeSerializerTest.testCompositeObject()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testNestedInterfaces()
* org.apache.flink.api.java.typeutils.runtime.PojoGenericTypeSerializerTest.testNestedObjects()
* org.apache.flink.api.java.typeutils.runtime.PojoGenericTypeSerializerTest.testBeanStyleObjects()
* org.apache.flink.api.java.typeutils.runtime.PojoGenericTypeSerializerTest.testNestedInterfaces()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoWithCustomSerializersTest.testNestedInterfaces()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericArraySerializerTest.testBeanStyleObjects()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericArraySerializerTest.testCompositeObject()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testString()
* org.apache.flink.api.java.typeutils.runtime.SubclassFromInterfaceSerializerTest.testSerializabilityAndEquals()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoWithCustomSerializersTest.testString()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testBeanStyleObjects()
* org.apache.flink.api.java.typeutils.runtime.PojoGenericTypeSerializerTest.testSimpleTypesObjects()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericArraySerializerTest.testString()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericArraySerializerTest.testNestedObjects()
* org.apache.flink.api.java.typeutils.runtime.kryo.KryoGenericTypeSerializerTest.testNestedObjects()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

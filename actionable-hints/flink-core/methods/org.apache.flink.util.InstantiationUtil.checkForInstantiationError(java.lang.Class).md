# checkForInstantiationError(java.lang.Class)

**Class:** org.apache.flink.util.InstantiationUtil

[[View code]](https://github.com/apache/flink/blob/740f711c4ec9c4b7cdefd01c9f64857c345a68a1/flink-core/src/main/java//org/apache/flink/util/InstantiationUtil.java#L227)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `&quot;&quot;`, `&quot;A&quot;`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 1 test method(s) with a minimum stack distance of 2.

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return "";
```

```Java
return "A";
```

The following transformations were also applied and they were detected by the test suite:

```Java
return null;
```





## Observed test methods

* org.apache.flink.util.InstantiationUtilTest.testCheckForInstantiationOfPrivateClass() at distance(s): 2


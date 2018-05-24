# isInVelocityBlock()

**Class:** org.xwiki.velocity.internal.util.VelocityParserContext

[[View code]](https://github.com/xwiki/xwiki-commons/blob/6090f4369cf659a57237449a21105515b1c27995/xwiki-commons-core/xwiki-commons-velocity/src/main/java//org/xwiki/velocity/internal/util/VelocityParserContext.java#L93)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes and it is directly covered by the test suite. 
It has been covered by 3 test method(s).

## Transformations


The body of this method has been replaced by the following instructions and they have not been detected by the test suite:

```Java
return false;
```

The following transformations were also applied and they were detected by the test suite:

```Java
return true;
```





## Observed test methods

* org.xwiki.velocity.internal.util.VelocityParserTest.getKeyWordDirective() at distance(s): 1
* org.xwiki.velocity.internal.util.VelocityParserTest.getKeyWordComment() at distance(s): 1
* org.xwiki.velocity.internal.util.VelocityParserTest.getKeyWordMultiLinesComment() at distance(s): 1

## Remarks
A new test case was added to target this method and make it return `true`.

## Involved commit(s)
[534c264fc53002997418f24653744da41c806b9f](https://github.com/xwiki/xwiki-commons/commit/534c264fc53002997418f24653744da41c806b9f)
# hasData(org.apache.commons.codec.binary.BaseNCodec$Context)

**Class:** org.apache.commons.codec.binary.BaseNCodec

[[View code]](https://github.com/apache/commons-codec/blob/588602694fa1d19e433f9e2705aed9ccb0b404ba/src/main/java//org/apache/commons/codec/binary/BaseNCodec.java#L222)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can not be accessed from other classes. 
It has been covered by 25 test method(s) with a minimum stack distance of 2.

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

* org.apache.commons.codec.binary.Base64InputStreamTest.testSkipNone() at distance(s): 2, 3
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipNone() at distance(s): 2, 3
* org.apache.commons.codec.binary.Base32InputStreamTest.testCodec105() at distance(s): 3
* org.apache.commons.codec.binary.Base64InputStreamTest.testSkipPastEnd() at distance(s): 3
* org.apache.commons.codec.binary.Base32InputStreamTest.testCodec130() at distance(s): 3, 4
* org.apache.commons.codec.binary.Base64InputStreamTest.testSkipBig() at distance(s): 3
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipToEnd() at distance(s): 3
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipPastEnd() at distance(s): 3
* org.apache.commons.codec.binary.Base64InputStreamTest.testCodec105() at distance(s): 3
* org.apache.commons.codec.binary.Base64InputStreamTest.testCodec130() at distance(s): 3, 4
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipBig() at distance(s): 3
* org.apache.commons.codec.binary.Base32InputStreamTest.testAvailable() at distance(s): 3
* org.apache.commons.codec.binary.Base64InputStreamTest.testAvailable() at distance(s): 3
* org.apache.commons.codec.binary.Base64InputStreamTest.testCodec101() at distance(s): 3
* org.apache.commons.codec.binary.Base64InputStreamTest.testSkipToEnd() at distance(s): 3
* org.apache.commons.codec.binary.Base64InputStreamTest.testBase64InputStreamByteByByte() at distance(s): 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42
* org.apache.commons.codec.binary.Base64InputStreamTest.testBase64InputStreamByChunk() at distance(s): 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32InputStreamByChunk() at distance(s): 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44
* org.apache.commons.codec.binary.Base64InputStreamTest.testCodec98NPE() at distance(s): 4
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32InputStreamByteByByte() at distance(s): 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42
* org.apache.commons.codec.binary.Base64InputStreamTest.testBase64EmptyInputStreamMimeChuckSize() at distance(s): 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32EmptyInputStreamMimeChuckSize() at distance(s): 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32EmptyInputStreamPemChuckSize() at distance(s): 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45
* org.apache.commons.codec.binary.Base64InputStreamTest.testBase64EmptyInputStreamPemChuckSize() at distance(s): 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45
* org.apache.commons.codec.binary.Base64InputStreamTest.testInputStreamReader() at distance(s): 9


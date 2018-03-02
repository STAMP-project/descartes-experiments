# isInAlphabet(byte)

**Class:** org.apache.commons.codec.binary.Base32

[[View code]](https://github.com/apache/commons-codec/blob/588602694fa1d19e433f9e2705aed9ccb0b404ba/src/main/java//org/apache/commons/codec/binary/Base32.java#L542)

This method is **partially-tested**.

It seems that this method has been tested to return only the following value(s): `false`


It can be accessed from other classes but it is not directly covered by the test suite. 
It has been covered by 38 test method(s) with a minimum stack distance of 3.

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

* org.apache.commons.codec.binary.Base32Test.testRandomBytesHex() at distance(s): 3
* org.apache.commons.codec.binary.Base32Test.testCodec200() at distance(s): 3
* org.apache.commons.codec.binary.Base32Test.testBase32HexSamplesReverse() at distance(s): 3
* org.apache.commons.codec.binary.Base32Test.testBase32HexSamplesReverseLowercase() at distance(s): 3
* org.apache.commons.codec.binary.Base32Test.testBase32HexSamples() at distance(s): 3
* org.apache.commons.codec.binary.Base32InputStreamTest.testCodec105() at distance(s): 4
* org.apache.commons.codec.binary.Base32OutputStreamTest.testBase32OutputStreamByChunk() at distance(s): 4, 5, 6
* org.apache.commons.codec.binary.Base32Test.testBase32Chunked() at distance(s): 4, 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32InputStreamByChunk() at distance(s): 4, 5, 6
* org.apache.commons.codec.binary.Base32Test.testBase32BinarySamples() at distance(s): 4
* org.apache.commons.codec.binary.Base32InputStreamTest.testReadOutOfBounds() at distance(s): 4, 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testRead0() at distance(s): 4, 5
* org.apache.commons.codec.binary.Base32Test.testRandomBytes() at distance(s): 4
* org.apache.commons.codec.binary.Base32Test.testSingleCharEncoding() at distance(s): 4
* org.apache.commons.codec.binary.Base32InputStreamTest.testReadNull() at distance(s): 4, 5
* org.apache.commons.codec.binary.Base32Test.testRandomBytesChunked() at distance(s): 4, 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32InputStreamByteByByte() at distance(s): 4, 5, 6
* org.apache.commons.codec.binary.Base32InputStreamTest.testMarkSupported() at distance(s): 4, 5
* org.apache.commons.codec.binary.Base32Test.testBase32BinarySamplesReverse() at distance(s): 4
* org.apache.commons.codec.binary.Base32Test.testBase32Samples() at distance(s): 4
* org.apache.commons.codec.binary.Base32Test.testBase32SamplesNonDefaultPadding() at distance(s): 4
* org.apache.commons.codec.binary.Base32OutputStreamTest.testBase32OutputStreamByteByByte() at distance(s): 4, 5, 6
* org.apache.commons.codec.binary.Base32OutputStreamTest.testWriteOutOfBounds() at distance(s): 5
* org.apache.commons.codec.binary.Base32Test.testBase64AtBufferStart() at distance(s): 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testCodec130() at distance(s): 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipToEnd() at distance(s): 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipPastEnd() at distance(s): 5
* org.apache.commons.codec.binary.Base32OutputStreamTest.testWriteToNullCoverage() at distance(s): 5
* org.apache.commons.codec.binary.Base32Test.testBase64AtBufferEnd() at distance(s): 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipNone() at distance(s): 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipBig() at distance(s): 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testAvailable() at distance(s): 5
* org.apache.commons.codec.binary.Base32InputStreamTest.testSkipWrongArgument() at distance(s): 5
* org.apache.commons.codec.binary.Base32Test.testBase64AtBufferMiddle() at distance(s): 5
* org.apache.commons.codec.binary.Base32OutputStreamTest.testBase32EmptyOutputStreamPemChunkSize() at distance(s): 6, 7
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32EmptyInputStreamMimeChuckSize() at distance(s): 6, 7
* org.apache.commons.codec.binary.Base32InputStreamTest.testBase32EmptyInputStreamPemChuckSize() at distance(s): 6, 7
* org.apache.commons.codec.binary.Base32OutputStreamTest.testBase32EmptyOutputStreamMimeChunkSize() at distance(s): 6, 7


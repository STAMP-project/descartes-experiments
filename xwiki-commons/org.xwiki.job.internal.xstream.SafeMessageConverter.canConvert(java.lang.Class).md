# Summary
**org.xwiki.job.internal.xstream.SafeMessageConverter.canConvert(java.lang.Class)**

This method is **weak pseudo-tested**.
It is covered by 37 test(s). 


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * false 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 37 test(s).
* org.xwiki.job.internal.DefaultJobStatusStoreTest.getJobStatusThatDoesNotExist()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithComponentManagerField()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogMessage()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testFailToSerializeObject()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testNotSerializableObjectInArray()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithCrossReference()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithSerializableStandaloneComponentArgument()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testNotSerializableObjectWithFailingToStringInArray()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithComponentArgument()
* org.xwiki.job.internal.JobStatusSerializerTest.test()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithProviderField()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithStandaloneComponentField()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithLoggerField()
* org.xwiki.job.internal.JobStatusSerializerTest.testProgress()
* org.xwiki.job.internal.DefaultJobStatusStoreTest.removeJobStatus()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithNotSerializableCustomObjectArgument()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithSerializableCustomObjectArgument()
* org.xwiki.job.internal.DefaultJobStatusStoreTest.getJobStatusInWrongPlaceAndWithInvalidLogArgument()
* org.xwiki.job.internal.DefaultJobStatusStoreTest.getJobStatusWithMultipleId()
* org.xwiki.job.internal.DefaultJobStatusStoreTest.getJobStatusWithNullId()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogMarker()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithComponentField()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testArrayWithReference()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testRecursiveObjectThroughArray()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithStandaloneComponentArgument()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithCustomObjectArgument()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithException()
* org.xwiki.job.internal.DefaultJobStatusStoreTest.storeJobStatus()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testFailToSerializeField()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testNotSerializableField()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testRecursiveObject()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithArguments()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithNullArguments()
* org.xwiki.job.internal.xstream.SafeXStreamTest.testNotSerializableObject()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithSerializableProviderField()
* org.xwiki.job.internal.DefaultJobStatusStoreTest.getJobStatusInOldPlace()
* org.xwiki.job.internal.JobStatusSerializerTest.testLogWithSerializableImplementationProviderField()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

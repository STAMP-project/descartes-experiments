# Summary
**org.xwiki.job.event.status.AbstractProgressEvent.matches(java.lang.Object)**

This method is **weak pseudo-tested**.
It is covered by 12 test(s). 


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 12 test(s).
* org.xwiki.job.internal.DefaultJobProgressTest.testProgressSteps()
* org.xwiki.job.internal.DefaultJobProgressTest.testPushLevelOnClosedStep()
* org.xwiki.job.internal.DefaultJobProgressTest.testMoreStepsThanExpected()
* org.xwiki.job.internal.DefaultJobProgressTest.testStartStepFromDifferentSource()
* org.xwiki.job.internal.DefaultJobProgressTest.testPopLevelOnParentLevelSource()
* org.xwiki.job.internal.DefaultJobProgressTest.testUnknownNumberOfSteps()
* org.xwiki.job.internal.DefaultJobProgressTest.testStepProgressEvent()
* org.xwiki.job.internal.DefaultJobProgressTest.testEndStepOnParentStepSource()
* org.xwiki.job.internal.DefaultJobProgressTest.testProgressDone()
* org.xwiki.job.internal.DefaultJobProgressTest.testMoveToNextStepInRoot()
* org.xwiki.job.internal.DefaultJobProgressTest.testPopLevelOnWrongSource()
* org.xwiki.job.internal.DefaultJobProgressTest.testPopDontMoveToNextStep()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

# Summary
**org.xwiki.extension.handler.internal.AbstractExtensionHandler.checkInstall(org.xwiki.extension.Extension,java.lang.String,org.xwiki.job.Request)**

This method is **strong pseudo-tested**.
It is covered by 44 test(s). 


## Transformations applied

- void


The test suite was not able to detect any transformation applied.

More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 44 test(s).
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenOnRootWithLowerDependency()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromAllNamespaces()
* org.xwiki.extension.job.internal.InstallJobTest.testReplaceDependencyWithFeature()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallLowerVersionOfDependencyOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithSimpleRemoteExtensionOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testUpgradeExtensionOnNamespaceWithDependencyAllowedOnRootOnly()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteOnNamespaces()
* org.xwiki.extension.job.internal.InstallJobTest.testDowngradeFirstOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testReInstalledWithMissingDependency()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanWithDependencyOnNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallNameSpaceExtensionWithExistingRootExtension()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanWithDependencyOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeOnDifferentIdNotAllowed()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteWithMissingDependency()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallNameSpaceExtensionWithExistingRootExtension()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithLowerCoreDependencyFeature()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithInstalledDependencyOnRoot()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnNamespaceWithExtensionOnRoot()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromNamespaceWithBackwarDepencency()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithCoreDependencyOnRoot()
* org.xwiki.extension.job.internal.InstallJobTest.testUpgradeFirstOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallOnNamespaceThenOnRoot()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeFeatureWithDifferentVersion()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallWithManagedDependency()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallNameSpaceExtensionWithIncompatibleRootDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenUpgradeOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithDowngradeOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithRemoteDependencyOnRoot()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnRootWithTargetDependencyExtension()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeOnDifferentId()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallNameSpaceExtensionWithDependencyAllowedOnRootOnly()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithHigherCoreDependencyFeature()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteOnNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallOnNamespaceThenUnpgradeOnRoot()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallWithOverwrittenManagedDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenMoveDependencyOnRoot()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallExtensionOnIncompatibleNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallWithManagedTransitiveDependency()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallRemoteWithMissingDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenOnRoot()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

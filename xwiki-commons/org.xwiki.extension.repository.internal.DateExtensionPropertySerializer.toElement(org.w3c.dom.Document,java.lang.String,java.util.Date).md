# Summary
**org.xwiki.extension.repository.internal.DateExtensionPropertySerializer.toElement(org.w3c.dom.Document,java.lang.String,java.util.Date)**

This method is **strong pseudo-tested**.
It is covered by 34 test(s). 


## Transformations applied

- null


The test suite was not able to detect any transformation applied.

More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 34 test(s).
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenOnRootWithLowerDependency()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromAllNamespaces()
* org.xwiki.extension.job.internal.InstallJobTest.testReplaceDependencyWithFeature()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallLowerVersionOfDependencyOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testUpgradeExtensionOnNamespaceWithDependencyAllowedOnRootOnly()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteOnNamespaces()
* org.xwiki.extension.job.internal.InstallJobTest.testDowngradeFirstOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testStoreExtensionAndInstall()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanWithDependencyOnNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallNameSpaceExtensionWithExistingRootExtension()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanWithDependencyOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testUninstallExtension()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteWithMissingDependency()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallNameSpaceExtensionWithExistingRootExtension()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnNamespaceWithExtensionOnRoot()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromNamespaceWithBackwarDepencency()
* org.xwiki.extension.job.internal.InstallJobTest.testUpgradeFirstOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallOnNamespaceThenOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testBackwardDependenciesWithExtensionOnNamespaceAndDepOnNamespace()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testBackwardDependenciesWithExtensionAndDepOnNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeFeatureWithDifferentVersion()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallNameSpaceExtensionWithIncompatibleRootDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenUpgradeOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithDowngradeOnRoot()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnRootWithTargetDependencyExtension()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteOnNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallOnNamespaceThenUnpgradeOnRoot()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnRoot()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenMoveDependencyOnRoot()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallExtensionOnIncompatibleNamespace()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenOnRoot()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

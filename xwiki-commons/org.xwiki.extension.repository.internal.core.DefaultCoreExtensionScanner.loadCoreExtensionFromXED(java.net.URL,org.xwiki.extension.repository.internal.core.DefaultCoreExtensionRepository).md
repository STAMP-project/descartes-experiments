# Summary
**org.xwiki.extension.repository.internal.core.DefaultCoreExtensionScanner.loadCoreExtensionFromXED(java.net.URL,org.xwiki.extension.repository.internal.core.DefaultCoreExtensionRepository)**

This method is **strong pseudo-tested**.
It is covered by 85 test(s). 


## Transformations applied

- null


The test suite was not able to detect any transformation applied.

More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 85 test(s).
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenOnRootWithLowerDependency()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromAllNamespaces()
* org.xwiki.extension.job.internal.InstallJobTest.testReplaceDependencyWithFeature()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallLowerVersionOfDependencyOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testUpgradeExtensionOnNamespaceWithDependencyAllowedOnRootOnly()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteOnNamespaces()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithSimpleRemoteExtensionOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithFeatureAsCoreExtension()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanWithDependencyOnNamespace()
* org.xwiki.extension.repository.core.DefaultCoreExtensionRepositoryTest.testResolve()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallNameSpaceExtensionWithExistingRootExtension()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanWithDependencyOnRoot()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testInit()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithCoreExtensionFeature()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallNameSpaceExtensionWithExistingRootExtension()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithLowerCoreDependencyFeature()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithCoreExtension()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithCoreDependencyOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithFeatureAsCoreExtensionFeature()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testGetLocalExtension()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testResolveUnexistingButFeatureCompatibleDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnRoot()
* org.xwiki.extension.repository.core.DefaultCoreExtensionRepositoryTest.testInit()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallOnNamespaceThenOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testBackwardDependenciesWithExtensionOnNamespaceAndDepOnNamespace()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testSearchInstalledExtensions()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testSearchWithQueryMATCH()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallWithBackwarDepencency()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallNameSpaceExtensionWithIncompatibleRootDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenUpgradeOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithRemoteDependencyOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithDowngradeOnRoot()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstall()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeOnDifferentId()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallNameSpaceExtensionWithDependencyAllowedOnRootOnly()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testInit()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testBackwardDependenciesWithExtensionAndDepOnRoot()
* org.xwiki.extension.repository.core.DefaultCoreExtensionRepositoryTest.testSearchWithSeveralFeatures()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithHigherCoreDependencyFeature()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteOnNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallOnNamespaceThenUnpgradeOnRoot()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnRoot()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallWithOverwrittenManagedDependency()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testForbiddenInstallExtensionOnIncompatibleNamespace()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testResolveIncompatibleDependencyVersion()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testSearch()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallRemoteWithMissingDependency()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testSearchWithQueryWithNullValue()
* org.xwiki.extension.job.internal.InstallJobTest.testDowngradeFirstOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testAdvancedSearchInstalledWithNullQuery()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testStoreExtensionAndInstall()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testSearch()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testRemove()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testReInstalledWithMissingDependency()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testUninstallExtension()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeOnDifferentIdNotAllowed()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testResolveExistingDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallRemoteWithMissingDependency()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testResolve()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testResolve()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testSearchWithQueryEQUAL()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testResolveUnexistingButSmalerVersionDependency()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithInstalledDependencyOnRoot()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnNamespaceWithExtensionOnRoot()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallFromNamespaceWithBackwarDepencency()
* org.xwiki.extension.job.internal.InstallJobTest.testUpgradeFirstOnRoot()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testAdvancedSearchWithNullQuery()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testBackwardDependenciesAfterUninstall()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUnsupportedType()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testBackwardDependenciesWithExtensionAndDepOnNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallPlanWithUpgradeFeatureWithDifferentVersion()
* org.xwiki.extension.job.internal.UninstallJobTest.testUninstallTwice()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testgetInstalledExtensionFeatureNamespace()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallWithManagedDependency()
* org.xwiki.extension.job.internal.UpgradePlanJobTest.testUpgradePlanOnRootWithTargetDependencyExtension()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testInstallTwice()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testBackwardDependenciesAfterInit()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenMoveDependencyOnRoot()
* org.xwiki.extension.repository.local.DefaultLocalExtensionRepositoryTest.testResolveUnexistingDependencyId()
* org.xwiki.extension.repository.installed.DefaultInstalledExtensionRepositoryTest.testResolveDependency()
* org.xwiki.extension.repository.core.DefaultCoreExtensionRepositoryTest.testGetCoreExtension()
* org.xwiki.extension.job.internal.InstallPlanJobTest.testInstallWithManagedTransitiveDependency()
* org.xwiki.extension.job.internal.InstallJobTest.testInstallOnNamespaceThenOnRoot()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

# Summary
**org.xwiki.crypto.pkix.internal.BcX509CertifiedPublicKey.isSignedBy(org.xwiki.crypto.params.cipher.asymmetric.PublicKeyParameters)**

This method is **weak pseudo-tested**.
It is covered by 21 test(s). 


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 21 test(s).
* org.xwiki.crypto.pkix.internal.BcX509CertificateChainBuilderTest.testIncompleteV3CertificatePath()
* org.xwiki.crypto.pkix.internal.BcX509CertificateFactoryTest.testV3CaCert()
* org.xwiki.crypto.pkix.internal.BcX509CertificateGeneratorFactoryTest.testGenerateEndEntitySignedCertificateVersion1()
* org.xwiki.crypto.pkix.internal.BcX509CertificateGeneratorFactoryTest.testGenerateSelfSignedCertificateVersion3WithoutExtension()
* org.xwiki.crypto.pkix.internal.BcX509CertificateGeneratorFactoryTest.testGenerateIntermediateCertificateVersion3()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSADetachedSignatureWithEmbeddedCerts()
* org.xwiki.crypto.pkix.internal.BcX509CertificateFactoryTest.testV1CaCert()
* org.xwiki.crypto.pkix.internal.BcX509CertificateFactoryTest.testV1Cert()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSADetachedSignatureWithExternalCerts()
* org.xwiki.crypto.pkix.internal.BcX509CertificateFactoryTest.testV3InterCACert()
* org.xwiki.crypto.pkix.internal.BcX509CertificateFactoryTest.testV3Cert()
* org.xwiki.crypto.pkix.internal.BcX509CertificateGeneratorFactoryTest.testGenerateSelfSignedCertificateVersion3RootCa()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testAddingCertificatesToSignature()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testPreCalculatedSignature()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSADetachedSignatureWitMixedCerts()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSASignatureWithExternalCerts()
* org.xwiki.crypto.pkix.internal.BcX509CertificateChainBuilderTest.testValidV1CertificatePath()
* org.xwiki.crypto.pkix.internal.BcX509CertificateGeneratorFactoryTest.testGenerateSelfSignedCertificateVersion1()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSASignatureAllEmbedded()
* org.xwiki.crypto.pkix.internal.BcX509CertificateGeneratorFactoryTest.testGenerateEndEntitySignedCertificateVersion3()
* org.xwiki.crypto.pkix.internal.BcX509CertificateChainBuilderTest.testValidV3CertificatePath()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

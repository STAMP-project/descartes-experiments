# Summary
**org.xwiki.crypto.signer.internal.cms.BcCMSUtils.verify(org.bouncycastle.cms.SignerInformation,org.xwiki.crypto.pkix.params.CertifiedPublicKey,org.xwiki.crypto.signer.internal.BcContentVerifierProviderBuilder,org.xwiki.crypto.DigestFactory)**

This method is **weak pseudo-tested**.
It is covered by 7 test(s). 


## Transformations applied

- false

- true


The test suite was not able to detect the following transformations:
 * true 


More information about the transformations applied can be found [here](https://github.com/STAMP-project/pitest-descartes)

## Covering tests
This method is covered by 7 test(s).
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testPreCalculatedSignature()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSADetachedSignatureWitMixedCerts()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSADetachedSignatureWithEmbeddedCerts()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSASignatureAllEmbedded()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSADetachedSignatureWithExternalCerts()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testAddingCertificatesToSignature()
* org.xwiki.crypto.signer.internal.cms.DefaultCMSSignedDataTest.testDSASignatureWithExternalCerts()


## Remarks
> Place here any remarks you have regarding this method.

## Involved commit(s)

> Place here any commit hash related to this issue.

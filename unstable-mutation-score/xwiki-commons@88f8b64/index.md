
# Module

`xwiki-commons-crypto-commons`@[88f8b64ce5b5792c1b1994bdc3060345a02225fa](https://github.com/xwiki/xwiki-commons/commit/88f8b64ce5b5792c1b1994bdc3060345a02225fa)

Executed 28 times. Attempt 29th resulted in deadlock.

# Feedback and conclusions

These tests are not supposed to be flakey but they use an entropy generator. This generator is tuned for the tests themselves (fixed entropy generation). It is possible that the entropy generator would not generate enough entropy making the tests longer to execute.

These tests should not be targeted in the analysis.

# Unstable mutations

* `null` on `org.xwiki.crypto.internal.asymmetric.generator.BcDSAKeyParameterGenerator.getUsage(I)Lorg/xwiki/crypto/params/generator/asymmetric/DSAKeyValidationParameters$Usage;` [Details](1.md) 
* `0` on `org.xwiki.crypto.internal.asymmetric.generator.BcDSAKeyParameterGenerator.getUsageIndex(Lorg/xwiki/crypto/params/generator/asymmetric/DSAKeyValidationParameters$Usage;)I` [Details](2.md) 
* `1` on `org.xwiki.crypto.internal.asymmetric.generator.BcDSAKeyParameterGenerator.getUsageIndex(Lorg/xwiki/crypto/params/generator/asymmetric/DSAKeyValidationParameters$Usage;)I` [Details](3.md) 
* `0` on `org.xwiki.crypto.params.generator.asymmetric.DSAKeyParametersGenerationParameters.getDefaultNsize(I)I` [Details](4.md) 
* `1` on `org.xwiki.crypto.params.generator.asymmetric.DSAKeyParametersGenerationParameters.getDefaultNsize(I)I` [Details](5.md) 

# Covering tests

* `org.xwiki.crypto.internal.asymmetric.generator.BcDSAKeyPairGeneratorTest.testGenerateWithoutArgument` 
* `org.xwiki.crypto.internal.FindEntropyForSecureRandomProvider.testFindGoodEntropySource` 
* `org.xwiki.crypto.internal.asymmetric.generator.BcDSAKeyPairGeneratorTest.testGenerateFIPS186_2` 
* `org.xwiki.crypto.internal.asymmetric.generator.BcDSAKeyPairGeneratorTest.testGenerateFIPS186_3` 

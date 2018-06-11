- [X] [org.ow2.authzforce.core.pdp.impl.combining.DPOverridesCombiningAlg$OverridingEffectFirstRuleCollector.hasRuleWithOverriddenEffectAndPepAction()](methods/org.ow2.authzforce.core.pdp.impl.combining.DPOverridesCombiningAlg$OverridingEffectFirstRuleCollector.hasRuleWithOverriddenEffectAndPepAction().md)
> It is part of the policy agreement and therefore involved in an important feature. Policy combining. It is critical in the policy evaluation.

- [X] [org.ow2.authzforce.core.pdp.impl.func.StandardHigherOrderBagFunctions$BooleanHigherOrderTwoBagFunction.checkNumberOfArgs(int)](methods/org.ow2.authzforce.core.pdp.impl.func.StandardHigherOrderBagFunctions$BooleanHigherOrderTwoBagFunction.checkNumberOfArgs(int).md)
> Methods like this one ensure that the policy is valid and was given the right number of parameters. Part of the initialization of the policy. Even if they are simple, their effect should be tested.

- [X] [org.ow2.authzforce.core.pdp.impl.func.StandardHigherOrderBagFunctions$AnyOfAny.checkNumberOfArgs(int)](methods/org.ow2.authzforce.core.pdp.impl.func.StandardHigherOrderBagFunctions$AnyOfAny.checkNumberOfArgs(int).md)
> Similar to the previous method.

- [X] [org.ow2.authzforce.core.pdp.impl.func.TimeRangeComparisonFunction$Call.setSameDate(java.util.Calendar,java.util.Calendar)](methods/org.ow2.authzforce.core.pdp.impl.func.TimeRangeComparisonFunction$Call.setSameDate(java.util.Calendar,java.util.Calendar).md)
> It is part of the *time in range* check. I plays an important role in date validation which is essential to the project.

- [X] [org.ow2.authzforce.core.pdp.impl.combining.DPOverridesCombiningAlg$OverridingEffectFirstRuleCollector.addFirstEmptyRuleWithOverriddenEffect(org.ow2.authzforce.core.pdp.impl.rule.RuleEvaluator)](methods/org.ow2.authzforce.core.pdp.impl.combining.DPOverridesCombiningAlg$OverridingEffectFirstRuleCollector.addFirstEmptyRuleWithOverriddenEffect(org.ow2.authzforce.core.pdp.impl.rule.RuleEvaluator).md)
> Similar to the first method. It is part of the policy combining algorithm.

- [ ] [org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestContext.putVariableIfAbsent(java.lang.String,org.ow2.authzforce.core.pdp.api.value.Value)](methods/org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestContext.putVariableIfAbsent(java.lang.String,org.ow2.authzforce.core.pdp.api.value.Value).md)
> Not so important. It supports a feature that is not used very much.

- [ ] [org.ow2.authzforce.core.pdp.impl.func.SubstringFunction.getInvalidArg1MessagePrefix(org.ow2.authzforce.core.pdp.api.func.FirstOrderFunctionSignature)](methods/org.ow2.authzforce.core.pdp.impl.func.SubstringFunction.getInvalidArg1MessagePrefix(org.ow2.authzforce.core.pdp.api.func.FirstOrderFunctionSignature).md)
> Development support.

- [ ] [org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestEvaluator.newReqMissingStdEnvAttrException(org.ow2.authzforce.core.pdp.api.AttributeFQN)](methods/org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestEvaluator.newReqMissingStdEnvAttrException(org.ow2.authzforce.core.pdp.api.AttributeFQN).md)
> It just creates an exception object.

- [X] [org.ow2.authzforce.core.pdp.impl.rule.RuleEvaluator$DenyDecisionWithPepActionResutFactory.getDecisionType()](methods/org.ow2.authzforce.core.pdp.impl.rule.RuleEvaluator$DenyDecisionWithPepActionResutFactory.getDecisionType().md)
> It is part of a core feature. The method is very simple, but its effects are important to some key features. The effects should be targeted in new test cases.

- [ ] [org.ow2.authzforce.core.pdp.impl.func.LogicalNOfFunction.getInvalidArg0MessagePrefix(org.ow2.authzforce.core.pdp.api.func.FirstOrderFunctionSignature)](methods/org.ow2.authzforce.core.pdp.impl.func.LogicalNOfFunction.getInvalidArg0MessagePrefix(org.ow2.authzforce.core.pdp.api.func.FirstOrderFunctionSignature).md)
> Development support.

> All variable related methods are not important as they are not important to a not widely used feature.

- [ ] [org.ow2.authzforce.core.pdp.impl.expression.DepthLimitingExpressionFactory.removeVariable(java.lang.String)](methods/org.ow2.authzforce.core.pdp.impl.expression.DepthLimitingExpressionFactory.removeVariable(java.lang.String).md) 


- [ ] [org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestContext.getVariableValue(java.lang.String,org.ow2.authzforce.core.pdp.api.value.Datatype)](methods/org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestContext.getVariableValue(java.lang.String,org.ow2.authzforce.core.pdp.api.value.Datatype).md)

- [ ] [org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestContext.removeVariable(java.lang.String)](methods/org.ow2.authzforce.core.pdp.impl.IndividualDecisionRequestContext.removeVariable(java.lang.String).md)


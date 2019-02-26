This directory contains reports generated to diagnose the xwiki-commons stability issue un the mutation score. See [here](STAMP-project/pitest-descartes#62).

## Remarks

There is a difference on how the initial scores were computed. PIT was configured in `xwiki/xwiki-commons@cb0ff74` to use Junit 4. In `xwiki/xwiki-commons@0a7d7ee` the configuration switched to Junit 5. This was done on 22-05-2018. The same day were reported significant differences in the score, which are the ones listed in the initial description of this issue.
Here is a summary of the issues and the outcome when trying to reproduce it.

| Commit                        | Score change  | Outcome |
|-------------------------------|---------------|---------|
| `xwiki/xwiki-commons@88f8b64` | from 68 to 40 | Score unstable but with no significant change. Might be due to some tuned test cases. | 
| `xwiki/xwiki-commons@85c9c98` | from 67 to 36 | Score stable at 36% after 100 executions. |
| `xwiki/xwiki-commons@574c333` | from 40 to 39 | Same as `xwiki/xwiki-commons@88f8b64` |
| `xwiki/xwiki-commons@f5394b4` | from 21 to 11 | Score stable at 11% after 100 executions. |
| `xwiki/xwiki-commons@2032022` | from 20 to 0  | Score stable at 0% (no coverage) after 30 executions. |

As hinted by the configuration issue for `xwiki/xwiki-commons@2032022` the drastic score change could be explained by the change of test plugin for PIT from Junit 4 to Junit 5. The Junit 5 plugin is not as stable as the other and may be missing some tests.
`xwiki/xwiki-commons@2032022` should be solved by adding Junit 5 to the module configuration.
The actual unstable score from `xwiki/xwiki-commons@88f8b64` and `xwiki/xwiki-commons@574c333` should be solved by removing the test cases identified as problematic (entropy generation).

The issue from `xwiki/xwikiplatform@d2b8e20` is different. In this case, the score is unstable but not due to timeouts. Two mutations have been detected as unstable. Their status goes from `KILLED` to `SURVIVED`. The test code seems to deal with files. If this is the case, then the state of the file system might be unstable after the analysis of a mutant. This is even worst if the mutants are analyzed in parallel, as it seems to be the case.

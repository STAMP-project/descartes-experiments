

Taken from the [DetectionStatus definition](https://github.com/hcoles/pitest/blob/57af81af9e4914c4f89c34af485c2342ec6e6a9e/pitest/src/main/java/org/pitest/mutationtest/DetectionStatus.java)

| Mutation Status | Detected | Reason |
|-----------------|----------|--------|
| `KILLED`        | `true`   | Mutation was detected by a test.  |
| `SURVIVED`      | `false`  | No test failed in the presence of the mutation |
| `TIMED_OUT`     | `true`   | A test took a long time to run when mutation was present, might indicate an that the mutation caused an infinite loop but we don't know for sure. |
| `NON_VIABLE`    | `true`   | Mutation could not be loaded into the jvm. Should never happen. |
| `MEMORY_ERROR`  | `true`   | JVM ran out of memory while processing a mutation. Might indicate that the mutation increases| memory usage but we don't know for sure. |
| `NOT_STARTED`   | `false`  | Mutation not yet assessed. For internal use only. |
| `STARTED`       | `false`  | Processing of mutation has begun but not yet fully assessed. For internal use only. |
| `RUN_ERROR`     | `true`   | Something went wrong. Don't know what but it was probably bad. |
| `NO_COVERAGE`   | `false`  | Mutation is not covered by any test. |


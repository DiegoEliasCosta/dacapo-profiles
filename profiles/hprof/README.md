# HPROF Profiles

HPROF profiles provide a dirty first look into the performance of an application.

We generated the profile through 2 methods:
- Sampling: Threads are sampled every 1ms and their stacktrace is inspected
- Profiling: Application code is instrumented and every method outputs its execution time and count metrics.
  - Profiling is more precise but it is considerably slower - 2 orders of magnitude at least
  
  
Environment:

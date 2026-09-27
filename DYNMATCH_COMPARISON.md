# DynMatch interoperability

The repository can export its repair-stress and application workloads into the exact input format documented by DynMatch.

Generate streams:

```bash
python experiments/export_dynmatch.py
```

Build DynMatch according to its upstream README, then run the same stream with established implementations, for example:

```bash
dynmatch datasets/dynmatch/hub_repair_n1024.graph --algorithm=neimansolomon
dynmatch datasets/dynmatch/hub_repair_n1024.graph --algorithm=baswanaguptasen -seed=1
dynmatch datasets/dynmatch/hub_repair_n1024.graph --algorithm=randomwalk -seed=1
```

Use multiple seeds for randomized algorithms. Record wall-clock time, maintained matching size, and any statistics exposed by DynMatch. Do not compare its native C++ wall-clock time directly to Python timing as an algorithmic complexity claim; use common-machine timing as an engineering comparison and DMRC's instrumented work as the mechanism analysis.

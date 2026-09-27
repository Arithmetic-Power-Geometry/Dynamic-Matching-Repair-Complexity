import os,csv,math
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("artifacts/output",exist_ok=True)
df=pd.read_csv("results/benchmark.csv")
summary=df.groupby("algorithm",as_index=False).agg(
    median_time_s=("time_s","median"),
    median_work=("work","median"),
    median_recourse=("recourse","median"),
    all_maximal=("maximal","min"))
summary.to_csv("artifacts/output/table_performance.csv",index=False)

fig,ax=plt.subplots(figsize=(8,5))
for name,g in df.groupby("algorithm"):
    x=g.groupby("n")["work"].median()
    ax.plot(x.index,x.values,marker="o",label=name)
ax.set_xlabel("Number of vertices n");ax.set_ylabel("Median instrumented work")
ax.set_title("Dynamic maximal-matching maintenance: baseline comparison")
ax.legend();fig.tight_layout()
fig.savefig("artifacts/output/figure_performance.png",dpi=220)
plt.close(fig)

with open("artifacts/output/algorithm.md","w") as f:
    f.write("""# Algorithm 1: Heavy/light repair witness maintenance

**Input:** dynamic graph G, maximal matching M, threshold T.

1. Classify vertex v as light if deg(v) <= T; otherwise heavy.
2. For every heavy vertex h, maintain a set of currently free neighbors.
3. When a vertex changes matched/free state, update only summaries of its heavy neighbors.
4. When a free light vertex requires repair, scan its at-most-T neighbors.
5. When a free heavy vertex requires repair, query its maintained free-neighbor witness.
6. If a free neighbor is found, match the pair; otherwise certify no local free-free edge at that vertex.
7. Rebuild classifications periodically if degree drift exceeds the chosen epoch rule.

Instrumentation records adjacency probes, summary-propagation work, and matching recourse separately.
""")
print(summary)
print("wrote artifacts/output/*")

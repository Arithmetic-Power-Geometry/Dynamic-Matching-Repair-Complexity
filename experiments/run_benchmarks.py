import os,sys,random,time,csv
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *

def make_graph(n,p,seed):
    r=random.Random(seed); G=DynamicGraph(n)
    for u in range(n):
        for v in range(u+1,n):
            if r.random()<p:G.add_edge(u,v)
    return G

def clone(G):
    H=DynamicGraph(G.n)
    for u,v in G.edges():H.add_edge(u,v)
    return H

def updates(G,k,seed):
    r=random.Random(seed); out=[]
    for _ in range(k):
        u,v=r.sample(range(G.n),2)
        if u>v:u,v=v,u
        op="del" if G.has_edge(u,v) else "add"
        out.append((op,u,v))
        if op=="add":G.add_edge(u,v)
        else:G.remove_edge(u,v)
    return out

def run_one(n,p,k,seed):
    base=make_graph(n,p,seed)
    seq=updates(clone(base),k,seed+99)
    algs=[
      ("recompute",RecomputeMatcher(clone(base))),
      ("scan",ScanRepairMatcher(clone(base))),
      ("eager",EagerCounterMatcher(clone(base))),
      ("heavy_light",HeavyLightMatcher(clone(base))),
    ]
    rows=[]
    for name,a in algs:
        a.initialize_greedy()
        t=time.perf_counter()
        ok=True
        for op,u,v in seq:
            a.update(op,u,v)
            ok &= a.is_maximal()
        elapsed=time.perf_counter()-t
        rows.append(dict(n=n,p=p,updates=k,algorithm=name,time_s=elapsed,
          probes=a.metrics.probes,propagation=a.metrics.propagation,
          work=a.metrics.probes+a.metrics.propagation,
          recourse=a.metrics.recourse,maximal=int(ok)))
    return rows

os.makedirs("results",exist_ok=True)
rows=[]
for n in [64,128,256,512]:
    for p in [0.02,0.05,0.10]:
        rows += run_one(n,p,300,7+n)
with open("results/benchmark.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote results/benchmark.csv",len(rows))

"""Export identical DMRC workloads in DynMatch's dynamic graph format.
DynMatch format: first line '# <nodes> <updates>'; then 1 u v insert, 0 u v delete.
"""
import os,sys,random
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
from generators import hub_graph

def clone(G):
 H=DynamicGraph(G.n)
 for e in G.edges(): H.add_edge(*e)
 return H

def write_stream(path,n,initial,updates):
 # DynMatch consumes an update stream, so initial graph is represented as insertions.
 ops=[(1,u,v) for u,v in initial]+[(1 if op=="add" else 0,u,v) for op,u,v in updates]
 with open(path,"w") as f:
  f.write(f"# {n} {len(ops)}\n")
  for op,u,v in ops:f.write(f"{op} {u} {v}\n")

os.makedirs("datasets/dynmatch",exist_ok=True)
for n in [128,256,512,1024,2048]:
 G=hub_graph(n); initial=list(G.edges())
 a=ScanRepairMatcher(clone(G));a.initialize_greedy()
 matched=[(u,v) for u,v in enumerate(a.mate) if v>u]
 q=[]
 for i in range(250):
  u,v=matched[i%len(matched)];q += [("del",u,v),("add",u,v)]
 write_stream(f"datasets/dynmatch/hub_repair_n{n}.graph",n,initial,q)

# Request-resource application
R=S=500;G=DynamicGraph(R+S);rng=random.Random(17)
for r in range(R):
 for s in rng.sample(range(R,R+S),25):G.add_edge(r,s)
initial=list(G.edges());a=ScanRepairMatcher(clone(G));a.initialize_greedy()
matched=[(u,v) for u,v in enumerate(a.mate) if v>u];q=[]
for i in range(750):
 u,v=matched[i%len(matched)];q += [("del",u,v),("add",u,v)]
write_stream("datasets/dynmatch/resource_allocation_1000.graph",R+S,initial,q)
print("DynMatch-compatible streams generated.")

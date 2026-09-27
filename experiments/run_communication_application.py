"""Communication-pairing stress application.

Models endpoints with a few high-degree relay/gateway vertices. Repeated loss and restoration
of matched links exercises latency-sensitive local repair. Results are mechanism-level and
must not be interpreted as a complete networking protocol.
"""
import os,sys,csv,statistics,time
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
from generators import hub_graph

def clone(G):
 H=DynamicGraph(G.n)
 for e in G.edges():H.add_edge(*e)
 return H

rows=[]
for n in [256,512,1024,2048]:
 base=hub_graph(n,hubs=8)
 seed=ScanRepairMatcher(clone(base));seed.initialize_greedy()
 matched=[(u,v) for u,v in enumerate(seed.mate) if v>u];q=[]
 for i in range(500):
  u,v=matched[i%len(matched)];q += [("del",u,v),("add",u,v)]
 for name,C in [("scan",ScanRepairMatcher),("eager",EagerCounterMatcher),("heavy_light",HeavyLightMatcher)]:
  a=C(clone(base));a.initialize_greedy();a.metrics=Metrics();per=[];t=time.perf_counter();ok=True
  for op,u,v in q:
   w=a.metrics.probes+a.metrics.propagation;a.update(op,u,v);per.append(a.metrics.probes+a.metrics.propagation-w);ok &= a.is_maximal()
  rows.append(dict(application="communication_pairing",n=n,algorithm=name,updates=len(q),
   time_s=time.perf_counter()-t,total_work=sum(per),median_work=statistics.median(per),
   p95_work=sorted(per)[int(.95*len(per))-1],max_work=max(per),recourse=a.metrics.recourse,maximal=int(ok)))
os.makedirs("results",exist_ok=True)
with open("results/communication_application.csv","w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote",len(rows),"application rows")

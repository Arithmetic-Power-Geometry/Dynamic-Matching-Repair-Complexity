import os,sys,csv,math,statistics
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
from generators import hub_graph

def clone(G):
 H=DynamicGraph(G.n)
 for e in G.edges():H.add_edge(*e)
 return H

rows=[]
for n in [128,256,512,1024,2048]:
 base=hub_graph(n)
 seed=ScanRepairMatcher(clone(base));seed.initialize_greedy()
 matched=[(u,v) for u,v in enumerate(seed.mate) if v>u]
 q=[]
 for i in range(250):
  u,v=matched[i%len(matched)];q += [("del",u,v),("add",u,v)]
 thresholds=sorted(set([2,4,8,16,32,64,int(math.sqrt(n)),max(2,2*int(math.sqrt(n)))]))
 for T in thresholds:
  a=HeavyLightMatcher(clone(base),threshold=T);a.initialize_greedy();a.metrics=Metrics();per=[];ok=True
  for op,u,v in q:
   w=a.metrics.probes+a.metrics.propagation;a.update(op,u,v);per.append(a.metrics.probes+a.metrics.propagation-w);ok &= a.is_maximal()
  rows.append(dict(n=n,threshold=T,total_work=sum(per),median_work=statistics.median(per),
    p95_work=sorted(per)[int(.95*len(per))-1],max_work=max(per),recourse=a.metrics.recourse,maximal=int(ok)))
os.makedirs("results",exist_ok=True)
with open("results/threshold_sweep.csv","w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote threshold sweep",len(rows))

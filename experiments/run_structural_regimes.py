import os,sys,csv,math,statistics
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
from structural_generators import clustered_hubs,regular_ring

def clone(G):
 H=DynamicGraph(G.n)
 for e in G.edges():H.add_edge(*e)
 return H
def hx(a,x):return sum(1 for y in a.G.adj[x] if a.heavy[y])
rows=[]
for n in [256,512,1024,2048]:
 for family,G in [("disjoint_hubs",clustered_hubs(n,8,False)),("shared_hubs",clustered_hubs(n,8,True)),("regular",regular_ring(n,16))]:
  s=ScanRepairMatcher(clone(G));s.initialize_greedy();matched=[(u,v) for u,v in enumerate(s.mate) if v>u]
  q=[]
  for i in range(min(300,len(matched)*4)):
   u,v=matched[i%len(matched)];q += [("del",u,v),("add",u,v)]
  for T in sorted(set([4,8,16,32,int(math.sqrt(n)),2*int(math.sqrt(n))])):
   a=HeavyLightMatcher(clone(G),threshold=T);a.initialize_greedy();a.metrics=Metrics();per=[];hs=[]
   for op,u,v in q:
    hs.extend([hx(a,u),hx(a,v)]);w=a.metrics.probes+a.metrics.propagation;a.update(op,u,v);per.append(a.metrics.probes+a.metrics.propagation-w)
   rows.append(dict(family=family,n=n,T=T,max_H=max(hs) if hs else 0,mean_H=sum(hs)/len(hs) if hs else 0,
    total_work=sum(per),median_work=statistics.median(per),p95_work=sorted(per)[int(.95*len(per))-1],max_work=max(per),maximal=int(a.is_maximal())))
os.makedirs("results",exist_ok=True)
with open("results/structural_regimes.csv","w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote",len(rows),"structural-regime rows")

import os,sys,csv,math
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
from structural_generators import clustered_hubs,regular_ring

def clone(G):
 H=DynamicGraph(G.n)
 for e in G.edges():H.add_edge(*e)
 return H
rows=[]
for n in [256,512,1024,2048]:
 for fam,G in [("disjoint_hubs",clustered_hubs(n,8,False)),("shared_hubs",clustered_hubs(n,8,True)),("regular",regular_ring(n,16))]:
  seed=ScanRepairMatcher(clone(G));seed.initialize_greedy();matched=[(u,v) for u,v in enumerate(seed.mate) if v>u]
  q=[]
  for i in range(min(400,max(1,len(matched))*4)):
   u,v=matched[i%len(matched)];q += [("del",u,v),("add",u,v)]
  for T in sorted(set([4,8,16,32,int(math.sqrt(n)),2*int(math.sqrt(n))])):
   a=HeavyLightMatcher(clone(G),threshold=T);a.initialize_greedy();a.metrics=Metrics()
   for step,(op,u,v) in enumerate(q):
    deg_u=len(a.G.adj[u]);deg_v=len(a.G.adj[v])
    Hu=sum(a.heavy[y] for y in a.G.adj[u]);Hv=sum(a.heavy[y] for y in a.G.adj[v])
    p=a.metrics.probes;s=a.metrics.propagation;r=a.metrics.recourse
    a.update(op,u,v)
    rows.append(dict(family=fam,n=n,T=T,step=step,op=op,u=u,v=v,
      deg_u=deg_u,deg_v=deg_v,H_u=Hu,H_v=Hv,heavy_u=int(a.heavy[u]),heavy_v=int(a.heavy[v]),
      probes=a.metrics.probes-p,propagation=a.metrics.propagation-s,
      work=(a.metrics.probes-p)+(a.metrics.propagation-s),recourse=a.metrics.recourse-r,
      maximal=int(a.is_maximal())))
os.makedirs("results",exist_ok=True)
with open("results/event_level.csv","w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote",len(rows),"event rows")

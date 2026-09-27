import os,sys,random,time,csv,statistics
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
def er(n,p,s):
 r=random.Random(s);G=DynamicGraph(n)
 for u in range(n):
  for v in range(u+1,n):
   if r.random()<p:G.add_edge(u,v)
 return G
def hub(n,h=4):
 G=DynamicGraph(n)
 for u in range(h):
  for v in range(h,n):G.add_edge(u,v)
 for v in range(h,n-1,2):G.add_edge(v,v+1)
 return G
def clone(G):
 H=DynamicGraph(G.n)
 for e in G.edges():H.add_edge(*e)
 return H
def stream(G,k,s):
 r=random.Random(s);q=[]
 for _ in range(k):
  u,v=r.sample(range(G.n),2);u,v=min(u,v),max(u,v);op="del" if G.has_edge(u,v) else "add";q.append((op,u,v))
  (G.remove_edge if op=="del" else G.add_edge)(u,v)
 return q
def case(fam,n,p,k,s):
 base=er(n,p,s) if fam=="er" else hub(n);q=stream(clone(base),k,s+99);rows=[]
 for name,C in [("recompute",RecomputeMatcher),("scan",ScanRepairMatcher),("eager",EagerCounterMatcher),("heavy_light",HeavyLightMatcher)]:
  x=C(clone(base));x.initialize_greedy();x.metrics=Metrics();per=[];t=time.perf_counter();ok=True
  for op,u,v in q:
   z=x.metrics.probes+x.metrics.propagation;x.update(op,u,v);per.append(x.metrics.probes+x.metrics.propagation-z);ok &= x.is_maximal()
  rows.append(dict(family=fam,n=n,p=p,updates=k,algorithm=name,time_s=time.perf_counter()-t,probes=x.metrics.probes,propagation=x.metrics.propagation,work=sum(per),median_work_update=statistics.median(per),p95_work_update=sorted(per)[int(.95*len(per))-1],max_work_update=max(per),recourse=x.metrics.recourse,maximal=int(ok)))
 return rows
os.makedirs("results",exist_ok=True);rows=[]
for n in [64,128,256,512,1024]:
 for p in [.01,.03,.08]:rows+=case("er",n,p,500,1000+n+int(p*100))
 rows+=case("hub",n,0,500,2000+n)
with open("results/benchmark.csv","w",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote",len(rows),"rows")

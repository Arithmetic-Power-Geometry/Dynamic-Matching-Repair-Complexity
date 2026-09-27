import os,sys,random,csv,time,statistics
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
def clone(G):
 H=DynamicGraph(G.n)
 for e in G.edges():H.add_edge(*e)
 return H
R=S=500;G=DynamicGraph(R+S);r=random.Random(17)
for u in range(R):
 for v in r.sample(range(R,R+S),25):G.add_edge(u,v)
shadow=clone(G);q=[]
for _ in range(1500):
 u=r.randrange(R);v=r.randrange(R,R+S);op="del" if shadow.has_edge(u,v) else "add";q.append((op,u,v));(shadow.remove_edge if op=="del" else shadow.add_edge)(u,v)
rows=[]
for name,C in [("recompute",RecomputeMatcher),("scan",ScanRepairMatcher),("eager",EagerCounterMatcher),("heavy_light",HeavyLightMatcher)]:
 x=C(clone(G));x.initialize_greedy();x.metrics=Metrics();before=x.matching_size();per=[];t=time.perf_counter()
 for op,u,v in q:z=x.metrics.probes+x.metrics.propagation;x.update(op,u,v);per.append(x.metrics.probes+x.metrics.propagation-z)
 rows.append(dict(scenario="request_resource_allocation",algorithm=name,vertices=R+S,updates=len(q),matching_before=before,matching_after=x.matching_size(),time_s=time.perf_counter()-t,total_work=sum(per),median_work_update=statistics.median(per),p95_work_update=sorted(per)[int(.95*len(per))-1],recourse=x.metrics.recourse,maximal=int(x.is_maximal())))
os.makedirs("results",exist_ok=True)
with open("results/application_demo.csv","w",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote application comparison")

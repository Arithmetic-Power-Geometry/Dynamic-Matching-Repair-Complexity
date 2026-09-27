import argparse,os,sys,csv,time,statistics,math
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import DynamicGraph,Metrics,ScanRepairMatcher,EagerCounterMatcher,HeavyLightMatcher
from temporal_adapter import read_temporal,native_events,window_events
ap=argparse.ArgumentParser();ap.add_argument("path");ap.add_argument("--mode",choices=["native","window"],default="native");ap.add_argument("--window",type=float,default=86400);ap.add_argument("--limit",type=int,default=0);ap.add_argument("--name",default="external");a=ap.parse_args()
n,raw=read_temporal(a.path);ev=native_events(raw) if a.mode=="native" else window_events(raw,a.window)
if a.limit:ev=ev[:a.limit]
rows=[]
for cls,name in [(ScanRepairMatcher,"scan"),(EagerCounterMatcher,"eager"),(HeavyLightMatcher,"heavy_light")]:
 G=DynamicGraph(n); alg=cls(G,threshold=max(2,int(math.sqrt(max(1,n))))) if name=="heavy_light" else cls(G);alg.initialize_greedy();alg.metrics=Metrics();per=[];update_time=0
 for e in ev:
  before=alg.metrics.probes+alg.metrics.propagation;t=time.perf_counter();alg.update(e.op,e.u,e.v);update_time+=time.perf_counter()-t;per.append(alg.metrics.probes+alg.metrics.propagation-before)
 ok=alg.is_maximal()
 q=lambda p: sorted(per)[min(len(per)-1,int(p*(len(per)-1)))] if per else 0
 rows.append(dict(dataset=a.name,mode=a.mode,n=n,events=len(ev),algorithm=name,update_time_s=update_time,total_work=sum(per),median_work=statistics.median(per) if per else 0,p95_work=q(.95),p99_work=q(.99),max_work=max(per) if per else 0,recourse=alg.metrics.recourse,maximal=int(ok)))
os.makedirs("results",exist_ok=True);out=f"results/real_{a.name}_{a.mode}.csv"
with open(out,"w",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print(*rows,sep="\n");print("wrote",out)

import argparse,os,sys,csv,time,math,statistics
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import DynamicGraph,Metrics,ScanRepairMatcher,EagerCounterMatcher,HeavyLightMatcher
from dynmatch_seq import read_dynmatch_seq
p=argparse.ArgumentParser();p.add_argument("path");p.add_argument("--name",default="dynmatch_real");p.add_argument("--limit",type=int,default=0);a=p.parse_args()
n,declared,ev=read_dynmatch_seq(a.path,a.limit);rows=[]
for cls,name in [(ScanRepairMatcher,"scan"),(EagerCounterMatcher,"eager"),(HeavyLightMatcher,"heavy_light")]:
 alg=cls(DynamicGraph(n),threshold=max(2,int(math.sqrt(n)))) if name=="heavy_light" else cls(DynamicGraph(n));alg.initialize_greedy();alg.metrics=Metrics();per=[];elapsed=0
 for e in ev:
  b=alg.metrics.probes+alg.metrics.propagation;t=time.perf_counter();alg.update(e.op,e.u,e.v);elapsed+=time.perf_counter()-t;per.append(alg.metrics.probes+alg.metrics.propagation-b)
 s=sorted(per);q=lambda z:s[min(len(s)-1,int(z*(len(s)-1)))] if s else 0
 rows.append(dict(dataset=a.name,n=n,declared_updates=declared,replayed_updates=len(ev),algorithm=name,update_time_s=elapsed,total_work=sum(per),median_work=statistics.median(per) if per else 0,p95_work=q(.95),p99_work=q(.99),max_work=max(per) if per else 0,recourse=alg.metrics.recourse,maximal=int(alg.is_maximal())))
os.makedirs("results",exist_ok=True);out=f"results/dynmatch_{a.name}.csv"
with open(out,"w",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(*rows,sep="\n");print("wrote",out)

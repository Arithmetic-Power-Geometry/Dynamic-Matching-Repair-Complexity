import os,sys,csv
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
from generators import star_of_pairs

def run(k,rounds,bf,rf):
 G,e=star_of_pairs(k);a=AdaptiveDebtMatcher(G,bf,rf)
 a.mate=[-1]*G.n;a._match(0,1)
 for i in range(k):x=2+2*i;a._match(x,x+1)
 per=[]
 for r in range(rounds):
  b=a.metrics.probes+a.metrics.propagation;a.update("del",*e);per.append(a.metrics.probes+a.metrics.propagation-b)
  b=a.metrics.probes+a.metrics.propagation;a.update("add",*e);per.append(a.metrics.probes+a.metrics.propagation-b)
 return sum(per),max(per),int(a.validate_invariants())
rows=[]
for bf in [.5,1,2,4]:
 for rf in [1,2,4]:
  total=mx=0;ok=1
  for k in [32,64,128,256]:
   w,m,v=run(k,50,bf,rf);total+=w;mx=max(mx,m);ok&=v
  rows.append(dict(build_factor=bf,retire_factor=rf,total_work=total,max_work=mx,valid=ok))
rows.sort(key=lambda r:(r["total_work"],r["max_work"]))
os.makedirs("results",exist_ok=True)
with open("results/adaptive_training.csv","w",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(rows)

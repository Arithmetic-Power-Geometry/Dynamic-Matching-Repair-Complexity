"""Compute exact Q decomposition at every repair event from a trace."""
import csv,argparse,collections,statistics
p=argparse.ArgumentParser();p.add_argument("trace");p.add_argument("out");a=p.parse_args()
by=collections.defaultdict(list)
with open(a.trace) as f:
 for r in csv.DictReader(f):
  for x in ["step","vertex","degree","scan_work","repair_number","inter_repair_gap"]:r[x]=int(r[x])
  by[r["vertex"]].append(r)
rows=[]
for v,ev in by.items():
 ev.sort(key=lambda x:x["step"])
 for j,e0 in enumerate(ev):
  d0=e0["degree"];future=ev[j+1:];k=len(future)
  vals=[]
  for e in future:
   di=e["degree"];si=e["scan_work"];ai=(si/di if di>0 else 0.0);gi=(di/d0 if d0>0 else 0.0)
   vals.append((ai,gi))
  q=(sum(e["scan_work"] for e in future)/d0 if d0>0 else 0.0)
  A=(sum(x[0] for x in vals)/k if k else 0.0);G=(sum(x[1] for x in vals)/k if k else 0.0)
  cov=(sum((x[0]-A)*(x[1]-G) for x in vals)/k if k else 0.0)
  q_identity=k*(A*G+cov)
  rows.append(dict(vertex=v,step=e0["step"],degree0=d0,future_repairs=k,
    mean_scan_intensity=A,mean_degree_drift=G,cov_intensity_drift=cov,
    Q=q,Q_identity=q_identity,break_even=int(q>1)))
with open(a.out,"w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
err=max((abs(r["Q"]-r["Q_identity"]) for r in rows),default=0)
print("events",len(rows),"max_identity_error",err,"break_even",sum(r["break_even"] for r in rows))

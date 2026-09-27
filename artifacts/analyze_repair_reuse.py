"""Analyze whether repair work at a vertex is recurrent enough to justify indexing."""
import csv,collections,statistics,argparse
p=argparse.ArgumentParser();p.add_argument("trace");p.add_argument("--out",default="results/repair_reuse_summary.csv");a=p.parse_args()
by=collections.defaultdict(list)
with open(a.trace) as f:
 for r in csv.DictReader(f):
  r["step"]=int(r["step"]);r["degree"]=int(r["degree"]);r["scan_work"]=int(r["scan_work"]);r["inter_repair_gap"]=int(r["inter_repair_gap"])
  by[int(r["vertex"])].append(r)
rows=[]
for v,ev in by.items():
 ev.sort(key=lambda x:x["step"]);works=[x["scan_work"] for x in ev];gaps=[x["inter_repair_gap"] for x in ev if x["inter_repair_gap"]>=0]
 # Oracle break-even diagnostic: after each repair, compare all later scan work
 # with degree-at-activation as the optimistic one-time build cost.
 best_ratio=0.0
 suffix=sum(works)
 for e in ev:
  suffix-=e["scan_work"];cost=max(1,e["degree"]);best_ratio=max(best_ratio,suffix/cost)
 rows.append(dict(vertex=v,repairs=len(ev),total_scan_work=sum(works),max_scan_work=max(works),
   median_gap=statistics.median(gaps) if gaps else -1,min_gap=min(gaps) if gaps else -1,
   max_degree=max(x["degree"] for x in ev),oracle_best_future_scan_to_build=best_ratio,
   oracle_indexable=int(best_ratio>1.0)))
with open(a.out,"w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys() if rows else ["vertex"]);w.writeheader();w.writerows(rows)
print("vertices_with_repairs",len(rows))
print("repeated_vertices",sum(r["repairs"]>1 for r in rows))
print("oracle_indexable_vertices",sum(r["oracle_indexable"] for r in rows))

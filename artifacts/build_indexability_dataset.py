"""Build pre-repair features and optimistic future-indexability labels.
Label y=1 iff future scan work after this repair exceeds current build degree.
Features use history available before/at the current repair only.
"""
import csv,collections,argparse
p=argparse.ArgumentParser();p.add_argument("trace");p.add_argument("out");a=p.parse_args()
by=collections.defaultdict(list)
with open(a.trace) as f:
 for r in csv.DictReader(f):
  for k in ["step","vertex","degree","scan_work","repair_number","inter_repair_gap"]:r[k]=int(r[k])
  by[r["vertex"]].append(r)
out=[]
for v,ev in by.items():
 ev.sort(key=lambda x:x["step"]);suffix=sum(x["scan_work"] for x in ev)
 cum=0;prev_work=0;prev_deg=0
 for i,e in enumerate(ev):
  suffix-=e["scan_work"]
  out.append(dict(step=e["step"],vertex=v,degree=e["degree"],
   repair_count_before=i,cumulative_scan_before=cum,previous_scan_work=prev_work,
   inter_repair_gap=e["inter_repair_gap"],degree_change=e["degree"]-prev_deg if i else 0,
   label_oracle_indexable=int(suffix>max(1,e["degree"]))))
  cum+=e["scan_work"];prev_work=e["scan_work"];prev_deg=e["degree"]
with open(a.out,"w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
print("events",len(out),"positives",sum(x["label_oracle_indexable"] for x in out))

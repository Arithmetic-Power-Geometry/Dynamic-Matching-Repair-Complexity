"""Discovery-profile analysis for RepairTraceMatcher CSV output.
Uses only exactly observed quantities; does not infer theorem variable r.
"""
import csv,argparse,statistics,collections,math
p=argparse.ArgumentParser()
p.add_argument("trace"); p.add_argument("--dataset",required=True); p.add_argument("--out",required=True)
a=p.parse_args()
rows=[]
with open(a.trace,newline="") as f:
    for x in csv.DictReader(f):
        d=int(x["degree"]); w=int(x["scan_work"]); found=int(x["found"])
        rows.append(dict(degree=d,work=w,found=found,
                         repeat=int(x["repair_number"])>1,
                         intensity=(w/d if d else 0.0)))
def q(vals,p):
    if not vals:return 0.0
    s=sorted(vals); return s[min(len(s)-1,int((len(s)-1)*p))]
def summarize(label,arr):
    works=[x["work"] for x in arr]; ints=[x["intensity"] for x in arr]; deg=[x["degree"] for x in arr]
    return dict(dataset=a.dataset,group=label,events=len(arr),
      total_discovery=sum(works),mean_discovery=(sum(works)/len(arr) if arr else 0),
      p50_discovery=q(works,.5),p95_discovery=q(works,.95),p99_discovery=q(works,.99),
      mean_degree=(sum(deg)/len(arr) if arr else 0),
      mean_scan_intensity=(sum(ints)/len(arr) if arr else 0),
      p50_scan_intensity=q(ints,.5),p95_scan_intensity=q(ints,.95),
      full_scan_fraction=(sum(x["degree"]>0 and x["work"]>=x["degree"] for x in arr)/len(arr) if arr else 0),
      found_fraction=(sum(x["found"] for x in arr)/len(arr) if arr else 0))
groups=[("all",rows),("found", [x for x in rows if x["found"]]),
        ("none",[x for x in rows if not x["found"]]),
        ("first",[x for x in rows if not x["repeat"]]),
        ("repeat",[x for x in rows if x["repeat"]])]
# logarithmic degree bands
for lo,hi in [(0,0),(1,4),(5,16),(17,64),(65,256),(257,10**18)]:
    groups.append((f"degree_{lo}_{hi if hi<10**18 else 'plus'}",
                   [x for x in rows if lo<=x["degree"]<=hi]))
out=[summarize(n,x) for n,x in groups]
with open(a.out,"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
for r in out: print(r)

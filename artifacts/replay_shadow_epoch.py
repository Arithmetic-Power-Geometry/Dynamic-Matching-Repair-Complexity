"""Replay a projected dynamic edge stream through ShadowEpochMatcher.

Input CSV columns: op,u,v where op is add/remove (also accepts +1/-1).
Node IDs may be arbitrary strings; they are remapped deterministically by first appearance.
"""
import csv,argparse,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import DynamicGraph
from dirty_shadow_epoch import DirtyShadowEpochMatcher

p=argparse.ArgumentParser()
p.add_argument("stream")
p.add_argument("--out",required=True)
a=p.parse_args()

ops=[]; ids={}
def nid(x):
    if x not in ids: ids[x]=len(ids)
    return ids[x]
with open(a.stream,newline="") as f:
    for r in csv.DictReader(f):
        op=r["op"].strip().lower()
        if op in {"+1","+","insert","add"}: op="add"
        elif op in {"-1","-","delete","remove"}: op="remove"
        else: raise ValueError("unknown op "+op)
        u,v=nid(r["u"]),nid(r["v"])
        if u!=v: ops.append((op,u,v,r.get("phase","dynamic").strip().lower()))
G=DynamicGraph(len(ids)); M=DirtyShadowEpochMatcher(G)
for op,u,v in ops: M.update(op,u,v)
fields=["step","vertex","degree","discovery","found","r_changed_common",
        "neighbors_added","neighbors_removed","changed_plus_churn","scan_intensity"]
with open(a.out,"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(M.epoch_trace)
print("nodes",len(ids),"updates",len(dynamic) if initial else len(ops),"repair_events",len(M.epoch_trace),
      "probes",M.metrics.probes,"recourse",M.metrics.recourse,
      "matching_size",M.matching_size(),"maximal",int(M.is_maximal()))

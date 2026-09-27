"""Replay a projected dynamic edge stream through the validated dirty shadow tracker.

Input CSV columns: op,u,v and optional phase. phase may be initial or dynamic.
Without phase, every row is treated as a measured dynamic update.
Node IDs may be arbitrary strings and are remapped deterministically by first appearance.
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
        phase=(r.get("phase") or "dynamic").strip().lower()
        if phase not in {"initial","dynamic"}:
            raise ValueError("unknown phase "+phase)
        if u!=v: ops.append((op,u,v,phase))

initial=[x for x in ops if x[3]=="initial"]
dynamic=[x for x in ops if x[3]=="dynamic"]
G=DynamicGraph(len(ids)); M=DirtyShadowEpochMatcher(G)

if initial:
    for op,u,v,_ in initial:
        if op!="add":
            raise ValueError("initial phase must contain only additions")
        G.add_edge(u,v)
    M.initialize_greedy()
    # Initialization establishes state but is not part of measured work.
    M.metrics.probes=0; M.metrics.propagation=0; M.metrics.recourse=0

for op,u,v,_ in dynamic:
    M.update(op,u,v)

fields=["step","vertex","degree","discovery","found","r_changed_common",
        "neighbors_added","neighbors_removed","changed_plus_churn","scan_intensity"]
os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
with open(a.out,"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(M.epoch_trace)
print("nodes",len(ids),"initial_edges",len(initial),"updates",len(dynamic),
      "repair_events",len(M.epoch_trace),"probes",M.metrics.probes,
      "recourse",M.metrics.recourse,"matching_size",M.matching_size(),
      "maximal",int(M.is_maximal()))

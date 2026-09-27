"""Reconstruct the frozen DMRC AS-CAIDA dynamic stream from SNAP's 122 snapshots.

Usage:
  python artifacts/reconstruct_caida.py as-caida.tar.gz --out data/caida_projected.csv

Acceptance gate for the previously reported DMRC benchmark:
  snapshots=122
  initial_edges=32955
  total_updates=542194
  insertions=281050
  deletions=261144
If these do not match, STOP: do not compare shadow statistics with frozen results.
"""
import argparse,tarfile,gzip,io,csv,re,os
p=argparse.ArgumentParser();p.add_argument("archive");p.add_argument("--out",required=True);a=p.parse_args()

def parse_edges(b):
    E=set()
    for raw in b.decode("utf-8","ignore").splitlines():
        s=raw.strip()
        if not s or s.startswith("#"): continue
        z=s.split()
        if len(z)<2: continue
        try:u,v=int(z[0]),int(z[1])
        except:continue
        if u==v:continue
        if u>v:u,v=v,u
        E.add((u,v))
    return E

snaps=[]
with tarfile.open(a.archive,"r:*") as tf:
    members=[m for m in tf.getmembers() if m.isfile() and re.search(r'\.(txt|edges)(\.gz)?$',m.name)]
    for m in sorted(members,key=lambda x:x.name):
        b=tf.extractfile(m).read()
        if m.name.endswith(".gz"): b=gzip.decompress(b)
        snaps.append((m.name,parse_edges(b)))
if len(snaps)!=122: raise SystemExit(f"GATE FAIL snapshots={len(snaps)} expected=122")
ops=[]
prev=set()
initial=len(snaps[0][1])
for idx,(name,E) in enumerate(snaps):
    if idx==0:
        for e in sorted(E): ops.append(("add",*e))
    else:
        for e in sorted(prev-E): ops.append(("remove",*e))
        for e in sorted(E-prev): ops.append(("add",*e))
    prev=E
ins=sum(op=="add" for op,_,_ in ops); dele=len(ops)-ins
# Frozen benchmark counts include the initial snapshot as initial state, not dynamic updates.
derived=len(ops)-initial; derived_ins=ins-initial
print("snapshots",len(snaps),"initial_edges",initial,"derived_updates",derived,
      "derived_insertions",derived_ins,"derived_deletions",dele)
expected=(32955,542194,281050,261144)
got=(initial,derived,derived_ins,dele)
if got!=expected:
    raise SystemExit(f"GATE FAIL got={got} expected={expected}")
os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
with open(a.out,"w",newline="") as f:
    w=csv.writer(f);w.writerow(["op","u","v"]);w.writerows(ops)
print("GATE PASS; wrote",len(ops),"operations including initial snapshot")

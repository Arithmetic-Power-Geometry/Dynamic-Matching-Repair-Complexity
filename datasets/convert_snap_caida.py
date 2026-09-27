#!/usr/bin/env python3
"""Convert chronological SNAP AS-CAIDA snapshots into dynamic undirected edge updates."""
import argparse,glob,os
p=argparse.ArgumentParser();p.add_argument("directory");p.add_argument("output");a=p.parse_args()
files=sorted(glob.glob(os.path.join(a.directory,"as-caida*.txt")))
def read_edges(path):
 s=set()
 with open(path) as f:
  for line in f:
   if not line.strip() or line.startswith("#"):continue
   x=line.split();u=int(x[0]);v=int(x[1])
   if u!=v:s.add((min(u,v),max(u,v)))
 return s
prev=None;adds=dels=0
with open(a.output,"w") as out:
 for path in files:
  cur=read_edges(path)
  if prev is None:
   for u,v in sorted(cur):out.write(f"1 {u} {v}\n");adds+=1
  else:
   for u,v in sorted(prev-cur):out.write(f"0 {u} {v}\n");dels+=1
   for u,v in sorted(cur-prev):out.write(f"1 {u} {v}\n");adds+=1
  prev=cur
print("snapshots",len(files),"insertions_including_initial",adds,"deletions",dels)

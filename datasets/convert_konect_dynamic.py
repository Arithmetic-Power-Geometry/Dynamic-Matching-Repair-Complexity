#!/usr/bin/env python3
"""Convert KONECT directed +/- temporal records to an undirected fully-dynamic stream.
A projected edge is active while either directed arc is active.
"""
import argparse
from collections import defaultdict
p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("output");a=p.parse_args()
arcs=set();count=defaultdict(int);stats=dict(raw=0,loops=0,adds=0,dels=0,duplicate_adds=0,orphan_removals=0)
with open(a.input) as f,open(a.output,"w") as g:
 for line in f:
  if not line.strip() or line.startswith("%"):continue
  x=line.split();u=int(x[0])-1;v=int(x[1])-1;w=x[2];stats["raw"]+=1
  if u==v:stats["loops"]+=1;continue
  arc=(u,v);e=(min(u,v),max(u,v))
  if w=="+1":
   if arc in arcs:stats["duplicate_adds"]+=1;continue
   arcs.add(arc);before=count[e];count[e]+=1
   if before==0:g.write(f"1 {e[0]} {e[1]}\n");stats["adds"]+=1
  elif w=="-1":
   if arc not in arcs:stats["orphan_removals"]+=1;continue
   arcs.remove(arc);count[e]-=1
   if count[e]==0:g.write(f"0 {e[0]} {e[1]}\n");stats["dels"]+=1;del count[e]
print(stats);print("projected_updates",stats["adds"]+stats["dels"]);print("final_active_edges",len(count))

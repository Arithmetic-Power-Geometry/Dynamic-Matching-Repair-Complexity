"""Read DynGraphLab/DynMatch fully-dynamic .seq files."""
from dataclasses import dataclass
@dataclass
class DynEvent:
    op:str; u:int; v:int

def read_dynmatch_seq(path,limit=0):
    import gzip,bz2
    if path.endswith(".gz"): f=gzip.open(path,"rt")
    elif path.endswith(".bz2"): f=bz2.open(path,"rt")
    else: f=open(path,"rt")
    n=None;declared=None;events=[]
    with f:
        for line in f:
            s=line.strip()
            if not s: continue
            if s.startswith("#"):
                p=s[1:].split()
                if len(p)>=2 and p[0].isdigit():
                    n=int(p[0]);declared=int(p[1])
                continue
            p=s.split()
            if len(p)<3: continue
            flag,u,v=p[0],int(p[1]),int(p[2])
            if u==v: continue
            events.append(DynEvent("add" if flag=="1" else "del",u,v))
            if limit and len(events)>=limit: break
    if n is None:
        n=1+max(max(e.u,e.v) for e in events)
    return n,declared,events

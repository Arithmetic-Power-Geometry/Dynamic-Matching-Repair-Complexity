"""Temporal edge-stream adapter for external datasets.
Accepted rows: u v [timestamp] [operation].
operation may be add/insert/1 or del/delete/remove/0.
If operation is absent, rows are treated as timestamped interactions.
"""
from dataclasses import dataclass
@dataclass
class Event:
    op:str; u:int; v:int; t:float=0.0

def read_temporal(path, delimiter=None, comment=("#","%")):
    raw=[]; ids={}
    def vid(x):
        if x not in ids: ids[x]=len(ids)
        return ids[x]
    with open(path,encoding="utf-8") as f:
        for line in f:
            s=line.strip()
            if not s or s.startswith(comment): continue
            p=s.split(delimiter)
            if len(p)<2: continue
            u,v=vid(p[0]),vid(p[1])
            if u==v: continue
            t=float(p[2]) if len(p)>2 and _num(p[2]) else float(len(raw))
            op=_op(p[3]) if len(p)>3 else "interaction"
            raw.append(Event(op,u,v,t))
    raw.sort(key=lambda e:e.t)
    return len(ids),raw

def _num(x):
    try: float(x); return True
    except: return False
def _op(x):
    x=x.lower()
    if x in {"1","add","insert","+","+1"}: return "add"
    if x in {"0","del","delete","remove","-","-1"}: return "del"
    return "interaction"

def native_events(events):
    active=set();out=[]
    for e in events:
        k=(min(e.u,e.v),max(e.u,e.v))
        if e.op=="add" and k not in active: active.add(k);out.append(e)
        elif e.op=="del" and k in active: active.remove(k);out.append(e)
    return out

def window_events(events,window):
    """Derive edge lifetimes from interactions. Expiration is synthetic and must be labelled derived."""
    active={};out=[]
    for e in events:
        now=e.t
        expired=[k for k,last in active.items() if now-last>window]
        for k in expired:
            out.append(Event("del",k[0],k[1],last+window));del active[k]
        k=(min(e.u,e.v),max(e.u,e.v))
        if k not in active: out.append(Event("add",k[0],k[1],now))
        active[k]=now
    for k,last in active.items(): out.append(Event("del",k[0],k[1],last+window))
    return sorted(out,key=lambda e:e.t)

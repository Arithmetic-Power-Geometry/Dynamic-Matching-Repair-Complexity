"""Differential audit: snapshot vs versioned shadow tracker."""
import os,sys,random
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import DynamicGraph
from shadow_epoch import ShadowEpochMatcher
from versioned_shadow_epoch import VersionedShadowEpochMatcher

FIELDS=["step","vertex","degree","discovery","found","r_changed_common",
        "neighbors_added","neighbors_removed","changed_plus_churn"]

def run(cls,n,ops):
    G=DynamicGraph(n); M=cls(G)
    for op,u,v in ops: M.update(op,u,v)
    return [{k:r[k] for k in FIELDS} for r in M.epoch_trace],M

def stream(n,steps,seed):
    R=random.Random(seed); E=set(); out=[]
    for _ in range(steps):
        u=R.randrange(n);v=R.randrange(n-1)
        if v>=u:v+=1
        e=(min(u,v),max(u,v))
        if e in E and R.random()<.7:
            E.remove(e);out.append(("remove",*e))
        else:
            if e not in E:E.add(e);out.append(("add",*e))
            else:out.append(("remove",*e));E.remove(e)
    return out

cases=0
for n in range(3,13):
    for seed in range(40):
        ops=stream(n,250,1000*n+seed)
        a,ma=run(ShadowEpochMatcher,n,ops)
        b,mb=run(VersionedShadowEpochMatcher,n,ops)
        assert a==b,(n,seed,next((i for i,(x,y) in enumerate(zip(a,b)) if x!=y),None))
        assert ma.is_maximal() and mb.is_maximal()
        cases+=1
print("DIFFERENTIAL PASS",cases,"streams")

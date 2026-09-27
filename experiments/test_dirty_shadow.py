"""Differential audit of event-driven DirtyShadowEpochMatcher."""
import os,sys,random
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import DynamicGraph
from shadow_epoch import ShadowEpochMatcher
from dirty_shadow_epoch import DirtyShadowEpochMatcher
FIELDS=["step","vertex","degree","discovery","found","r_changed_common","neighbors_added","neighbors_removed","changed_plus_churn"]
def run(C,n,ops):
 G=DynamicGraph(n);m=C(G)
 for z in ops:m.update(*z)
 return [{k:r[k] for k in FIELDS} for r in m.epoch_trace],m
def gen(n,steps,seed):
 R=random.Random(seed);E=set();o=[]
 for _ in range(steps):
  u=R.randrange(n);v=R.randrange(n-1);v+=v>=u;e=(min(u,v),max(u,v))
  if e in E:E.remove(e);o.append(("remove",*e))
  else:E.add(e);o.append(("add",*e))
 return o
cases=0
for n in range(3,16):
 for seed in range(50):
  ops=gen(n,300,n*10000+seed);a,ma=run(ShadowEpochMatcher,n,ops);b,mb=run(DirtyShadowEpochMatcher,n,ops)
  assert a==b,(n,seed,next((i for i,(x,y) in enumerate(zip(a,b)) if x!=y),None))
  assert ma.is_maximal() and mb.is_maximal();cases+=1
print("DIRTY DIFFERENTIAL PASS",cases)

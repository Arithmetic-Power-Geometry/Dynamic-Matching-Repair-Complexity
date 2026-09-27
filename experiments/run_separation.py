import os,sys,csv
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *
from generators import star_of_pairs

rows=[]
for k in [8,16,32,64,128,256,512,1024]:
    for cls,name in [(ScanRepairMatcher,"scan"),(EagerCounterMatcher,"eager"),(HeavyLightMatcher,"heavy_light")]:
        G,e=star_of_pairs(k)
        a=cls(G)
        # Force intended initial matching.
        a.mate=[-1]*G.n
        a._match(0,1)
        for i in range(k):
            x=2+2*i;a._match(x,x+1)
        p0=a.metrics.probes;g0=a.metrics.propagation;r0=a.metrics.recourse
        a.update("del",*e)
        rows.append(dict(k=k,n=G.n,algorithm=name,
            probes=a.metrics.probes-p0,
            propagation=a.metrics.propagation-g0,
            work=(a.metrics.probes-p0)+(a.metrics.propagation-g0),
            recourse=a.metrics.recourse-r0,
            maximal=int(a.is_maximal())))
os.makedirs("results",exist_ok=True)
with open("results/separation.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("wrote results/separation.csv",len(rows))

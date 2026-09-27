import os,sys,random,csv
sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from dmrc import *

# Application-style bipartite compatibility graph: requests 0..R-1, resources R..R+S-1.
R,S=120,120
G=DynamicGraph(R+S)
rng=random.Random(17)
for r in range(R):
    choices=rng.sample(range(R,R+S),12)
    for s in choices:G.add_edge(r,s)

algs=[("scan",ScanRepairMatcher(G)),]
a=algs[0][1];a.initialize_greedy()
before=a.matching_size()
# simulate resource-link failures and new compatibility links
for _ in range(250):
    r=rng.randrange(R);s=rng.randrange(R,R+S)
    op="del" if a.G.has_edge(r,s) else "add"
    a.update(op,r,s)
after=a.matching_size()
os.makedirs("results",exist_ok=True)
with open("results/application_demo.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["scenario","matching_before","matching_after","probes","recourse","maximal"])
    w.writeheader();w.writerow(dict(scenario="dynamic_resource_allocation",matching_before=before,
       matching_after=after,probes=a.metrics.probes,recourse=a.metrics.recourse,maximal=int(a.is_maximal())))
print("wrote results/application_demo.csv")

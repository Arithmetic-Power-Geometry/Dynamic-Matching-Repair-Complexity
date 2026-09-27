"""Compact summary of ShadowEpochMatcher output."""
import csv,argparse,statistics
p=argparse.ArgumentParser();p.add_argument("events");p.add_argument("--dataset",required=True);p.add_argument("--out",required=True);a=p.parse_args()
R=list(csv.DictReader(open(a.events)))
def I(x,k):return int(x[k])
def F(x,k):return float(x[k])
def quant(v,p):
    if not v:return 0
    v=sorted(v);return v[min(len(v)-1,int((len(v)-1)*p))]
D=[I(x,"discovery") for x in R]; deg=[I(x,"degree") for x in R]
rs=[I(x,"r_changed_common") for x in R]; churn=[I(x,"neighbors_added")+I(x,"neighbors_removed") for x in R]
inten=[F(x,"scan_intensity") for x in R]
out=dict(dataset=a.dataset,repair_events=len(R),total_discovery=sum(D),
 mean_D=sum(D)/len(D) if D else 0,p95_D=quant(D,.95),p99_D=quant(D,.99),max_D=max(D,default=0),
 mean_scan_intensity=sum(inten)/len(inten) if inten else 0,p95_scan_intensity=quant(inten,.95),
 full_scan_fraction=sum(d>0 and w>=d for d,w in zip(deg,D))/len(R) if R else 0,
 events_status_change=sum(x>0 for x in rs),mean_status_changes=sum(rs)/len(R) if R else 0,
 events_adjacency_churn=sum(x>0 for x in churn),mean_adjacency_churn=sum(churn)/len(R) if R else 0,
 status_change_total=sum(rs),adjacency_churn_total=sum(churn))
with open(a.out,"w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=out.keys());w.writeheader();w.writerow(out)
print(out)

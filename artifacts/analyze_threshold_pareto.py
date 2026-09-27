import os,pandas as pd
src="results/structural_regimes.csv"
if not os.path.exists(src):raise SystemExit("Run structural experiment first")
d=pd.read_csv(src);rows=[]
for (family,n),g in d.groupby(["family","n"]):
 bt=g.loc[g.total_work.idxmin()]; bx=g.loc[g.max_work.idxmin()]; pareto=[]
 for _,r in g.iterrows():
  dom=((g.total_work<=r.total_work)&(g.max_work<=r.max_work)&((g.total_work<r.total_work)|(g.max_work<r.max_work))).any()
  if not dom:pareto.append(int(r.T))
 rows.append(dict(family=family,n=n,T_total=int(bt.T),min_total=int(bt.total_work),T_tail=int(bx.T),min_max_work=int(bx.max_work),pareto_T=";".join(map(str,sorted(pareto)))))
out=pd.DataFrame(rows);os.makedirs("artifacts/output",exist_ok=True);out.to_csv("artifacts/output/table_threshold_pareto.csv",index=False);print(out.to_string(index=False))

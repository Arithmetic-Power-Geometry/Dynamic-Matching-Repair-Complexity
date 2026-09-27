import os,pandas as pd
parts=[]
for path,label in [("results/benchmark.csv","dmrc"),("results/application_demo.csv","application"),("results/dynmatch_external.csv","external")]:
 if os.path.exists(path):
  d=pd.read_csv(path);d["source"]=label;parts.append(d)
if not parts: raise SystemExit("No result files found.")
out=pd.concat(parts,ignore_index=True,sort=False)
os.makedirs("artifacts/output",exist_ok=True)
out.to_csv("artifacts/output/all_algorithm_results.csv",index=False)
cols=[c for c in ["source","family","scenario","algorithm","n","vertices","updates","operations","time_s","work","total_work","median_work_update","p95_work_update","max_work_update","recourse","maximal","matching_size"] if c in out]
out[cols].to_csv("artifacts/output/table_algorithm_comparison.csv",index=False)
print(out[cols].to_string(index=False))

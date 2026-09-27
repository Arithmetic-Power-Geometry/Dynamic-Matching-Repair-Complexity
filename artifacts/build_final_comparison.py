import os,pandas as pd
os.makedirs("artifacts/output",exist_ok=True)
rows=[
{"category":"published theory","method":"Neiman-Solomon","guarantee":"deterministic O(sqrt(m)) worst-case update","measured_here":"no"},
{"category":"published theory","method":"Chuzhoy-Khanna-Song 2026","guarantee":"deterministic n^(1/2+o(1)) amortized update","measured_here":"no"}]
for path,label in [("results/benchmark.csv","internal benchmark"),("results/application_demo.csv","resource allocation"),("results/communication_application.csv","communication pairing")]:
 if os.path.exists(path):
  d=pd.read_csv(path)
  for _,r in d.iterrows():
   rows.append({"category":label,"method":r.get("algorithm",""),"guarantee":"prototype measurement","measured_here":"yes","tail_work":r.get("max_work_update",r.get("max_work","")),"total_work":r.get("work",r.get("total_work",""))})
ext="results/dynmatch_external.csv"
if os.path.exists(ext):
 d=pd.read_csv(ext)
 for _,r in d.iterrows():rows.append({"category":"external DynMatch","method":r.algorithm,"guarantee":"native implementation measurement","measured_here":"yes"})
else:
 for m in ["dynmatch_neiman_solomon","dynmatch_baswana_gupta_sen","dynmatch_random_walk"]:rows.append({"category":"external DynMatch","method":m,"guarantee":"pending common-stream run","measured_here":"NO - NOT RUN"})
out=pd.DataFrame(rows);out.to_csv("artifacts/output/table_existing_vs_proposed.csv",index=False);print(out.to_string(index=False))

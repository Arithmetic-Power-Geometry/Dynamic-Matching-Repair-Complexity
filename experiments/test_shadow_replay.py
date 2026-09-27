import csv,os,subprocess,sys,tempfile
root=os.path.dirname(os.path.dirname(__file__))
fixture=os.path.join(root,"experiments","fixtures","shadow_small.csv")
with tempfile.TemporaryDirectory() as d:
 out=os.path.join(d,"events.csv")
 p=subprocess.run([sys.executable,os.path.join(root,"artifacts","replay_shadow_epoch.py"),fixture,"--out",out],
                  capture_output=True,text=True,check=True)
 rows=list(csv.DictReader(open(out)))
 assert "maximal 1" in p.stdout
 assert len(rows)>0
 for r in rows:
  dgr=int(r["degree"]); disc=int(r["discovery"])
  assert 0<=disc<=dgr
  assert int(r["changed_plus_churn"])>=int(r["r_changed_common"])
 print(p.stdout.strip())
 print("shadow_fixture_events",len(rows))

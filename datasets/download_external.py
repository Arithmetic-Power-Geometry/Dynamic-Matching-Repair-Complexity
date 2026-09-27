#!/usr/bin/env python3
import argparse,hashlib,os,urllib.request
DATASETS={
 "college_msg":{"url":"https://snap.stanford.edu/data/CollegeMsg.txt.gz","source":"SNAP","mode":"window","format":"SRC DST UNIXTS"},
 "email_eu_core":{"url":"https://snap.stanford.edu/data/email-Eu-core-temporal.txt.gz","source":"SNAP","mode":"window","format":"SRC DST UNIXTS"}
}
p=argparse.ArgumentParser();p.add_argument("name",choices=DATASETS);a=p.parse_args();d=DATASETS[a.name]
os.makedirs("datasets/external",exist_ok=True);path="datasets/external/"+d["url"].rsplit("/",1)[-1]
urllib.request.urlretrieve(d["url"],path)
h=hashlib.sha256(open(path,"rb").read()).hexdigest()
print("dataset",a.name);print("path",path);print("source",d["source"]);print("recommended_mode",d["mode"]);print("sha256",h)

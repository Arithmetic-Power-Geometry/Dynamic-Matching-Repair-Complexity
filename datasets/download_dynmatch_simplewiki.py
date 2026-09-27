#!/usr/bin/env python3
import hashlib,os,tarfile,urllib.request
URL="https://aeghpc101.ifi.uni-heidelberg.de/~cschulz/dyngraphlabrepo/link-dynamic-simplewiki.tar.bz2"
os.makedirs("datasets/external",exist_ok=True);arc="datasets/external/link-dynamic-simplewiki.tar.bz2"
urllib.request.urlretrieve(URL,arc)
h=hashlib.sha256(open(arc,"rb").read()).hexdigest()
print("source=DynGraphLab Dynamic Graph Repository");print("dataset=Dynamic Simple Wiki");print("sha256="+h)
with tarfile.open(arc,"r:bz2") as t:
 safe=[m for m in t.getmembers() if m.isfile() and ".." not in m.name and not m.name.startswith("/")]
 for m in safe:t.extract(m,"datasets/external",filter="data")
print("extracted",len(safe),"files")

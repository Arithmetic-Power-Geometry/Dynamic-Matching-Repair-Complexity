"""Cross-domain prediction of optimistic future indexability.
Dependency-light logistic regression implemented with numpy.
Reports ROC-AUC and average precision; no per-target tuning.
"""
import argparse,csv,numpy as np
p=argparse.ArgumentParser();p.add_argument("train");p.add_argument("test");a=p.parse_args()
ALL=["degree","repair_count_before","cumulative_scan_before","previous_scan_work","inter_repair_gap","degree_change"]
models={"degree_only":["degree"],"repair_count_only":["repair_count_before"],"history":ALL}
def load(path,cols):
 X=[];y=[]
 with open(path) as f:
  for r in csv.DictReader(f):
   X.append([np.log1p(max(0,float(r[c]))) if c!="degree_change" else np.sign(float(r[c]))*np.log1p(abs(float(r[c]))) for c in cols])
   y.append(int(r["label_oracle_indexable"]))
 return np.asarray(X,float),np.asarray(y,float)
def auc(y,s):
 pos=s[y==1];neg=s[y==0]
 if len(pos)==0 or len(neg)==0:return float("nan")
 order=np.argsort(s);r=np.empty(len(s));r[order]=np.arange(len(s))+1
 return (r[y==1].sum()-len(pos)*(len(pos)+1)/2)/(len(pos)*len(neg))
def ap(y,s):
 o=np.argsort(-s);yy=y[o];tp=np.cumsum(yy);k=np.arange(1,len(y)+1)
 return float(((tp/k)*yy).sum()/max(1,yy.sum()))
def fit(X,y):
 mu=X.mean(0);sd=X.std(0)+1e-9;X=(X-mu)/sd;X=np.c_[np.ones(len(X)),X];w=np.zeros(X.shape[1])
 # class-balanced logistic loss so rare positives are not ignored
 wp=len(y)/(2*max(1,y.sum()));wn=len(y)/(2*max(1,(1-y).sum()))
 weights=np.where(y==1,wp,wn)
 for _ in range(400):
  z=np.clip(X@w,-30,30);pr=1/(1+np.exp(-z));g=X.T@((pr-y)*weights)/len(y);w-=0.1*g
 return w,mu,sd
for name,cols in models.items():
 X,y=load(a.train,cols);Xt,yt=load(a.test,cols);w,mu,sd=fit(X,y)
 score=1/(1+np.exp(-np.clip(np.c_[np.ones(len(Xt)),(Xt-mu)/sd]@w,-30,30)))
 print(name,"test_n",len(yt),"prevalence",yt.mean(),"auc",auc(yt,score),"ap",ap(yt,score))

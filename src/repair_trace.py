"""Event-level repair-reuse instrumentation.
Wraps ScanRepairMatcher without changing its matching decisions.
"""
from dmrc import ScanRepairMatcher

class RepairTraceMatcher(ScanRepairMatcher):
    def __init__(self,G):
        super().__init__(G)
        self.step=0
        self.trace=[]
        self.last_repair=[None]*G.n
        self.repair_count=[0]*G.n
    def find_free_neighbor(self,u):
        before=self.metrics.probes
        degree=len(self.G.adj[u])
        ans=super().find_free_neighbor(u)
        work=self.metrics.probes-before
        last=self.last_repair[u]
        gap=None if last is None else self.step-last
        self.repair_count[u]+=1
        self.trace.append(dict(step=self.step,vertex=u,degree=degree,
            scan_work=work,found=int(ans>=0),repair_number=self.repair_count[u],
            inter_repair_gap=gap if gap is not None else -1))
        self.last_repair[u]=self.step
        return ans
    def update(self,op,u,v):
        self.step+=1
        return super().update(op,u,v)

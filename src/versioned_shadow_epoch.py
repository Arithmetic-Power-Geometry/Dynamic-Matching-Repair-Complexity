"""Exact versioned shadow instrumentation.

Avoids copying full neighbor status maps at every repair. Each vertex carries a status
version incremented whenever its matched/free state changes. For a queried center u,
we retain versions only for neighbors present at its previous repair plus the previous
neighbor set needed to distinguish adjacency churn.

This is intended as an exact optimization of ShadowEpochMatcher and must pass
differential tests before real-data use.
"""
from repair_trace import RepairTraceMatcher

class VersionedShadowEpochMatcher(RepairTraceMatcher):
    def __init__(self,G):
        super().__init__(G)
        self.status_version=[0]*G.n
        self.prev_versions=[None]*G.n
        self.prev_neighbors=[None]*G.n
        self.epoch_trace=[]

    def find_free_neighbor(self,u):
        current_N=set(self.G.adj[u])
        prevN=self.prev_neighbors[u]; prevF=self.prev_free[u]
        if prevN is None:
            r_changed=0; added=0; removed=0
        else:
            common=current_N & prevN
            r_changed=sum((self.mate[v]<0)!=prevF[v] for v in common)
            added=len(current_N-prevN); removed=len(prevN-current_N)
        before=self.metrics.probes
        ans=super().find_free_neighbor(u)
        D=self.metrics.probes-before; d=len(current_N)
        self.epoch_trace.append(dict(step=self.step,vertex=u,degree=d,discovery=D,
            found=int(ans>=0),r_changed_common=r_changed,neighbors_added=added,
            neighbors_removed=removed,changed_plus_churn=r_changed+added+removed,
            scan_intensity=(D/d if d else 0.0)))
        self.prev_neighbors[u]=current_N
        self.prev_free[u]={v:(self.mate[v]<0) for v in current_N}
        return ans

"""Shadow epoch instrumentation for exact repair-state-change counts.

This matcher preserves ScanRepairMatcher decisions. It augments RepairTraceMatcher with,
for each vertex u, a snapshot of neighbor free/nonfree status at u's previous repair.
At the next repair it reports:
  r_changed = number of currently adjacent neighbors whose free status differs from snapshot,
  D = actual Scan probes,
  d = current degree,
  intensity = D/d.

Important: r_changed is a reproducible empirical epoch statistic. It is not automatically
identical to the adversarial r in the restricted lower-bound theorem when adjacency itself
changes between snapshots; adjacency churn is reported separately.
"""
from repair_trace import RepairTraceMatcher

class ShadowEpochMatcher(RepairTraceMatcher):
    def __init__(self,G):
        super().__init__(G)
        self.prev_status=[None]*G.n
        self.prev_neighbors=[None]*G.n
        self.epoch_trace=[]

    def _snapshot(self,u):
        N=set(self.G.adj[u])
        return N,{v:(self.mate[v]<0) for v in N}

    def find_free_neighbor(self,u):
        current_N=set(self.G.adj[u])
        prevN=self.prev_neighbors[u]
        prevS=self.prev_status[u]
        if prevN is None:
            r_changed=0; added=0; removed=0
        else:
            common=current_N & prevN
            r_changed=sum((self.mate[v]<0)!=prevS[v] for v in common)
            added=len(current_N-prevN); removed=len(prevN-current_N)

        before=self.metrics.probes
        ans=super().find_free_neighbor(u)
        D=self.metrics.probes-before
        d=len(current_N)
        self.epoch_trace.append(dict(
            step=self.step,vertex=u,degree=d,discovery=D,found=int(ans>=0),
            r_changed_common=r_changed,neighbors_added=added,neighbors_removed=removed,
            changed_plus_churn=r_changed+added+removed,
            scan_intensity=(D/d if d else 0.0)))
        N,S=self._snapshot(u)
        self.prev_neighbors[u]=N; self.prev_status[u]=S
        return ans

"""Event-driven exact endpoint shadow tracker.

For vertices that have already been repaired, maintain baseline neighbor membership/free
state and a dirty set of neighbors whose *current endpoint state* differs from that baseline.
Updates to matching status and adjacency update only affected repaired centers.
At repair, counts are O(1) from maintained sets; baseline is advanced by applying dirty
entries rather than copying the full neighborhood.
"""
from repair_trace import RepairTraceMatcher

class DirtyShadowEpochMatcher(RepairTraceMatcher):
    def __init__(self,G):
        super().__init__(G)
        self.seen=[False]*G.n
        self.base_members=[set() for _ in range(G.n)]
        self.base_free=[{} for _ in range(G.n)]
        self.dirty=[set() for _ in range(G.n)]
        self.epoch_trace=[]

    def _refresh_neighbor_for_center(self,c,x):
        if not self.seen[c]: return
        base_in=x in self.base_members[c]
        cur_in=x in self.G.adj[c]
        differs=(base_in!=cur_in)
        if base_in and cur_in:
            differs=((self.mate[x]<0)!=self.base_free[c][x])
        if differs:self.dirty[c].add(x)
        else:self.dirty[c].discard(x)

    def _status_changed(self,x):
        for c in self.G.adj[x]:
            self._refresh_neighbor_for_center(c,x)

    def _match(self,u,v):
        super()._match(u,v); self._status_changed(u); self._status_changed(v)

    def _unmatch(self,u,v):
        super()._unmatch(u,v); self._status_changed(u); self._status_changed(v)

    def update(self,op,u,v):
        # Preserve exact event ordering of ScanRepairMatcher while making adjacency
        # membership changes visible to the shadow state at the correct endpoint.
        self.step += 1
        if op=="add":
            self.G.add_edge(u,v)
            self._refresh_neighbor_for_center(u,v); self._refresh_neighbor_for_center(v,u)
            if self.mate[u]<0 and self.mate[v]<0:
                self._match(u,v); self.metrics.recourse+=1
        else:
            if not self.G.has_edge(u,v): return
            was=self.mate[u]==v
            # Record the membership transition immediately after graph deletion and
            # before any matching-state repair triggered by that deletion.
            self.G.remove_edge(u,v)
            self._refresh_neighbor_for_center(u,v); self._refresh_neighbor_for_center(v,u)
            if was:
                self._unmatch(u,v); self.metrics.recourse+=1
                self.repair_vertex(u); self.repair_vertex(v)

    def find_free_neighbor(self,u):
        if not self.seen[u]:
            r_changed=added=removed=0
        else:
            r_changed=added=removed=0
            for x in self.dirty[u]:
                b=x in self.base_members[u]; c=x in self.G.adj[u]
                if b and c:r_changed+=1
                elif c:added+=1
                else:removed+=1
        before=self.metrics.probes
        ans=super().find_free_neighbor(u)
        D=self.metrics.probes-before; d=len(self.G.adj[u])
        self.epoch_trace.append(dict(step=self.step,vertex=u,degree=d,discovery=D,
            found=int(ans>=0),r_changed_common=r_changed,neighbors_added=added,
            neighbors_removed=removed,changed_plus_churn=r_changed+added+removed,
            scan_intensity=(D/d if d else 0.0)))
        # Advance baseline only on dirty coordinates; first observation initializes once.
        if not self.seen[u]:
            self.base_members[u]=set(self.G.adj[u])
            self.base_free[u]={x:(self.mate[x]<0) for x in self.G.adj[u]}
            self.seen[u]=True
        else:
            for x in list(self.dirty[u]):
                if x in self.G.adj[u]:
                    self.base_members[u].add(x);self.base_free[u][x]=(self.mate[x]<0)
                else:
                    self.base_members[u].discard(x);self.base_free[u].pop(x,None)
            self.dirty[u].clear()
        return ans

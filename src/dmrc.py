from dataclasses import dataclass
import math, random

@dataclass
class Metrics:
    probes:int=0
    propagation:int=0
    recourse:int=0

class DynamicGraph:
    def __init__(self,n):
        self.n=n
        self.adj=[set() for _ in range(n)]
    def add_edge(self,u,v):
        if u==v: return
        self.adj[u].add(v); self.adj[v].add(u)
    def remove_edge(self,u,v):
        self.adj[u].discard(v); self.adj[v].discard(u)
    def has_edge(self,u,v):
        return v in self.adj[u]
    def edges(self):
        for u in range(self.n):
            for v in self.adj[u]:
                if u<v: yield (u,v)

class BaseMatcher:
    def __init__(self,G):
        self.G=G; self.mate=[-1]*G.n; self.metrics=Metrics()
    def _match(self,u,v):
        self.mate[u]=v; self.mate[v]=u
    def _unmatch(self,u,v):
        self.mate[u]=self.mate[v]=-1
    def initialize_greedy(self):
        for u,v in self.G.edges():
            if self.mate[u]<0 and self.mate[v]<0: self._match(u,v)
    def matching_size(self):
        return sum(1 for u,v in enumerate(self.mate) if v>u)
    def is_maximal(self):
        for u,v in self.G.edges():
            if self.mate[u]<0 and self.mate[v]<0: return False
        return True

class RecomputeMatcher(BaseMatcher):
    def update(self,op,u,v):
        old={(min(i,j),max(i,j)) for i,j in enumerate(self.mate) if j>i}
        if op=="add": self.G.add_edge(u,v)
        else: self.G.remove_edge(u,v)
        self.mate=[-1]*self.G.n
        # full adjacency scan proxy
        self.metrics.probes += sum(len(a) for a in self.G.adj)
        self.initialize_greedy()
        new={(min(i,j),max(i,j)) for i,j in enumerate(self.mate) if j>i}
        self.metrics.recourse += len(old^new)

class ScanRepairMatcher(BaseMatcher):
    def find_free_neighbor(self,u):
        for v in self.G.adj[u]:
            self.metrics.probes += 1
            if self.mate[v]<0: return v
        return -1
    def repair_vertex(self,u):
        if self.mate[u]>=0: return
        v=self.find_free_neighbor(u)
        if v>=0:
            self._match(u,v); self.metrics.recourse+=1
    def update(self,op,u,v):
        if op=="add":
            self.G.add_edge(u,v)
            if self.mate[u]<0 and self.mate[v]<0:
                self._match(u,v); self.metrics.recourse+=1
        else:
            was=self.mate[u]==v
            self.G.remove_edge(u,v)
            if was:
                self._unmatch(u,v); self.metrics.recourse+=1
                self.repair_vertex(u); self.repair_vertex(v)

class EagerCounterMatcher(ScanRepairMatcher):
    def __init__(self,G):
        super().__init__(G)
        self.free=[True]*G.n
        self.free_neighbors=[set(G.adj[u]) for u in range(G.n)]
    def _set_free(self,x,state):
        if self.free[x]==state: return
        self.free[x]=state
        for y in self.G.adj[x]:
            self.metrics.propagation += 1
            if state: self.free_neighbors[y].add(x)
            else: self.free_neighbors[y].discard(x)
    def _match(self,u,v):
        self._set_free(u,False); self._set_free(v,False)
        self.mate[u]=v; self.mate[v]=u
    def _unmatch(self,u,v):
        self.mate[u]=self.mate[v]=-1
        self._set_free(u,True); self._set_free(v,True)
    def find_free_neighbor(self,u):
        self.metrics.probes += 1
        return next(iter(self.free_neighbors[u]),-1)
    def update(self,op,u,v):
        if op=="add":
            self.G.add_edge(u,v)
            if self.free[v]: self.free_neighbors[u].add(v)
            if self.free[u]: self.free_neighbors[v].add(u)
            if self.mate[u]<0 and self.mate[v]<0:
                self._match(u,v); self.metrics.recourse+=1
        else:
            was=self.mate[u]==v
            self.G.remove_edge(u,v)
            self.free_neighbors[u].discard(v); self.free_neighbors[v].discard(u)
            if was:
                self._unmatch(u,v); self.metrics.recourse+=1
                self.repair_vertex(u); self.repair_vertex(v)

class HeavyLightMatcher(ScanRepairMatcher):
    def __init__(self,G,threshold=None):
        super().__init__(G)
        self.T=threshold or max(2,int(math.sqrt(max(1,G.n))))
        self.heavy=[len(G.adj[u])>self.T for u in range(G.n)]
        self.free=[True]*G.n
        self.hfree={u:set(G.adj[u]) for u in range(G.n) if self.heavy[u]}
    def _set_free(self,x,state):
        if self.free[x]==state: return
        self.free[x]=state
        # propagate only to heavy neighbors
        for y in self.G.adj[x]:
            if self.heavy[y]:
                self.metrics.propagation += 1
                if state:self.hfree[y].add(x)
                else:self.hfree[y].discard(x)
    def _match(self,u,v):
        self._set_free(u,False); self._set_free(v,False)
        self.mate[u]=v; self.mate[v]=u
    def _unmatch(self,u,v):
        self.mate[u]=self.mate[v]=-1
        self._set_free(u,True); self._set_free(v,True)
    def find_free_neighbor(self,u):
        if self.heavy[u]:
            self.metrics.probes += 1
            return next(iter(self.hfree[u]),-1)
        for v in self.G.adj[u]:
            self.metrics.probes += 1
            if self.mate[v]<0:return v
        return -1
    def _reclassify(self,x):
        new_heavy=len(self.G.adj[x])>self.T
        if new_heavy==self.heavy[x]: return
        # Building or discarding an exact heavy summary is real maintenance work.
        self.metrics.propagation += len(self.G.adj[x])
        self.heavy[x]=new_heavy
        if new_heavy:
            self.hfree[x]={y for y in self.G.adj[x] if self.free[y]}
        else:
            self.hfree.pop(x,None)
    def update(self,op,u,v):
        if op=="add":
            existed=self.G.has_edge(u,v)
            self.G.add_edge(u,v)
            if not existed:
                self._reclassify(u); self._reclassify(v)
                if self.heavy[u] and self.free[v]: self.hfree[u].add(v)
                if self.heavy[v] and self.free[u]: self.hfree[v].add(u)
            if self.mate[u]<0 and self.mate[v]<0:
                self._match(u,v); self.metrics.recourse+=1
        else:
            if not self.G.has_edge(u,v): return
            was=self.mate[u]==v
            if self.heavy[u]: self.hfree[u].discard(v)
            if self.heavy[v]: self.hfree[v].discard(u)
            self.G.remove_edge(u,v)
            self._reclassify(u); self._reclassify(v)
            if was:
                self._unmatch(u,v); self.metrics.recourse+=1
                self.repair_vertex(u); self.repair_vertex(v)
    def validate_invariants(self):
        for u,v in enumerate(self.mate):
            if v>=0:
                if v>=self.G.n or self.mate[v]!=u or not self.G.has_edge(u,v): return False
        for u in range(self.G.n):
            if self.heavy[u] != (len(self.G.adj[u])>self.T): return False
            if self.heavy[u]:
                expected={v for v in self.G.adj[u] if self.mate[v]<0}
                if self.hfree.get(u,set()) != expected: return False
        return self.is_maximal()



class AdaptiveDebtMatcher(ScanRepairMatcher):
    """Scan by default; activate an exact free-neighbor index only after observed
    scan debt pays its construction cost. All index construction/maintenance
    work is charged to propagation. No future information is used."""
    def __init__(self,G,build_factor=1.0,retire_factor=2.0):
        super().__init__(G)
        self.free=[True]*G.n
        self.indexed=[False]*G.n
        self.ifree={}
        self.debt=[0]*G.n
        self.maint=[0]*G.n
        self.build_factor=build_factor
        self.retire_factor=retire_factor
    def _build(self,u):
        if self.indexed[u]: return
        self.metrics.propagation += len(self.G.adj[u])
        self.ifree[u]={v for v in self.G.adj[u] if self.mate[v]<0}
        self.indexed[u]=True; self.debt[u]=0; self.maint[u]=0
    def _retire(self,u):
        if not self.indexed[u]: return
        self.indexed[u]=False; self.ifree.pop(u,None); self.debt[u]=0; self.maint[u]=0
    def _set_free(self,x,state):
        if self.free[x]==state:return
        self.free[x]=state
        for y in self.G.adj[x]:
            if self.indexed[y]:
                self.metrics.propagation += 1; self.maint[y]+=1
                if state:self.ifree[y].add(x)
                else:self.ifree[y].discard(x)
                if self.maint[y] > self.retire_factor*max(1,len(self.G.adj[y])):
                    self._retire(y)
    def _match(self,u,v):
        self._set_free(u,False);self._set_free(v,False);self.mate[u]=v;self.mate[v]=u
    def _unmatch(self,u,v):
        self.mate[u]=self.mate[v]=-1;self._set_free(u,True);self._set_free(v,True)
    def find_free_neighbor(self,u):
        if self.indexed[u]:
            self.metrics.probes+=1
            return next(iter(self.ifree[u]),-1)
        before=self.metrics.probes
        ans=super().find_free_neighbor(u)
        spent=self.metrics.probes-before
        self.debt[u]+=spent
        if len(self.G.adj[u]) and self.debt[u] >= self.build_factor*len(self.G.adj[u]):
            self._build(u)
        return ans
    def update(self,op,u,v):
        if op=="add":
            existed=self.G.has_edge(u,v);self.G.add_edge(u,v)
            if not existed:
                if self.indexed[u] and self.free[v]:self.ifree[u].add(v)
                if self.indexed[v] and self.free[u]:self.ifree[v].add(u)
            if self.mate[u]<0 and self.mate[v]<0:
                self._match(u,v);self.metrics.recourse+=1
        else:
            if not self.G.has_edge(u,v):return
            was=self.mate[u]==v
            if self.indexed[u]:self.ifree[u].discard(v)
            if self.indexed[v]:self.ifree[v].discard(u)
            self.G.remove_edge(u,v)
            if was:
                self._unmatch(u,v);self.metrics.recourse+=1
                self.repair_vertex(u);self.repair_vertex(v)
    def validate_invariants(self):
        for u,v in enumerate(self.mate):
            if v>=0 and (self.mate[v]!=u or not self.G.has_edge(u,v)):return False
        for u in range(self.G.n):
            if self.indexed[u]:
                if self.ifree[u] != {v for v in self.G.adj[u] if self.mate[v]<0}:return False
        return self.is_maximal()

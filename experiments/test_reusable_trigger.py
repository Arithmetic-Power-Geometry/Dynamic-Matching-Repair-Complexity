"""Exhaustive reusable-trigger audit for the TMMR gadget.

Tests three reset strategies on all small set systems / active sets:
1. naive: re-add protected edge after a query;
2. explicit_restore: delete the query-created match (if any), then restore protected edge;
3. fresh_copy: consume a fresh protected center copy per query.

This is a structural audit, not a benchmark of Python wall-clock time.
"""
from itertools import product, combinations

def maximal(edges, mate):
    for u,v in edges:
        if mate.get(u) is None and mate.get(v) is None:
            return False
    return True

def build(r, sets, copies=1):
    edges=set(); mate={}
    for i in range(r):
        x=f"x{i}"; y=f"y{i}"
        edges.add(tuple(sorted((x,y)))); mate[x]=y; mate[y]=x
    for j,T in enumerate(sets):
        for c in range(copies):
            v=f"v{j}_{c}"; p=f"p{j}_{c}"
            edges.add(tuple(sorted((v,p)))); mate[v]=p; mate[p]=v
            for i in T: edges.add(tuple(sorted((v,f"x{i}"))))
    return edges,mate

def remove_edge(edges,u,v): edges.discard(tuple(sorted((u,v))))
def add_edge(edges,u,v): edges.add(tuple(sorted((u,v))))
def unmatch(mate,u,v):
    assert mate.get(u)==v and mate.get(v)==u
    mate[u]=None; mate[v]=None
def match(mate,u,v):
    assert mate.get(u) is None and mate.get(v) is None
    mate[u]=v; mate[v]=u

def activate(edges,mate,i):
    x,y=f"x{i}",f"y{i}"
    remove_edge(edges,x,y)
    if mate.get(x)==y: unmatch(mate,x,y)

def trigger(edges,mate,j,c=0):
    v,p=f"v{j}_{c}",f"p{j}_{c}"
    remove_edge(edges,v,p)
    if mate.get(v)==p: unmatch(mate,v,p)
    free=[x for x in sorted({b if a==v else a for a,b in edges if a==v or b==v})
          if mate.get(x) is None]
    witness=next((x for x in free if x.startswith("x")),None)
    if witness is not None: match(mate,v,witness)
    return witness

def naive_reset(edges,mate,j,c=0):
    v,p=f"v{j}_{c}",f"p{j}_{c}"
    add_edge(edges,v,p)
    if mate.get(v) is None and mate.get(p) is None: match(mate,v,p)

def explicit_restore(edges,mate,j,c=0):
    v,p=f"v{j}_{c}",f"p{j}_{c}"
    # If query matched v to an active candidate, undo that recourse.
    w=mate.get(v)
    changes=0
    if w is not None and w!=p:
        unmatch(mate,v,w); changes+=1
    add_edge(edges,v,p)
    if mate.get(v) is None and mate.get(p) is None:
        match(mate,v,p); changes+=1
    return changes

def encoded_active(mate,r):
    return {i for i in range(r) if mate.get(f"x{i}") is None}

def all_subsets(r):
    for mask in range(1<<r):
        yield {i for i in range(r) if mask>>i&1}

def audit(rmax=4):
    rows=[]
    for r in range(1,rmax+1):
        universe=list(all_subsets(r))
        # query families of size 1..min(3,2^r), exhaustive combinations
        for q in range(1,min(3,len(universe))+1):
            for sets in combinations(universe,q):
                for S in universe:
                    # naive repeated query of every center
                    e,m=build(r,sets)
                    for i in S: activate(e,m,i)
                    initial=set(S)
                    naive_ok=True
                    for j,T in enumerate(sets):
                        w=trigger(e,m,j)
                        if (w is not None)!=(bool(S & T)): naive_ok=False; break
                        naive_reset(e,m,j)
                        if not maximal(e,m) or encoded_active(m,r)!=initial:
                            naive_ok=False; break
                    # explicit restore
                    e2,m2=build(r,sets); total_restore=0; explicit_ok=True
                    for i in S: activate(e2,m2,i)
                    for j,T in enumerate(sets):
                        w=trigger(e2,m2,j)
                        if (w is not None)!=(bool(S & T)): explicit_ok=False; break
                        total_restore += explicit_restore(e2,m2,j)
                        if not maximal(e2,m2) or encoded_active(m2,r)!=initial:
                            explicit_ok=False; break
                    # fresh copies: one copy consumed per query occurrence; here one/query
                    e3,m3=build(r,sets,copies=1); fresh_ok=True
                    for i in S: activate(e3,m3,i)
                    for j,T in enumerate(sets):
                        w=trigger(e3,m3,j)
                        if (w is not None)!=(bool(S & T)): fresh_ok=False; break
                    rows.append((r,q,naive_ok,explicit_ok,fresh_ok,total_restore))
    return rows

if __name__=="__main__":
    rows=audit()
    print("cases",len(rows))
    for name,idx in [("naive",2),("explicit_restore",3),("fresh_copy",4)]:
        ok=sum(bool(x[idx]) for x in rows)
        print(name,ok,"/",len(rows))
    bad=[x for x in rows if not x[3]]
    print("explicit_restore_failures",len(bad))
    print("max_explicit_restore_changes",max((x[5] for x in rows),default=0))

"""Degree-controlled stress families for testing the structural parameter H(x)."""
from dmrc import DynamicGraph

def clustered_hubs(n,hubs,shared=True):
    G=DynamicGraph(n); hubs=min(hubs,max(1,n//4))
    if shared:
        # heavy vertices share the same periphery: high H(x) for hub-hub edges plus dense incidence.
        for h in range(hubs):
            for v in range(hubs,n): G.add_edge(h,v)
        for h in range(hubs):
            for j in range(h+1,hubs): G.add_edge(h,j)
    else:
        # disjoint hub neighborhoods: high degree but low heavy-neighbor incidence.
        per=list(range(hubs,n))
        for i,v in enumerate(per): G.add_edge(i%hubs,v)
    for v in range(hubs,n-1,2): G.add_edge(v,v+1)
    return G

def regular_ring(n,d):
    G=DynamicGraph(n);d=min(d,n-1)
    for u in range(n):
        for j in range(1,d//2+1):G.add_edge(u,(u+j)%n)
    return G

from dmrc import DynamicGraph

def star_of_pairs(k):
    """
    Separation-style graph.
    Center x=0 is matched to y=1.  x is adjacent to one endpoint of k matched pairs.
    Deleting (0,1) creates constant recourse but naive negative witness discovery
    may inspect k neighbors.
    """
    n=2*k+2
    G=DynamicGraph(n)
    G.add_edge(0,1)
    for i in range(k):
        a=2+2*i;b=a+1
        G.add_edge(a,b)
        G.add_edge(0,a)
    return G,(0,1)

def hub_graph(n,hubs=4):
    G=DynamicGraph(n)
    for h in range(min(hubs,n)):
        for v in range(hubs,n):
            G.add_edge(h,v)
    for v in range(hubs,n-1,2):
        G.add_edge(v,v+1)
    return G

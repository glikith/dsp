import networkx as nx

def build_rag(scenario):
    G = nx.DiGraph()
    for p in scenario['processes']:
        G.add_node(p, type='process')
    for r in scenario['resources']:
        G.add_node(r, type='resource')
    for p, info in scenario['processes'].items():
        for h in info.get('holds', []):
            G.add_edge(h, p)        # resource -> process
        for rq in info.get('requests', []):
            G.add_edge(p, rq)       # process -> resource
    return G

def build_wait_for_graph(scenario):
    W = nx.DiGraph()
    for p in scenario['processes']:
        W.add_node(p)
    holders = {}
    for p, info in scenario['processes'].items():
        for h in info.get('holds', []):
            holders.setdefault(h, []).append(p)
    for p, info in scenario['processes'].items():
        for rq in info.get('requests', []):
            for h in holders.get(rq, []):
                W.add_edge(p, h)    # P waiting for holder of rq
    return W

def detect_deadlock_wfg(W):
    return list(nx.simple_cycles(W))

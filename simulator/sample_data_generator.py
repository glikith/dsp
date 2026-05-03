from .data_collector import simulate_scenario
from .rag import build_wait_for_graph, detect_deadlock_wfg
import numpy as np

def scenario_to_features(scenario):
    procs = scenario['processes']
    num_procs = len(procs)
    num_res = len(scenario.get('resources', []))
    total_holds = sum(len(v['holds']) for v in procs.values())
    total_requests = sum(len(v['requests']) for v in procs.values())
    avg_hold = total_holds / max(1, num_procs)
    avg_req = total_requests / max(1, num_procs)
    frac_req = sum(1 for v in procs.values() if v['requests']) / max(1, num_procs)
    return [num_procs, num_res, total_holds, total_requests, avg_hold, avg_req, frac_req]

def generate_dataset(n=200, seed=42):
    X, y = [], []
    for i in range(n):
        sc = simulate_scenario(num_procs=5, num_res=4, chance_request=0.5, seed=seed+i)
        W = build_wait_for_graph(sc)
        label = 1 if detect_deadlock_wfg(W) else 0
        X.append(scenario_to_features(sc))
        y.append(label)
    return (np.array(X), np.array(y))

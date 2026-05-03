import random

def simulate_scenario(num_procs=5, num_res=4, chance_request=0.5, seed=None):
    random.seed(seed)
    resources=[f"R{i+1}" for i in range(num_res)]
    processes={}
    for i in range(num_procs):
        pid=f"P{i+1}"
        holds=[r for r in resources if random.random()<0.3]
        holds=list(set(holds))
        requests=[r for r in resources if r not in holds and random.random()<chance_request]
        processes[pid]={"holds":holds,"requests":requests}
    return {"processes":processes,"resources":resources}

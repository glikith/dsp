from simulator.data_collector import simulate_scenario
from simulator.rag import build_wait_for_graph, detect_deadlock_wfg
from simulator.predictor import DeadlockPredictor
import json

def pretty_print_scenario(s):
    print("Processes:")
    for p,info in s['processes'].items():
        print(f"  {p} holds={info['holds']} requests={info['requests']}")
    print("Resources:", s.get('resources', []))

def main():
    sc = simulate_scenario(num_procs=6, num_res=4, chance_request=0.6)
    pretty_print_scenario(sc)
    W = build_wait_for_graph(sc)
    cycles = detect_deadlock_wfg(W)
    if cycles:
        print("DEADLOCK DETECTED (WFG cycles):", cycles)
    else:
        print("No WFG cycles detected.")
    pred = DeadlockPredictor()
    pred.train(n=200)
    prob = pred.predict_proba(sc)
    print(f"Predicted deadlock probability: {prob:.2f}")
    with open("assets/last_cli_scenario.json", "w") as f:
        json.dump(sc, f, indent=2)
    print("Scenario saved to assets/last_cli_scenario.json")

if __name__ == "__main__":
    main()

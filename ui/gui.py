import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from simulator.data_collector import simulate_scenario
from simulator.rag import build_rag, build_wait_for_graph, detect_deadlock_wfg
from simulator.predictor import DeadlockPredictor

class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Simulator & Predictor")

        top = ttk.Frame(root)
        top.pack(fill='x', padx=8, pady=6)

        ttk.Button(top, text="Generate Scenario", command=self.generate).pack(side='left', padx=4)
        ttk.Button(top, text="Detect Deadlock", command=self.detect).pack(side='left', padx=4)
        ttk.Button(top, text="Predict Risk", command=self.predict).pack(side='left', padx=4)

        self.status = ttk.Label(root, text="Ready")
        self.status.pack(fill='x', padx=8, pady=4)

        self.fig, self.ax = plt.subplots(figsize=(6,4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        self.scenario = None
        self.predictor = DeadlockPredictor()
        try:
            self.predictor.train(n=300)
        except Exception:
            pass

    def generate(self):
        self.scenario = simulate_scenario(num_procs=6, num_res=4, chance_request=0.6)
        self.draw_rag()
        self.status.config(text="New scenario generated")

    def draw_rag(self):
        if not self.scenario:
            return
        G = build_rag(self.scenario)
        self.ax.clear()
        pos = nx.spring_layout(G, seed=2)
        nx.draw(G, pos, with_labels=True, node_size=700, ax=self.ax)
        self.fig.tight_layout()
        self.canvas.draw()

    def detect(self):
        if not self.scenario:
            messagebox.showinfo("Info", "Generate a scenario first")
            return
        W = build_wait_for_graph(self.scenario)
        cycles = detect_deadlock_wfg(W)
        if cycles:
            messagebox.showerror("Deadlock Detected", f"WFG cycles: {cycles}")
        else:
            messagebox.showinfo("No Deadlock", "No cycles detected")

    def predict(self):
        if not self.scenario:
            messagebox.showinfo("Info", "Generate a scenario first")
            return
        prob = self.predictor.predict_proba(self.scenario)
        messagebox.showinfo("Prediction", f"Estimated deadlock probability: {prob:.2f}")

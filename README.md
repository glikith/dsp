# DSP — Deadlock Simulator & Predictor

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-Graph-informational?style=flat)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat)
![psutil](https://img.shields.io/badge/psutil-System%20Monitoring-grey?style=flat)

> Simulate process-resource deadlock scenarios, detect cycles in resource allocation graphs, and predict deadlock risk using machine learning with both a GUI and a CLI.

---

## Overview

DSP models the classic OS deadlock problem using directed resource allocation graphs. It runs cycle detection to identify actual deadlocks, and uses a trained ML classifier to predict deadlock probability before one occurs. Available as a desktop GUI with live graph rendering or a terminal-based CLI for scripted use.

---

## Features

| Feature | Description |
|---|---|
| Deadlock Simulation | Define processes and resources, simulate allocation and wait states |
| Cycle Detection | Detects circular wait conditions in the resource allocation graph via NetworkX |
| Deadlock Prediction | scikit-learn classifier predicts deadlock risk from the current system state |
| Graph Visualization | Live rendering of the resource allocation graph using Matplotlib |
| Dual Interface | Full GUI mode (`run_gui.py`) and headless CLI mode (`run_cli.py`) |
| System Monitoring | psutil integration for real-time process and resource tracking |

---

## Tech Stack

```
Language       : Python 3.10+
Graph Engine   : NetworkX
ML             : scikit-learn, NumPy
Visualization  : Matplotlib, Pillow
System Info    : psutil
```

---

## How it works

**Cycle detection** runs a DFS on the directed RAG, a cycle means circular wait, which is deadlock by definition. The **ML predictor** is trained on simulated state features (allocation ratios, wait counts, resource contention) to flag high-risk states before the cycle actually forms.

---

## Author

**Gummadi Likith**

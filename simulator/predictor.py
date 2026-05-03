import numpy as np
try:
    from sklearn.linear_model import LogisticRegression
    SKL = True
except Exception:
    SKL = False

from .sample_data_generator import generate_dataset, scenario_to_features

class DeadlockPredictor:
    def __init__(self):
        self.model = LogisticRegression(solver='liblinear') if SKL else None

    def train(self, n=300):
        X, y = generate_dataset(n=n)
        if SKL:
            self.model.fit(X, y)
            return True
        return False

    def predict_proba(self, scenario):
        feat = np.array(scenario_to_features(scenario)).reshape(1, -1)
        if SKL and self.model:
            return float(self.model.predict_proba(feat)[0, 1])
        # heuristic fallback
        num_procs, num_res, total_holds, total_requests, avg_hold, avg_req, frac_req = feat.flatten().tolist()
        score = (total_requests + 1) / (total_holds + 2) * (1 + frac_req)
        return float(1.0 / (1.0 + np.exp(-0.7 * (score - 1))))

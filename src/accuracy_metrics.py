import numpy as np
from sklearn.metrics import roc_curve
from scipy.optimize import brentq
from scipy.interpolate import interp1d

class AccuracyEvaluator:
    @staticmethod
    def calculate_biometric_metrics(y_true: np.ndarray, y_scores: np.ndarray) -> dict:
        """
        Calculates EER, optimal operating threshold, and model accuracy metrics.
        """
        fpr, tpr, thresholds = roc_curve(y_true, y_scores, pos_label=1)
        fnr = 1 - tpr
        
        # Find Equal Error Rate point where FPR equals FNR
        eer = brentq(lambda x: 1. - x - interp1d(fpr, tpr)(x), 0., 1.)
        optimal_threshold = float(interp1d(fpr, thresholds)(eer))
        
        # Calculate accuracy at optimal threshold
        predictions = (y_scores >= optimal_threshold).astype(int)
        accuracy = float(np.mean(predictions == y_true))

        return {
            "equal_error_rate_pct": round(eer * 100, 4),
            "optimal_threshold": round(optimal_threshold, 4),
            "accuracy_pct": round(accuracy * 100, 2)
        }

if __name__ == "__main__":
    # Simulated validation vectors for testing metrics pipeline
    true_labels = np.array([1, 0, 1, 1, 0, 0, 1, 0])
    similarity_scores = np.array([0.89, 0.12, 0.76, 0.65, 0.22, 0.05, 0.91, 0.31])
    print(AccuracyEvaluator.calculate_biometric_metrics(true_labels, similarity_scores))

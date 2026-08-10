import numpy as np
from sklearn.metrics import roc_curve
from scipy.optimize import brentq
from scipy.interpolate import interp1d

def compute_eer(y_true, y_scores):
    """
    Calculates Equal Error Rate: the point where False Acceptance 
    matches False Rejection. Lower is better.
    """
    fpr, tpr, thresholds = roc_curve(y_true, y_scores, pos_label=1)
    fnr = 1 - tpr
    
    # Find the threshold where FPR == FNR
    eer = brentq(lambda x: 1. - x - interp1d(fpr, tpr)(x), 0., 1.)
    thresh = interp1d(fpr, thresholds)(eer)
    
    return eer, thresh

if __name__ == "__main__":
    print("Evaluation module loaded.")

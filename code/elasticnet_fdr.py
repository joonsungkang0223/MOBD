import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNetCV
from statsmodels.stats.multitest import multipletests

def run_elasticnet(X, y, l1_ratio=0.5, cv=5):
    model = ElasticNetCV(l1_ratio=l1_ratio, cv=cv, random_state=42)
    model.fit(X, y)
    coef = model.coef_
    selected = np.where(coef != 0)[0]
    return selected, coef

def compute_fdr(p_values, alpha=0.05):
    rejected, q_values, _, _ = multipletests(p_values, alpha=alpha, method='fdr_bh')
    return rejected, q_values
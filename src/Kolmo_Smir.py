from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

class Kolmonogorov_Smirnov:

    def __init__(self, calibration, holdout, simulation_data, model_name):
        self.calibration = calibration
        self.holdout = holdout
        self.simulation_data = simulation_data
        self.model_name = model_name

    def test(self):
        # Test on calibration data
        calibration_changes = np.diff(self.calibration).flatten()
        sim_changes = np.diff(self.simulation_data, axis=1).flatten()
    
        ks_calibration, p_calibration = stats.ks_2samp(calibration_changes, sim_changes)

    #  Test on holdout
        holdout_changes = np.diff(self.holdout).flatten()
        ks_holdout, p_holdout = stats.ks_2samp(holdout_changes, sim_changes)
    
    # Dict of results
        results = {
            'model': self.model_name,
            'train_ks': ks_calibration,
            'train_p': f'{p_calibration:.2f}',
            'train_pass': p_calibration > 0.05,
            'holdout_ks': ks_holdout,
            'holdout_p': f'{p_holdout:.2f}',
            'holdout_pass': p_holdout > 0.05,
            'generalization': 'Good' if (p_calibration > 0.05 and p_holdout > 0.05) else 'Poor'
        }   
    
        return results
    
    def plot(self):

        calibration_changes = np.diff(self.calibration.flatten())
        sim_changes = np.diff(self.simulation_data, axis=1).flatten()


        fig = sm.qqplot_2samples(calibration_changes, sim_changes, line='45')
        plt.title("Q-Q Plot: Two Unknown Distributions")
        plt.xlabel("Quantiles of Sample X")
        plt.ylabel("Quantiles of Sample Y")
        plt.show()

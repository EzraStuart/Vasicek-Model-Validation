import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class Vasicek:

    def __init__(self, data, T=20, dt=1/12, n_paths=1000):
        self.data = data
        self.T =T
        self.dt = dt
        self.n_paths = n_paths
    

    def logLik(self, params, rates):
        a, b , sigma = params

        if a <= 0 or sigma <= 0:
            return 1e10

        r_t = rates[:-1]
        r_t1 = rates[1:]

        # calcuate mean and variance from conditional expectation ad variance 
        mean = r_t +a*(b-r_t)*self.dt

        var = sigma**2*self.dt

        ll = -0.5*np.sum (np.log(2*np.pi*var) + ((r_t1 - mean)**2 / var))
        return -ll

    def MLE(self, rates):
        b_init = np.mean(rates)
        a_init = 0.1
        sigma_init = np.std(np.diff(rates)) / np.sqrt(self.dt)

        result = minimize(self.logLik, 
            x0=[a_init, b_init, sigma_init],
            args = (rates),
            method='L-BFGS-B',
            bounds=[(0.001, 5), (0, 100), (0.001, 100)])

        a, b, sigma = result.x
        return a,b,sigma   
    
    def simulation(self, rates, kappa, theta, sigma ,clip_negative=False):
        r0 = rates[-1]
        n_steps = int(self.T/self.dt)
        r = np.zeros((self.n_paths,n_steps))
        r[:,0] = r0
        eps = np.random.randn(self.n_paths,n_steps - 1)

        for n in range(1,n_steps):
            dr = kappa*(theta-r[:,n-1])*self.dt + sigma*np.sqrt(self.dt)*eps[:,n-1]
            r[:,n] = dr + r[:,n-1]
        
        if clip_negative:
            r[:, n] = np.clip(r[:, n], 0, None)
        return r


    def vasicek_residuals(self, rates, kappa, theta, sigma):
        residuals = np.zeros(len(rates) - 1)

        for i in range(len(rates) -1):
            expected_change = kappa*(theta - rates[i])*self.dt
            actual_change = rates[i+1] - rates[i]

            standardised_residuals = (actual_change - expected_change) / (sigma*np.sqrt(self.dt))
            residuals[i] = standardised_residuals
        return residuals


    def run(self):
        rates = self.data.flatten()
        kappa, theta, sigma = self.MLE(rates)
        vaSim = self.simulation(rates, kappa, theta, sigma)

        residuals = self.vasicek_residuals(rates, kappa, theta, sigma)
        return vaSim, kappa, theta, sigma , residuals

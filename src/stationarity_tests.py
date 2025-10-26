from statsmodels.tsa.stattools import adfuller, zivot_andrews, kpss
import pandas as pd

class stationarity:
    """"
    Tests for stationarity:

    Augmented Dickey Fuller test
    Zivot-Andrews Test
    KPSS Test
    """
    def __init__(self, data, sig = 0.05):
        self.data = data
        self.sig = sig

    def adf_test(self):
        result = adfuller(self.data)
        print('ADF Statistic:', result[0])
        print('p-value:', result[1])
        print('Critical Values:', result[4])
        if result[1] < self.sig:
            print('ADF conclusion: stationary') 
        else:
            print( 'ADF conculsion: non-stationary')

    def zatest(self):
        result = zivot_andrews(
            self.data,
            trim=0.1,
            maxlag=None,
            regression='ct',
            autolag='AIC'
        )
        print('ZA Statistic:', result[0])
        print('p-value:', result[1])
        print('Critical Values:', result[2])
        if result[1] < self.sig:
            print('Zivot-Andrews conclusion: stationary') 
        else:
            print( 'Zivot-Andrews conculsion: non-stationary')
    
    def kpss(self):
        result = kpss(self.data)
        print('KPSS Stat:', result[0])
        print('p-value:', result[1])
        print('crit-values:', result[3])
        if result[1] > self.sig:
            print('KPSS conclusion: stationary') 
        else:
            print( 'KPSS conculsion: non-stationary')
    
    def run(self):
        self.adf_test()
        self.zatest()
        self.kpss()

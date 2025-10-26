from src.models import Vasicek
from src.box_test import ljungBox
from src.Kolmo_Smir import Kolmonogorov_Smirnov
from src.stationarity_tests import stationarity
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load our data
    calibration = pd.read_csv('data/calibration.csv', index_col='Date')
    holdout = pd.read_csv('data/holdout.csv', index_col='Date')

    trainingSeries = calibration.values
    testSeries = holdout.values

    #stationarity tests:
    stationarityTests = stationarity(trainingSeries)
    stationarityTests.run()

    # Vasicek Model
    vasicekModel = Vasicek(trainingSeries, T =20, dt=1/2, n_paths=1000)
    vasicekSim, kappa, theta, sigma , residuals = vasicekModel.run()

    print(kappa, theta, sigma)
    # Kolmonongorov Smirnov Test
    KS = Kolmonogorov_Smirnov(trainingSeries, testSeries, vasicekSim, 'Vasicek')
    KS.test()
    KS.plot()
    
    #Ljung Box test
    ljb = ljungBox(residuals)
    lb_test = ljb.test()
    ljb.plot(lb_test)

if __name__ == '__main__':
    main()
# Vasicek Model Validation

## Project Overview

This project provides a comprehensive analysis and validation of the Vasicek model for modeling US Treasury yields. The primary goal is to assess the model's effectiveness in capturing the dynamics of interest rates, which is crucial for applications in financial risk management, asset pricing, and economic forecasting. 

### Findings:
- The 10 Year Yields failed all stationarity tests at a 5% significance level
  - Making the Vasicek Model innapropriate as it assumes stationarity
- Despite this, the model performed extremely well under holdout Kolmonogorov tests
- Therefore, concluded that the model was apt for the purpose of long term forecasting, but could not accurately capture short term dynamics

The analysis involves:
- **Data Acquisition and Processing:** Fetching, cleaning, and preparing historical US 10-Year Treasury yield data from the FRED API.
- **Model Calibration:** Estimating the Vasicek model parameters (kappa, theta, sigma) using Maximum Likelihood Estimation (MLE).
- **Stochastic Simulation:** Simulating future interest rate paths using the calibrated Vasicek model.
- **Rigorous Model Validation:** A suite of statistical tests to evaluate the model's performance, including:
    - **Stationarity Tests:** ADF, Zivot-Andrews, and KPSS tests to check for stationarity in the time series.
    - **Goodness-of-Fit:** Kolmogorov-Smirnov test to compare the distribution of simulated rate changes with historical data.
    - **Residual Analysis:** Ljung-Box test to check for autocorrelation in model residuals.
- **Comparative Analysis:** The Vasicek model's performance is compared against a baseline Geometric Brownian Motion (GBM) model.

## Tech Stack

- **Python:** The core programming language for the project.
- **Libraries:**
    - **pandas:** For data manipulation and analysis.
    - **NumPy:** For numerical operations.
    - **SciPy:** For scientific and technical computing, including optimization for MLE.
    - **statsmodels:** For statistical tests, including stationarity tests and Ljung-Box test.
    - **matplotlib:** For data visualization.
    - **fredapi:** For fetching data from the Federal Reserve Economic Data (FRED) database.

## Features

- **Automated Data Pipeline:** Scripts to automatically download and process the latest interest rate data.
- **Modular Code Structure:** The project is organized into modules for data handling, modeling, and statistical tests, promoting code reusability and maintainability.
- **In-depth Validation Suite:** A comprehensive set of statistical tests to rigorously validate the model's assumptions and performance.
- **Jupyter Notebook for Analysis:** A detailed Jupyter notebook (`rough_workbook.ipynb`) that walks through the entire analysis, from data exploration to model validation, complete with visualizations and interpretations.

This script will:
1.  Load the pre-processed calibration and holdout data.
2.  Perform stationarity tests on the training data.
3.  Calibrate the Vasicek model.
4.  Run simulations.
5.  Perform Kolmogorov-Smirnov and Ljung-Box tests.
6.  Display the results and plots.

For a more interactive and detailed exploration of the analysis, you can open and run the `rough_workbook.ipynb` in a Jupyter environment.

## Key Findings

- The Vasicek model demonstrates a reasonable fit to the historical data, capturing the mean-reverting behavior of interest rates.
- The Kolmogorov-Smirnov test indicates that the distribution of simulated rate changes is statistically similar to the historical distribution on the training data, but shows some divergence on the holdout set.
- The Ljung-Box test on the residuals suggests that the model effectively captures the temporal dependencies in the data.
- The model's performance, while not perfect, is a significant improvement over a simple Geometric Brownian Motion model, highlighting the importance of mean reversion in interest rate modeling.

## Future Work

- **Parameter Sensitivity Analysis:** Investigate how the model's predictions change with variations in the calibrated parameters.
- **Alternative Models:** Implement and compare the Vasicek model with other short-rate models like Cox-Ingersoll-Ross (CIR) or Hull-White.
- **Multi-Factor Models:** Explore multi-factor models to capture more complex interest rate dynamics, such as the shape of the yield curve.
- **Application to Derivatives Pricing:** Use the simulated interest rate paths to price interest rate derivatives, such as bonds, swaps, and options.

## Contact

For any questions or opportunities, please feel free to reach out.

---
*This README is designed to be a comprehensive overview of the project, suitable for showcasing on a GitHub profile to attract recruiters and demonstrate a strong foundation in quantitative finance and data analysis.*

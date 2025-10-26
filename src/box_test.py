import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox


class ljungBox:
    def __init__(self, residuals):
        self.residuals = residuals

    def test(self, max_lag=20):
        lb_test = acorr_ljungbox(self.residuals, lags=max_lag, return_df=True)

        print("="*60)
        print("LJUNG-BOX TEST FOR RESIDUAL AUTOCORRELATION")
        print("="*60)
        print(f"\nNull Hypothesis: Residuals are independently distributed (no autocorrelation)")
        print(f"Alternative: Residuals exhibit autocorrelation at some lag\n")
        print(f"Significance level: 0.05")
        print(f"If p-value < 0.05, reject null (residuals have autocorrelation)\n")

# Show results for selected lags
        print(lb_test.head(10))

        significant_lags = lb_test[lb_test['lb_pvalue'] < 0.05]
        if len(significant_lags) > 0:
            print(f"\n FAIL: Significant autocorrelation detected at {len(significant_lags)} lag(s)")
            print(f"Lags with p < 0.05: {significant_lags.index.tolist()}")
            print("\nInterpretation: Model has NOT captured all temporal structure.")
            print("Consider: More complex model or check parameter estimates.")
        else:
            print(f"\n PASS: No significant autocorrelation detected")
            print("Interpretation: Model adequately captures temporal dependence.")

        return lb_test


    def plot(self, lb_test):
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Residuals over time
        axes[0].plot(self.residuals, linewidth=0.8)
        axes[0].axhline(y=0, color='r', linestyle='--', alpha=0.5)
        axes[0].axhline(y=2, color='orange', linestyle='--', alpha=0.3, label='±2σ')
        axes[0].axhline(y=-2, color='orange', linestyle='--', alpha=0.3)
        axes[0].set_title(' Residuals Over Time', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Time')
        axes[0].set_ylabel('Residual')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)


        # Ljung-Box p-values by lag
        axes[1].plot(lb_test.index, lb_test['lb_pvalue'], marker='o', linewidth=2)
        axes[1].axhline(y=0.05, color='r', linestyle='--', label='5% significance')
        axes[1].set_title('Ljung-Box Test P-values by Lag', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('Lag')
        axes[1].set_ylabel('P-value')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        axes[1].set_ylim(-0.05, 1.05)

        plt.tight_layout()
        plt.show()

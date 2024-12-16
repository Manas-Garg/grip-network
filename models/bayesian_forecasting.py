import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load and Prepare Data
data = pd.read_csv("processed/processed_climate_data.csv")
data = data.set_index("timestamp")
data = data["co2"].values

# Define Bayesian Model
with pm.Model() as model:
    # Priors for unknown model parameters
    alpha = pm.Normal("alpha", mu=0, sigma=10)
    beta = pm.Normal("beta", mu=0, sigma=10)
    sigma = pm.HalfNormal("sigma", sigma=1)

    # Expected value of outcome
    x = np.arange(len(data))
    mu = alpha + beta * x

    # Likelihood (sampling distribution) of observations
    y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=data)

    # Posterior Inference
    trace = pm.sample(2000, return_inferencedata=False)

# Plot Results
pm.plot_posterior(trace)
plt.show()

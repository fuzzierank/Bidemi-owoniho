import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
import os

# Load data
df = pd.read_csv('data/historical_inflation.csv', parse_dates=['date'])
df.set_index('date', inplace=True)

# Create lags
for lag in [1,2,3,6]:
    df[f'usd_ngn_lag{lag}'] = df['usd_ngn_avg'].shift(lag)

df.dropna(inplace=True)

# Simple OLS
X = sm.add_constant(df['usd_ngn_avg'])
y = df['headline_yoy']
model = sm.OLS(y, X).fit()
print(model.summary())

# Multiple lags
X_multi = df[[f'usd_ngn_lag{lag}' for lag in [0,1,2,6] if f'usd_ngn_lag{lag}' in df.columns or lag==0]]
X_multi = sm.add_constant(X_multi)
model_multi = sm.OLS(y, X_multi).fit()
print(model_multi.summary())

# Plot
plt.figure(figsize=(12,6))
plt.plot(df.index, df['headline_yoy'], label='Headline Inflation')
plt.plot(df.index, df['usd_ngn_avg']/100, label='USD/NGN (scaled)')
plt.title('Inflation vs Naira Exchange Rate')
plt.legend()
plt.savefig('visualizations/inflation_vs_naira.png')
plt.close()

print("✅ Regression analysis completed!")

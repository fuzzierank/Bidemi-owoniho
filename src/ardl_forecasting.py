import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ARDL
import os

# Load data
df = pd.read_csv('data/historical_inflation.csv', parse_dates=['date'])
df.set_index('date', inplace=True)
df = df.sort_index()

print("Data shape:", df.shape)
print(df.tail())

# ARDL Model: Inflation \~ lags of itself + lags of Naira rate
y = df['headline_yoy']
X = df[['usd_ngn_avg']]

model = ARDL(y, lags=2, exog=X, order=2, trend='c')  # ARDL(2,2)
results = model.fit()

print(results.summary())

# Forecasting
forecast_steps = 6
future_exog = pd.DataFrame({'usd_ngn_avg': [1370] * forecast_steps}, index=pd.date_range(start=df.index[-1], periods=forecast_steps, freq='ME'))
forecast = results.forecast(steps=forecast_steps, exog=future_exog)

print("\nFuture Forecast (next 6 periods):")
print(forecast)

# Plot
plt.figure(figsize=(12,6))
plt.plot(df.index, y, label='Actual Headline Inflation')
future_index = forecast.index
plt.plot(future_index, forecast, label='ARDL Forecast', linestyle='--')
plt.title('Nigeria Inflation ARDL Forecast with Naira Impact')
plt.legend()
plt.savefig('visualizations/ardl_forecast.png')
plt.close()

print("✅ ARDL analysis and forecast completed!")

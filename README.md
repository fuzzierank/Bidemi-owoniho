# Bidemi-owoniho
Nigeria Inflation Analysis with Naira exchange rate impact, lag regression &amp; ARDL forecasting (June 2026)
# Nigeria Inflation Analysis

## Overview
Comprehensive analysis of Nigeria's inflation trends (as of June 2026) using NBS data. Focuses on **Naira exchange rate impact**, lagged regression, and **ARDL forecasting models**.

**Latest (May 2026)**:  
- Headline Inflation (YoY): **15.93%**  
- Food Inflation: **16.96%**

## Key Insights
- Strong pass-through from Naira depreciation to inflation (especially food) with 6-month lag.
- Inflation moderated from 2024 peak (\~34%) due to recent Naira stability.
- ARDL models capture dynamic short- and long-run effects.

## Repository Structure
- `data/` — Historical inflation + USD/NGN data
- `notebooks/` — Interactive Jupyter analysis
- `src/` — Python scripts (data loader, regression, forecasting)
- `visualizations/` — Plots

## Setup & Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/Nigeria_Inflation_ARDL.ipynb

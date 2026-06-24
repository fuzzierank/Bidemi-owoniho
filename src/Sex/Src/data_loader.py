import pandas as pd
import os

def load_historical_csv() -> pd.DataFrame:
    """Load sample historical data."""
    csv_path = "data/historical_inflation.csv"
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")
    df = pd.read_csv(csv_path, parse_dates=['date'])
    df.set_index('date', inplace=True)
    return df

if __name__ == "__main__":
    try:
        df = load_historical_csv()
        print("✅ Sample data loaded successfully!")
        print(df.head())
        print("\nColumns:", df.columns.tolist())
    except Exception as e:
        print(f"❌ Error: {e}")

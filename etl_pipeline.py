import pandas as pd

# 1. Extract
def extract(path):
    df = pd.read_csv(path)
    return df

# 2. Transform
def transform(df):
    # No Gender column to encode
    df = df.dropna()
    return df

# 3. Load
def load(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    df_raw = extract("Social_Network_Ads.csv")
    df_clean = transform(df_raw)
    load(df_clean, "cleaned_ads.csv")

from scipy.io import arff
import pandas as pd
data, meta = arff.loadarff('PhishingData.arff')
df = pd.DataFrame(data)
for col in df.select_dtypes([object]).columns:
    df[col] = df[col].str.decode('utf-8')
df.to_csv("/home/kali/Documents/PhishingData.csv", index=False)
csv_path = "/home/kali/Documents/PhishingData.csv"
print(f"successfully saved CSV file: {csv_path}")
df = pd.read_csv('/home/kali/Documents/PhishingData.csv')
print(df)

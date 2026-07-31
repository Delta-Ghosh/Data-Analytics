import pandas as pd
df = pd.read_csv("sample_data_small.csv")
df = df.dropna()
print(df)

df = pd.read_excel("data.xlsx") #specify the path to your Excel file

# Read a specific sheet:
pd.read_excel("data.xlsx", sheet_name="Sheet1")

# List all sheet names:
pd.ExcelFile("data.xlsx").sheet_names
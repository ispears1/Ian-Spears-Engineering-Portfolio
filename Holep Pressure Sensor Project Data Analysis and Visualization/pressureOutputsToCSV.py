import csv
import pandas as pd

# ---- Load the CSV files ----
file1 = r"C:\Users\iansp\OneDrive\Desktop\Pressure Sensor data\Station 5 Third 8-21.csv"
file2 = r"C:\Users\iansp\OneDrive\Desktop\Pressure Sensor data\Station 5 Third 8-22.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# ---- Clean column names (in case of extra spaces) ----
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

directions = ["North", "East", "South", "West"]

df1_norm = df1.copy()
df2_norm = df2.copy()

for direction in directions:
    df1_norm[direction] = df1[direction] - df1[direction].mean()
    df2_norm[direction] = df2[direction] - df2[direction].mean()

csvFile = open('newOutputs.csv', 'w', newline='')
writer = csv.writer(csvFile)
writer.writerow(['North Avg 1', 'East Avg 1', 'South Avg 1', 'West Avg 1', 'North Avg 2', 'East Avg 2', 'South Avg 2', 'West Avg 2', 'North Std 1', 'East Std 1', 'South Std 1', 'West Std 1', 'North Std 2', 'East Std 2', 'South Std 2', 'West Std 2'])

row = []
for direction in directions:
    row.append(df1_norm[direction].mean())
for direction in directions:
    row.append(df2_norm[direction].mean())
for direction in directions:
    row.append(df1_norm[direction].std())
for direction in directions:
    row.append(df2_norm[direction].std())

writer.writerow(row)

csvFile.close()
print("Completed Successfully!")
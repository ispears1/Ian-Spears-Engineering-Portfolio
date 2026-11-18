import pandas as pd
import toSeconds
import csv

columnNames = ['Fri Weight', 'Fri Time', 'Sat Weight', 'Sat Time', 'North Norm Avg Fri', 'East Norm Avg Fri', 'South Norm Avg Fri', 'West Norm Avg Fri', 'North Norm Avg Sat', 'East Norm Avg Sat', 'South Norm Avg Sat', 'West Norm Avg Sat', 'North Norm Std Fri', 'East Norm Std Fri', 'South Norm Std Fri', 'West Norm Std Fri', 'North Norm Std Sat', 'East Norm Std Sat', 'South Norm Std Sat', 'West Norm Std Sat']

dataFile = r"C:\Users\iansp\OneDrive\Desktop\Chicago Adv HoLEP Data\Pressure Sensor Data.xlsx"

workingFile = pd.read_excel(dataFile)
workingFile = workingFile.drop('Name', axis = 1)


workingFile["Fri Time"] = workingFile["Fri Time"].apply(toSeconds.to_seconds)
workingFile["Sat Time"] = workingFile["Sat Time"].apply(toSeconds.to_seconds)

csvFile = open('correlations.csv', 'w', newline='')
writer = csv.writer(csvFile)

for i in range(20):
    for j in range(i+1, 20):
        corr = workingFile.iloc[:,i].corr(workingFile.iloc[:,j])
        writer.writerow([columnNames[i], columnNames[j], corr])

print("Done!")
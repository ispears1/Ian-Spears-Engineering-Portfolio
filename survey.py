import csv
indicator = "whatever I want"

with open("survey.csv", "a+") as csvFile:
    csvWriter = csv.writer(csvFile)
    while(indicator != "y" and indicator != "Y"):
        csvWriter.writerow([input("Input your name:\n"), input("Input your favorite color:\n")])
        indicator = input("Do you want to quit (y or n)?\n")

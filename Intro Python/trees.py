import csv
totalCircumference=0
totalHeight=0
totalVolume=0
maxIndex=0

with open("trees.csv", "r") as csvFile:
    csvReader = csv.reader(csvFile)
    for (i,line) in enumerate(csvReader):
        if(i>0):
            maxIndex=float(line[0].strip())
            totalCircumference += float(line[1].strip())
            totalHeight += float(line[2].strip())
            totalVolume += float(line[3].strip())
    print("Mean tree circumference, height, and volume are {0:.1f} in, {1:.1f} ft, and {2:.1f} ft^3 respectively.".format(totalCircumference/maxIndex,totalHeight/maxIndex,totalVolume/maxIndex))

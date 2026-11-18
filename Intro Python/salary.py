#This program calculates the salary of doctors based on the patients.txt file
#and then displays the pays in a historgram

range1=0
range2=0
range3=0
range4=0
range5=0

with open("patients.txt", "r") as myFile:
    for line in myFile:
        salary = 200000 + ((int(line)//5)*10000)
        if(salary <= 200000):
            range1 += 1
        elif(salary <= 250000):
            range2 += 1
        elif(salary <= 300000):
            range3 += 1
        elif(salary <= 350000):
            range4 +=1
        else:
            range5 += 1

print("<= 200,000      |",end="")
for i in range(range1):
    print("*", end="")
print()
print("200,001-250,000 |", end="")
for i in range(range2):
    print("*", end="")
print()
print("250,001-300,000 |", end="")
for i in range(range3):
    print("*", end="")
print()
print("300,001-350,000 |", end="")
for i in range(range4):
    print("*", end="")
print()
print(">= 350,001      |",end="")
for i in range(range5):
    print("*", end="")
    
with open("historgram.txt", "w") as newFile:
    newFile.write("<= 200,000      |")
    for i in range(range1):
        newFile.write("*")
    newFile.write("\n")
    newFile.write("200,001-250,000 |")
    for i in range(range2):
        newFile.write("*")
    newFile.write("\n")
    newFile.write("250,001-300,000 |")
    for i in range(range3):
        newFile.write("*")
    newFile.write("\n")
    newFile.write("300,001-350,000 |")
    for i in range(range4):
        newFile.write("*")
    newFile.write("\n")
    newFile.write(">= 350,001      |")
    for i in range(range5):
        newFile.write("*")

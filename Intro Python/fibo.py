#This program takes an integer from the user, and displays that many number of Fibonacci numbers.
n = int(input("Enter the number of Fibonacci numbers to be displayed:"))
numA=1
numB=1

for i in range(n):
    if(numA<=numB):
        print(numA, end=' ')
        numA=numA+numB
    else:
        print(numB, end=' ')
        numB=numA+numB

#This program takes an integer from the user, and displays that many of even Fibonacci numbers.
n=int(input("Enter the number of even Fibonacci numbers to be displayed:"))
numA=1
numB=1
count=0

while (count<n):
    if(numA<=numB):
        if(numA%2==0):
            print(numA, end = ' ')
            count=count+1
        numA=numA+numB
    else:
        if(numB%2==0):
            print(numB, end = ' '1)
            count=count+1
        numB=numB+numA

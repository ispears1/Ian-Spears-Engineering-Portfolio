#This program calculates the nth order Taylor series of cos(x) where n comes from the user, and displays the percent error compared to the math.cos function
import math
n=int(input("Enter n:"))
x=float(input("Enter x:"))
sum=0

for k in range(n+1):
    sum = sum + (math.pow(-1, k) * math.pow(x, 2*k) / math.factorial(2*k))
print("cox(x) =", sum)

percentError = ((sum-math.cos(x)) / math.cos(x)) * 100

print("Percent error =", percentError)
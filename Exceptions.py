import numpy as np

def divide(a,b):
    c = 0
    try:
        c = float(a)/float(b)
    except ValueError:
        print("Error: Inputs are not numbers")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except:
        print("Error: Could not divide")
    return c

def getAge():
    c = 0
    try:
        c=float(input("Enter your age:\n"))
    except ValueError:
        print("Error: Input is not a number")
    except:
        print("Error: Unable to display age")
    if(c<0):
        print("Error: Input is a negative number")
        c=0
    return "You are " + str(c) + " years young!"

def squareInteger():
    num = -1
    while(num==-1):
        try:
            num=int(input("Please enter a positive integer:\n"))
            if(num<0):
                print("Error: Input is not a positive integer. Try again.")
                num=-1
        except ValueError:
            print("Error: Input is not understandable. Try again.")
            num=-1
        except:
            print("Error: Unable to compute. Try again.")
            num=-1
    return num * num

def totalItems():
    items=input("Enter grocery list and amount of each item:\n")
    thisSum = 0
    l = items.split()
    for item in l:
        try:
            thisSum += int(item)
        except:
            pass
    return thisSum
    

def matrixMultiply():
    c = 0
    try:
        A= np.arange(12).reshape(3,4)
        B=np.arange(16).reshape(4,4)
        c=A@B
    except ValueError:
        print("Shape of arrays do not match.")
    except:
        print("Error: Could not compute.")
    return c
    
print(totalItems())
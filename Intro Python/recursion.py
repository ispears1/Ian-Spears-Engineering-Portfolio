import math
def countdown(n):
    if(n<=0):
        return "Go!" #Base case
    else:
        return str(n)+" " + countdown(n-1) #Recursive Case

def factorial(n):
    if(n<=0):
        return 1
    else:
        return n * factorial(n-1)
    
def mystery(value, low = 1, high = None):
    if value < 1: raise Exception("Error: value < 1")
    if low < 1: raise Exception("Error: low < 1")

    if high is None: high = value

    while True: 
        guess = (high - low) / 2 + low        
        if math.isclose(guess**2, value):
            return guess
        elif guess**2 > value:
            high = guess            
        else:
            low = guess

def mysteryR(value, low=1, high=None):
    if value < 1: raise Exception("Error: value < 1")
    if low < 1: raise Exception("Error: low < 1")

    if high==None:
        high = value
    
    guess = (high - low) / 2 + low        
    
    if math.isclose(guess**2, value):
        return guess
    elif guess**2 > value:
        return mysteryR(value, low=1, high=guess)
    else:
        return mysteryR(value, low=guess, high=high)

def fibo(n):
    startingFibo = [1,1]
    if(n==0):
        return []
    if(n==1):
        return [1]
    else:
        for i in range(1,n-1):
            startingFibo.append(int(startingFibo[i-1] + startingFibo[i]))
        return startingFibo
    
def fiboR(n):
    """
    Returns Fibonacci sequence of length n (Recursive)
    """
    if n <= 2: # Base case
        return [1]*n 
    else: # Recursive case
        seq = fiboR(n-1)
        seq.append(seq[n-2]+seq[n-3])
        return seq
    
print(fiboR(4))

#This program holds the functions used to convert between Fahrenheit, Celcius, and Kelvin
def C2F(temp):
    newtemp= (temp * 9 / 5) + 32
    return newtemp

def F2C(temp):
    newtemp= ((temp-32)*5/9)
    return newtemp

def C2K(temp):
    return temp+273.15

def K2C(temp):
    return temp-273.15

def F2K(temp):
    newtemp = F2C(temp)
    return newtemp+237.15

def K2F(temp):
    newtemp = K2C(temp)
    return newtemp-273.15

if __name__=='_main_':
    print("")
else:
    print("")
    

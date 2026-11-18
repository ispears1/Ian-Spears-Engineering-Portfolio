import tempFunctions

user_temp = float(input("Enter the temperature you would like converted:\n"))
input_type = input("Enter this temperature's scale (F for Fahrenheit, C for Celsius, or K for Kelvin):\n")
temp_type=input_type.lower()

if(temp_type=="f" or temp_type=="fahrenheit"):
    print(tempFunctions.F2C(user_temp), "°C and", tempFunctions.F2K(user_temp), "K")
elif(temp_type=="c" or temp_type=="celsius"):
    print(tempFunctions.C2F(user_temp), "°F and", tempFunctions.C2K(user_temp), "K")
elif(temp_type=="k" or temp_type=="kelvin"):
    print(tempFunctions.K2F(user_temp), "°F and", tempFunctions.K2C(user_temp), "°C")
else:
    print("Invalid temperature scale")

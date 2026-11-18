start_year = int(input("Enter starting year:"))
numYears = int(input("Enter number of leap years to be displayed:"))
count = 0
while count < numYears:
    if(start_year%100 == 0):
        if(start_year%400 == 0):
            print(start_year)
            count=count+1
    elif(start_year%4==0):
        print(start_year)
        count=count+1
    start_year=start_year+1

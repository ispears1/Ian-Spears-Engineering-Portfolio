cash = float(input("Enter amount to be made into change: \n"))
cash = int(cash * 100)
print("You can make", cash, "cents by using:")
change = cash // 25
print(change, "quarter(s)")
cash = cash%25
change = cash //10
print(change, "dime(s)")
cash = cash%10
change = cash //5
print(change, "nickel(s), and")
cash = cash%5
print(change, "penny(ies)")

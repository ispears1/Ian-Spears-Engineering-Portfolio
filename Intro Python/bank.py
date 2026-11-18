class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = [balance]
    
    def getBalance(self):
        return self.balance
    
    def getOwner(self):
        return self.owner
    
    def __str__(self):
        return "%s's account contains %.2f dollars" % (self.owner, self.balance)
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.history.append(float("%.2f" % (self.balance)))
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.history.append(float("%.2f" % (self.balance)))
        
    def transferTo(self, other, amount):
        self.balance = self.balance - amount
        self.history.append(float("%.2f" % (self.balance)))
        other.balance = other.balance + amount
        other.history.append(float("%.2f" % (other.balance)))
    
    def getHistory(self):
        return self.history
    
class SavingsAccount(Account):
    def __init__(self, owner, balance, interestRate):
        Account.__init__(self, owner, balance)
        self.interestRate = interestRate
    
    def getInterestRate(self):
        return self.interestRate
    
    def addInterest(self):
        self.balance = self.balance + (self.balance * (self.interestRate / 100))
        self.history.append(float("%.2f" % (self.balance)))
    
if __name__ == "__main__":
    a = SavingsAccount("Mike", 50, 10)
    b = Account("Dan", 100)
    c = SavingsAccount("Dan", 400, 1)
    c.addInterest()
    print(c)
    print(a)
    print(b)
    a.deposit(90.80)
    a.withdraw(30)
    a.transferTo(b, 3)
    a.addInterest()
    print(a)
    print(b)
    print("Dan's history:", b.getHistory())
    print("Mike's history:", a.getHistory())

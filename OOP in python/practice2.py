class Account:
    
    def __init__(self,bal,acc):
        self.balance = bal
        self.acount = acc
        
    def debit(self,amount):
        self.balance -= amount
        print("BDT",amount,"Was Debited")
        print("Your Current Balance is ",self.balance)
        
    def credit(self,amount):
        self.balance += amount
        print("BDT",amount,"Was Credited")
        print("Your Current Balance is ",self.balance)

        
    def total(Self):
        return Self.balance
    
    
user1 = Account(9000,"SMSA31")
user1.debit(1000)
user1.credit(7000)
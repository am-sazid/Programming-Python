class Account:
    
    def __init__(self,bal,acc):
        self.ballance = bal
        self.Account_No = acc
        
    def debit(self,amount):
        self.ballance -= amount
        print("BDT",amount,"Was Debited")
        print("Your Ballance Is ",self.total())
        
    def credit(self,amount):
        self.ballance += amount
        print("BDT",amount,"Was Credit")
        print("Your Ballance Is ",self.total())
        
    def total(self):
        return self.ballance
        
        
acc1 = Account(10000,"SMSA31")
acc1.debit(1000)
acc1.credit(500)
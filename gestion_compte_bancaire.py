class Account:

    def __init__(self,balance = 0):
        self.balance = balance
    
    def getBalance(self):
        balance = self.balance
        return balance
       
    
    def deposer(self,montant):
        self.balance = self.balance + montant
        
    
    def retirer(self,montant):
        self.balance = self.balance - montant
    

compte = Account()
compte.deposer(10)
print(f"le compte est a {compte.getBalance()}")

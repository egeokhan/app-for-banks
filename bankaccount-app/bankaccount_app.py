
class Account:

    def __init__(self,name,number,balance):

        self.name = name
        self.number = number
        self.balance = balance
    def AccountInfo(self):
        print("Name:",self.name)
        print("Number:",self.number)
        print("Balance:",self.balance)
    def WithdrawMoney(self,amount):
        if(self.balance - amount < 0):
            print("You do not have enough balance.")
        else:
            oldbalance = self.balance
            self.balance -= amount
            print("Old Balance:",oldbalance)
            print("New Balance:",self.balance)
    def AddMoney(self,amount):
        oldbalance = self.balance
        self.balance += amount
        print("Old Balance:",oldbalance)
        print("New Balance:",self.balance)
    def ChangeInformation(self,newname,newnumber):
        verification = input("Your information will be changed, are you sure? Yes/No: ")
        if(verification.lower() == "yes"):
            self.name = newname
            self.number = newnumber
            print("Your Information Has Been Changed:")
            account.AccountInfo()
        elif(verification.lower() == "no"):
            print("Transaction canceled:")
            account.AccountInfo()        
account = Account("Ege",12345,1000)
account.AccountInfo()
account.WithdrawMoney(100)
account.AddMoney(100)
account.ChangeInformation("Ege123","0555 000 00 00")
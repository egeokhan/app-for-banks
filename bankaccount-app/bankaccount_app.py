class Account:        
    def __init__(self,name,number,balance,password):
        self.name = name
        self.number = number
        self.balance = balance
        self.password = password
    def Login(self):
        file = open("Accounts.txt","r")
        login = False
        for info in file:
            list = info.split(";")
            if self.name == list[0] and self.password == list[1]:
                login = True
                self.number = list[2]
                self.balance = int(list[3])
        file.close()
        if(login == False):
            print("We couldn't find your account...")
            question = input("Would you like to create an account? Y/N: ")
            result = False
            if question.upper() == "Y":
                file1 = open("Accounts.txt","a")
                file2 = open("Accounts.txt","r")
                createusername = input("Username: ")
                for names in file2:
                    liste = names.split(";")
                    if createusername == liste[0]:
                        result = True
                file2.close()
                if result == False:
                    createpassword = input("Password: ")
                    createnumber = input("Number: ")
                    file1.write("\n{};{};{};0".format(createusername,createpassword,createnumber))
                    file1.close()
                    print("Your account has been created. You can login.")
                elif result == True:
                    print("Please enter a different username...")
            elif question.upper() == "N":
                print("Okay, Goodbye!")
        elif(login == True):
            print("Login successful...")
            account.AccountInfo()
            select = int(input("Select an Action:\nPress 1 for account information\nPress 2 to withdraw money\nPress 3 to add money\nPress 4 to change your information\nPress: "))
            if select == 1:
                account.AccountInfo()
            elif select == 2:
                amount = int(input("Amount to be withdrawn: "))
                account.WithdrawMoney(amount)
            elif select == 3:
                amount = int(input("Amount to add: "))
                account.AddMoney(amount)
            elif select == 4:
                newname = input("New Name: ")
                newnumber = input("New Number: ")
                account.ChangeInformation(newname,newnumber)
    def AccountInfo(self):
        print("Name:",self.name)
        print("Number:",self.number)
        print("Balance:",self.balance)
    def WithdrawMoney(self,amount):
        if(int(self.balance) - amount < 0):
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
name = input("Username: ")    
password = input("Password: ")
account = Account(name,None,None,password)
account.Login()
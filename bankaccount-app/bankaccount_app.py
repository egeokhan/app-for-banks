class Account:
    def __init__(self,name,number,balance,password):
        self.name = name
        self.number = number
        self.balance = balance
        self.password = password
        self.degisken = 0
        self.list = ["0"]
        self.list.clear()
############################################################################################################
    def Login(self):
        file = open("Accounts.txt","r")
        login = False
        for info in file:
            self.degisken += 1
            liste = info.split(";")
            if self.name == liste[0] and self.password == liste[1]:
                self.number = liste[2]
                self.balance = int(liste[3])
                login = True
                break
        file.close()
        filenew = open("Accounts.txt","r")
        self.list.append(filenew.readlines())
        filenew.close()
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
                newpassword = input("New Password: ")
                newnumber = input("New Number: ")
                account.ChangeInformation(newname,newpassword,newnumber)
############################################################################################################
    def AccountInfo(self):
        print("Name:",self.name)
        print("Number:",self.number)
        print("Balance:",self.balance)
############################################################################################################
    def WithdrawMoney(self,amount):
        if(int(self.balance) - amount < 0):
            print("You do not have enough balance.")
        else:
            oldbalance = self.balance
            self.balance -= amount
            print("Old Balance:",oldbalance)
            print("New Balance:",self.balance)
            updatefile3 = open("Accounts.txt","r")
            meter1 = 0
            self.list.clear()
            for meter in updatefile3:
                self.list.append(meter)
                meter1 += 1
            updatefile3.close()
            updatefile2 = open("Accounts.txt","w")
            updatefile2.write("")
            updatefile2.close()
            listline = "{};{};{};{}".format(self.name,self.password,self.number,self.balance) 
            del self.list[self.degisken-1]
            self.list.append(listline)
            updatefile = open("Accounts.txt","a")
            num = 0
            while num < meter1:
                if num != meter1 - 1:
                    updatefile.writelines("{}".format(self.list[num]))
                elif num == meter1 -1:
                    updatefile.writelines("{}\n".format(self.list[num]))
                num += 1
            updatefile.close()
############################################################################################################
    def AddMoney(self,amount):
        oldbalance = self.balance
        self.balance += amount
        print("Old Balance:",oldbalance)
        print("New Balance:",self.balance)
        updatefile3 = open("Accounts.txt","r")
        meter1 = 0
        self.list.clear()
        for meter in updatefile3:
            self.list.append(meter)
            meter1 += 1
        updatefile3.close()
        updatefile2 = open("Accounts.txt","w")
        updatefile2.write("")
        updatefile2.close()
        listline = "{};{};{};{}".format(self.name,self.password,self.number,self.balance) 
        del self.list[self.degisken-1]
        self.list.append(listline)
        updatefile = open("Accounts.txt","a")
        num = 0
        while num < meter1:
            if num != meter1 - 1:
                updatefile.writelines("{}".format(self.list[num]))
            elif num == meter1 -1:
                updatefile.writelines("{}\n".format(self.list[num]))
            num += 1
        updatefile.close()
############################################################################################################        
    def ChangeInformation(self,newname,newpassword,newnumber):
        updatefile2 = open("Accounts.txt","r")
        result = False
        for linefor2 in updatefile2:
            namecheck = linefor2.split(";")
            check = namecheck[0]
            if newname == check:
                result = True
                break
        updatefile2.close()
        if result == False:
            verification = input("Your information will be changed, are you sure? Y/N: ")
            if(verification.lower() == "y"):
                self.name = newname
                self.password = newpassword
                self.number = newnumber
                print("Your Information Has Been Changed:")
                account.AccountInfo()
            elif(verification.lower() == "n"):
                print("Transaction canceled:")
                account.AccountInfo()     
            updatefile3 = open("Accounts.txt","r")
            meter1 = 0
            self.list.clear()
            for meter in updatefile3:
                self.list.append(meter)
                meter1 += 1
            updatefile3.close()
            updatefile2 = open("Accounts.txt","w")
            updatefile2.write("")
            updatefile2.close()
            listline = "{};{};{};{}".format(self.name,self.password,self.number,self.balance) 
            del self.list[self.degisken-1]
            self.list.append(listline)
            updatefile = open("Accounts.txt","a")
            num = 0
            while num < meter1:
                if num != meter1 - 1:
                    updatefile.writelines("{}".format(self.list[num]))
                elif num == meter1 -1:
                    updatefile.writelines("{}\n".format(self.list[num]))
                num += 1
            updatefile.close()
        elif result == True:
            print("Please enter a different username...")
############################################################################################################
name = input("Username: ")    
password = input("Password: ")
account = Account(name,None,None,password)
account.Login()
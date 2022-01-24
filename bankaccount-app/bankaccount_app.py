print("----------------------------------------------")
print("Welcome to the Bank:")
print("----------------------------------------------")
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
            print("----------------------------------------------")
            print("We couldn't find your account...")
            question = input("Would you like to create an account? Y/N: ")
            print("----------------------------------------------")
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
                    print("----------------------------------------------")
                    print("Your account has been created. You can login.")
                    print("----------------------------------------------")
                elif result == True:
                    print("----------------------------------------------")
                    print("Please enter a different username...")
                    print("----------------------------------------------")
            elif question.upper() == "N":
                print("Okay, Goodbye!")
                print("----------------------------------------------")
        elif(login == True):
            print("----------------------------------------------")
            print("Login successful...")
            account.Menu()
    def Menu(self):
        print("----------------------------------------------")
        select = int(input("Select an Action:\nPress 1 to account information\nPress 2 to withdraw money\nPress 3 to add money\nPress 4 to change your information\nPress 5 to Exit\nPress: "))
        if select == 1:
            account.AccountInfo()
        elif select == 2:
            print("----------------------------------------------")
            amount = int(input("Amount to be withdrawn: "))
            account.WithdrawMoney(amount)
        elif select == 3:
            print("----------------------------------------------")
            amount = int(input("Amount to add: "))
            account.AddMoney(amount)
        elif select == 4:
            print("----------------------------------------------")
            newname = input("New Name: ")
            newpassword = input("New Password: ")
            newnumber = input("New Number: ")
            account.ChangeInformation(newname,newpassword,newnumber)
        elif select == 5:
            print("----------------------------------------------")
            print("Goodbye!")
            print("----------------------------------------------")
            exit()

############################################################################################################
    def AccountInfo(self):
        print("----------------------------------------------")
        print("Name:",self.name)
        print("Number:",self.number)
        print("Balance:",self.balance)
        print("----------------------------------------------")
        backmenu = input("Press 1 to return to the menu\nPress 2 to exit\nPress: ")
        if backmenu == "1":
            account.Menu()
        else:
            print("----------------------------------------------")
            print("Goodbye!")
            print("----------------------------------------------")
            exit()
############################################################################################################
    def WithdrawMoney(self,amount):
        if(int(self.balance) - amount < 0):
            print("You do not have enough balance.")
            backmenu = input("Press 1 to Go to the menu\nPress 2 to exit\nPress: ")
            if backmenu == "1":
                account.Menu()
            else:
                print("----------------------------------------------")
                print("Goodbye!")
                print("----------------------------------------------")
                exit()
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
            print("----------------------------------------------")
            backmenu = input("Press 1 to Go to the menu\nPress 2 to exit\nPress: ")
            if backmenu == "1":
                account.Menu()
            else:
                print("----------------------------------------------")
                print("Goodbye!")
                print("----------------------------------------------")
                exit()
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
        print("----------------------------------------------")
        backmenu = input("Press 1 to return to the menu\nPress 2 to exit\nPress: ")
        if backmenu == "1":
            account.Menu()
        elif backmenu == "2":
            print("----------------------------------------------")
            print("Goodbye!")
            print("----------------------------------------------")
            exit()
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
            verification = input("Your information will be changed, are you sure? Yes/No: ")
            if(verification.lower() == "yes"):
                self.name = newname
                self.password = newpassword
                self.number = newnumber
                print("Your Information Has Been Changed:")
                account.AccountInfo()
            elif(verification.lower() == "no"):
                print("----------------------------------------------")
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
            print("----------------------------------------------")
            print("Please enter a different username...")
            print("----------------------------------------------")
        backmenu = input("Press 1 to return to the menu\nPress 2 to exit\nPress: ")
        if backmenu == "1":
            account.Menu()
        else:
            print("----------------------------------------------")
            print("Goodbye!")
            print("----------------------------------------------")
            exit()
############################################################################################################
name = input("Username: ")    
password = input("Password: ")
account = Account(name,None,None,password)
account.Login()
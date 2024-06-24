from abc import abstractmethod
import random
import time

class Bank:
    bank_name = "State Bank Of India"
    @abstractmethod
    def details(self,username,Adharcard,pancard,mobilenumber):
        pass

class people(Bank):
    def details(self, username,Adharcard,pancard,mobilenumber):
        print(username) 
        print(Adharcard)  
        print(pancard)
        print(mobilenumber)

print("Bank is",Bank.bank_name)
Bank.bank_name        
k= people()
a = input("Enetr your username:")
b = input("Enetr your adharcard:")
c = input("Enetr your pancard:")
d = input("Enetr your mobile:")
otp = random.randint(1000,9999)
time.sleep(3)
print("otp is",otp)
time.sleep(3)
print("your verification is succesfull")
account_number = random.randint(1000000,999999999)
time.sleep(3)
print("Your Account number has been create",account_number)
k.details(a,b,c,d)


class ATM(Bank):
    def __init__(self,avalabelbalance,pin_number,ac):
        self.account_number = ac
        self.pin_number = pin_number  
        self.avalabelbalance = avalabelbalance
            
    def Deposte(self,Ac,amount):
        if(self.account_number == Ac):
            self.avalabelbalance += amount
            print("your",amount,"succesfully deposite your balance is",self.avalabelbalance)    
        else:
            print("your Account number is wrong")
    
    # def withdrawl(self,Ac,pin,amount):
    def withdrawl(self,Ac,pin,amount):
         if(self.account_number == Ac):
            if(self.pin_number==pin):
                if(amount>self.avalabelbalance):
                    print("insafficiant balance")
                else:
                    self.avalabelbalance -= amount
                    print("your",amount,"succesfully withdrawl your balance is",self.avalabelbalance)
            else:
                print("pin_number is not correct")    
         else:
            print("your Account number is wrong")    


    def balance_check(self,Ac,pin):
         if(self.account_number == Ac):
            if(self.pin_number==pin):
                print(" your Total balance is",self.avalabelbalance)
            else:
                print("pin_number is not correct")    
         else:
            print("your Account number is wrong")



pin_number = input("create your pin number:")
f = ATM(0,pin_number,account_number)
ATM.bank_name
print("Correct Ac number",f.account_number)


print("click 1 for deposit")
print("click 2 for withdrawl")
print("click 3 for checkbalance")
print("click 4 for Exit")
while(True):
    x = int(input("Enter for:"))
    if(x==1):
        Ac= int(input("Enetr Ac number:"))
        b = int(input("Enter amount:"))
        f.Deposte(Ac,b)
        continue

    elif(x==2):
        Ac= int(input("Enetr Ac number:"))
        b = (input("Enter pass:"))
        c = int(input("Enter amount:"))
        f.withdrawl(Ac,b,c)
        continue

    elif(x==3):
         Ac= int(input("Enetr Ac number:"))
         b = input("Enter pin:")
         f.balance_check(Ac,b)
         continue
        

    elif(x==4):
        print("Thank You")
        break

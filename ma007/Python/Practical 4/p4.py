class Account:
    intrest_rate=7;

    def __init__(self,ac_no,ac_name,balance):
        self.ac_no=ac_no;
        self.ac_name=ac_name;
        self.balance=balance;
        
    def set(self):
        ac_no=int(input("enter account no : "))
        ac_name = input("enter account name : ")
        balance = int(input("Enter balance : "))
    def deposit(self):
        dep = int(input("enter deposit amount : "))
        tot_balance  = self.balance+dep;
        print("Total Balance : ",tot_balance)
    def withdraw(self):
        withdr=int(input("Enter withdrwal amount : "))
        after_with_bal = self.balance - withdr;
        print("After withdraw balance : ",after_with_bal)
    def calc_interest(self):
        yr = int(input("Enter years for intrest : "))
        inst = (self.balance*Account.intrest_rate*yr)//100;
        print("Intrest is : ",inst)
    def show(self):
        print("Account no is : ",self.ac_no)
        print("Account name : ",self.ac_name)
        print("Balance : ",self.balance)
        

a1 = Account(456,"vidhi",50000)
a1.show();
a1.deposit();
a1.withdraw();
a1.calc_interest();


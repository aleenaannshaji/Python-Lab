class Bank:
    def __init__(self,acc_no,name,type_acc,bal):
        self.acc_no=acc_no
        self.name=name
        self.type_acc=type_acc
        self.bal=0

    def showamnt(self):
        print("Account holder name: ",self.name)
        print("Account number: ", self.acc_no)
        print("Account type: ", self.type_acc)
        print("Balance amount: ", self.bal)

    def deposit(self,d1):
        self.bal=self.bal+d1
        return self.bal

    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal

n=input("Enter your name: ")
a=int(input("Enter your account number: "))
t=input("Enter your account type: ")
d=0
o=Bank(a,n,t,bal=0)
o.showamnt()

while(True):
    print("\nMenu")
    print("\n1. Deposit ")
    print("\n2. Withdraw ")
    c=int(input("Enter your choice: "))
    if(c==1):
        d=int(input("Enter the amount to deposit: "))
        print("Your total balance is: ", o.deposit(d))
    elif(c==2):
        w=int(input("Enter the amount to be withdrawn: "))
        if(w>d):
            print("Insufficient balance")
        else:
            print("Your total balance amount is: ",o.withd(w))
    else:
        print("Enter a valid choice")
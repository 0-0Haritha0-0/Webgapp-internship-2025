class bank:
    def cal(self,bal,withdraw,name,rollno):
        self.bal=bal
        self.withdraw=withdraw
        self.rollno=rollno
        self.name=name
        self.newbal=self.bal-self.withdraw
        if(self.newbal<0):
            print("Bal :",self.bal)
            print("Withdraw amount exceeding the limit")
        else:
            print("\n")
            print("ACCOUNT DETAILS :")
            print("\n")
            print("Employee no :",self.rollno)
            print("Name :",self.name)
            print("Balance :",self.bal)
            print("Withdraw amt :",self.withdraw)
            print("New balance after withdrawing :",self.newbal)
    def acc(self,rollno,withdraw,name):
        self.name=name
        self.withdraw=withdraw
        self.rollno=rollno
        if(self.rollno==1):
            self.bal=5000
            self.cal(self.bal,self.withdraw,self.name,self.rollno)
        elif(self.rollno==2):
            self.bal=300
            self.cal(self.bal,self.withdraw,self.name,self.rollno)
        elif(self.rollno==3):
            self.bal=10000
            self.cal(self.bal,self.withdraw,self.name,self.rollno)
        elif(self.rollno==4):
            self.bal=10
            self.cal(self.bal,self.withdraw,self.name,self.rollno)
        elif(self.rollno==5):
            self.bal=9875
            self.cal(self.bal,self.withdraw,self.name,self.rollno)
        else: 
            print("Incorrect account number")
    def num(self,no,name,withdraw):
        self.no=no
        self.name=name
        self.withdraw=withdraw
        if(no==1234567890):
            self.no=1
            self.acc(self.no,self.withdraw,self.name)
        elif(no==2345678901):
            self.no=2
            self.acc(self.no,self.withdraw,self.name)
        elif(no==3456789012):
            self.no=3
            self.acc(self.no,self.withdraw,self.name)
        elif(no==4567890123):
            self.no=4
            self.acc(self.no,self.withdraw,self.name)
        elif(no==5678901234):
            self.no=5
            self.acc(self.no,self.withdraw,self.name)
        else:
            self.no=6
            self.acc(self.no,self.withdraw,self.name)
b=bank()
b.num(int(input("Enter acc no : ")),input("Enter name : "),int(input("enter withdraw amt : ")))
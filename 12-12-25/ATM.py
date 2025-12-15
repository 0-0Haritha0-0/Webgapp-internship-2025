print("Account number:")
print("ENTER 1 for 1234567890\nENTER 2 for 2345678901\nENTER 3 for 0123456789")
acc=int(input())
if(acc==1): 
    balance=4500
    print("Balance:",balance)
    withdraw=int(input("Enter amt to be withdrawed:"))
    if(withdraw<=balance): 
        balance=balance-withdraw
        print("New balance:",balance)
    else: print("Insufficient balance")
elif(acc==2):
    balance=50000
    print("Balance:",balance)
    withdraw=int(input("Enter amt to be withdrawed:"))
    if(withdraw<=balance): 
        balance=balance-withdraw
        print("New balance:",balance)
    else: print("Insufficient balance")
elif(acc==3):
    balance=147
    print("Balance:",balance)
    withdraw=int(input("Enter amt to be withdrawed:"))
    if(withdraw<=balance): 
        balance=balance-withdraw
        print("New balance:",balance)
    else: print("Insufficient balance")
else: print("Account does not exist")
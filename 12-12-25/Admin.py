username="Haritha"
password="lifesuck"
name=input("Enter username:")
if(name==username): 
    p=input("Enter password:")
    if(p==password): print("Logged successfully")
    else: print("Error: Incorrect password")
else: print("Error: User doesn't exist")
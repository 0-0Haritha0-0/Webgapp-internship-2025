num=input("Enter odd or even : ")
end=int(input("Enter ending number = "))
if(num=='ODD' or num=='Odd' or num=='odd'):
    for i in range(1,end):
        print(i,end=" ")
        i+=2
elif(num=='EVEN' or num=='Even' or num=='even'):
    for i in range(2,end):
        print(i,end=" ")
        i+=2
else:
    print("Invalid input")
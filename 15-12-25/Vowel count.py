string=input("Enter string:")
count=0
for i in string:
    if(i=='a' or i=='A' or i=='E' or i=='e' or i=='i' or i=='I' or i =='o' or i=='O' or i=='u' or i=='U'):
        count+=1
print("Number of vowels = ",count)
const=len(string)-count
print("Number of consonents = ",const)
list=[2,2,3,4,5,6,5,1]
print("list",list)
# d=set(list)
# print(d)
a=[]
for i in list:
    if(i in a):
        print()
    else:
        a.append(i)
print("list without duplicates",a)

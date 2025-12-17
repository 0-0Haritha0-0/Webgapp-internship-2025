a=[2,34,75,8,19]
high=a[0]
low=a[0]
for i in range(1,len(a)):
    if(high<a[i]):
        high=a[i]
for i in range(1,len(a)):
    if(low>a[i]):
        high=a[i]
print(high,"is the highest")
print(low,"is the lowest")
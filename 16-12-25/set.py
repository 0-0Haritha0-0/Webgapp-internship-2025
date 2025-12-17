a={1,2,3}
b={2,3,4}
c=a&b #c=a.intersection(b)
d=a|b #d=a.union(b)
e=a^b #e=a.symmetric_difference(b)
f=a-b #f=a.difference(b)
print("Intersection =",c)
print("union =",d)
print("symmetric difference =",e)
print("difference =",f)
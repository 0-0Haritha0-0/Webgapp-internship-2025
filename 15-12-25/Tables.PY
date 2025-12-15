def tables(a,b):
    return(a*b)
b=int(input("Multiplication table of = "))
for i in range(1,10):
    print(i,"*",b,"=",tables(i,b))
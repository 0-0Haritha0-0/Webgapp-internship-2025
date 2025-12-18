# class student:
#     def name(self,name):
#         self.name=name
#         print("I am",self.name)
# s1=student()
# print(s1.name('Haritha'))



# class shape:
#     def circle(self,radius):
#         self.r=radius
#         print(2*22/7*self.r)
#     def rectangle(self,l,b):
#         self.l=l
#         self.b=b
#         return(l*b)
# c=shape()
# print(c.circle(7/22))
# print(c.rectangle(2,3))



class student:
    def info(self,name,depart):
        self.name=name
        self.depart=depart
        print("NAME :",self.name,";","DEPARTMENT :",self.depart)
s=student()
s.info("HARITHA","CSE")
s.info("PARKAVE","ECE")
s.info("BAVISHYA","ORTHO")


# class animals:
#     def dog(self,name,age,breed):
#         self.name=name
#         self.age=age
#         self.breed=breed
#         print("DOG:")
#         print("dog's name :",self.name)
#         print("dog's age :",age)
#         print("dog's breed :",self.breed )
#     def cow(self,name,kids,color):
#         self.name=name
#         self.kids=kids
#         self.color=color
#         print("COW:")
#         print("cow's name :",self.name)
#         print("cow's kids count :",self.kids)
#         print("cow's color :",self.color)
#     def cat(self,name,color,nails):
#         self.name=name
#         self.color=color
#         self.nails=nails
#         print("CAT:")
#         print("cat's name :",self.name)
#         print("cat's color :",self.color)
#         print("cat's nails strength :",self.nails)
# a=animals()
# print(a.dog('charlie',2,'golden puff'))
# # c=a.cow("lakshmi",2,"black")
# # d=a.cat("izzie",'brown','weak')
# # print("DOG:\n",a,"\nCOW:\n",b,"\nCAT:\n",c)
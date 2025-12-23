class offname():
    def __init__(self,officename):
        self.officename=officename
    def name(self):
        print("Office name :",self.officename)
class cmpname(offname):
    def name(self):
        print("Company name : ",self.officename)
class buildingname(cmpname):
    def name(self):
        print("Building name : ",self.officename)

# method 1
# obj=buildingname("google"),cmpname("microsoft"),offname("apple")
# for obj in obj:
#     obj.name()

# method 2
obj1=buildingname("google")
obj2=cmpname("microsoft")
obj3=offname("apple")
obj1.name()
obj2.name()
obj3.name()
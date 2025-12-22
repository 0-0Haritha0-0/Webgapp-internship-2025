class CEO:
    salaryceo=1000000
    def earning(self):
        print("MONTHLY EARNINGS OF CEO :",self.salaryceo)

class manager(CEO):
    salarymanager = CEO.salaryceo/4
    def salary(self):
        print("MONTHLY EARNINGS OF MANAGER :",self.salarymanager)
class tl(manager):
    def money(self):
        self.salarytl=self.salarymanager/3
        print("MONTHLY EARNINGS OF TL :",self.salarytl)
class employee(tl):
    def cash(self):
        self.salaryemployee=self.salarytl/2
        print("MONTHLY EARNINGS OF EMPLOYEE :",self.salaryemployee)

obj=employee()
obj.earning()
obj.salary()
obj.money()
obj.cash()
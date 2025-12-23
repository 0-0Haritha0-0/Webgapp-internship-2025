class CEO:
    def __init__(self):
        self.__salaryceo=1000000
    def earning(self):
        print("MONTHLY EARNINGS OF CEO :",self.__salaryceo)
    def senderceo(self):
        return self.__salaryceo

class manager(CEO):
    def getter(self):
        self.__salarymanager=self.senderceo()/4
    def salary(self):
        print("MONTHLY EARNINGS OF MANAGER :",self.__salarymanager)
    def sendermanager(self):
        return self.__salarymanager
class tl(manager):
    def money(self):
        self.__salarytl=self.sendermanager()/3
        print("MONTHLY EARNINGS OF TL :",self.__salarytl)
    def sendertl(self):
        return self.__salarytl
class employee(tl):
    def cash(self):
        self.__salaryemployee=self.sendertl()/2
        print("MONTHLY EARNINGS OF EMPLOYEE :",self.__salaryemployee)

obj=employee()
obj.earning()
obj.getter()
obj.salary()
obj.money()
obj.cash()
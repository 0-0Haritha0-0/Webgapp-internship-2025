#  single
class Parent():
    def one(self):
        print("1")

class Child(Parent):
    def two(self):
        print("2")

obj=Child()
obj.one()
obj.two()


# mulitiple

class mom():
    def mother(self):
        print("MOM")
class dad():
    def father(self):
        print("DAD")
class child(mom,dad):
    def children(self):
        print("CHILD")

obj=child()
obj.mother()
obj.father()
obj.children()


# multilevel

class grandmother():
    def granny(self):
        print("mother to mother")
class mother(grandmother):
    def mommy(self):
        print("mother")
class child(mother):
    def kid(self):
        print("kid")

obj=child()
obj.granny()
obj.mommy()
obj.kid()

# hierarchical

class property():
    def p(self):
        print("properties :")
class land(property):
    def l(self):
        print("Propert of land")
class house(property):
    def h(self):
        print("Property house")

obj2=house()
obj1=land()
obj1.p()
obj1.l()
obj1.p()
obj2.h()

# hybrid

class head():
    def leader(self):
        print("head")
class body(head):
    def middle(self):
        print("body")
class end(head):
    def footer(self):
        print("end")
class ending(body,end):
    def climax(self):
        print("ending")
class everything(ending):
    def all(self):
        print("everything")

obj=everything()
obj.leader()
obj.middle()
obj.footer()
obj.climax()
obj.all()


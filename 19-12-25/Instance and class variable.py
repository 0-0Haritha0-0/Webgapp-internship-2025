class eat:
    fruit="apple"
    def __init__ (self,vegtable,snacks,ricee):
        self.vegtable=vegtable
        self.snacks=snacks
        self.ricee=ricee
    def veg(self):
        print("I eat", self.vegtable,"for vegetables")
    def snack(self):
        print("I eat", self.snacks,"for snack")
    def rice(self):
        print("I eat", self.ricee,"for rice")
me=eat("potato","chips","curd")
me.veg()
me.snack()
me.rice()
print("I eat",me.fruit,"for fruit")
you=eat("brinjal","fries","lemon")
you.veg()
you.snack()
you.rice()
print("I eat",you.fruit,"for fruit")
opp=eat("greens","cake","briyani")
opp.fruit="Mango"
opp.veg()
opp.snack()
opp.rice()
print("I eat",opp.fruit,"for fruit")
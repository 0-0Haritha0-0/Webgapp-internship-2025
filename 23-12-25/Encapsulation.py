class offname():
    def __init__(self,officename):
        self.__officename=officename
    def name(self):
        print("Office name :",self.__officename)
obj=offname("soft")
obj.name()


# class office():
#     def __init__(self, name):
#         self.__office = name
#     def show(self):
#         print(self.__office)
# obj = office("webgapp")
# obj.show()
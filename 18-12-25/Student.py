class stdu:
    def __init__(self,no,name,dep,email,clgname,year):
        self.name=name
        self.no=no
        self.dep=dep
        self.email=email
        self.clgname=clgname
        self.year=year
    def info(self):
        print("Student",self.no)
        print("\n")
        print("NAME :",self.name)
        print("EMAIL :",self.email)
        print("COLLAGE :",self.clgname)
        print("DEPARTMENT :",self.dep)
        print("YEAR :",self.year)
        print("\n\n")
s1=stdu(1,"Hari","hari@gmail.com","SRM","EEE",1)

s2=stdu(2,"Haritha","haritha@gmail.com","SRMIST","CSE",1)

s3=stdu(3,"Rita","rita@gmail.com","ANNA UNI","MBA",1)

s4=stdu(4,"Rithu","rithu@gmail.com","SRMIST","CSE",1)

s5=stdu(5,"Bavishya","bavishya@gmail.com","ULTRA","ORTHO",1)

s6=stdu(6,"Parkave","parkave@gmail.com","SIT","ECE",1)

s7=stdu(7,"Dhivya","dhivya@gmail.com","RMC","HEALTH",1)

s8=stdu(8,"Akshaya","akshaya@gmail.com","ETHRAJ","CS",1)

s9=stdu(9,"Nevey","nevey@gmail.com","SRMIST","EEE",1)

s10=stdu(10,"Priya","priya@gmail.com","TIT","CS",1)
s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()
s7.info()
s8.info()
s9.info()
s10.info()

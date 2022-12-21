#Composition ربط الكلاسات
class Address:
    def __init__(self,country,city,area, street,house,long,lat):
        self.country = country
        self.city = city
        self.area = area
        self.street = street
        self.house = house
        self.long = long
        self.lat = lat
    def display(self):
        print(self.city,self.country)

class Employee:
    def __init__(self,name,age,phone,salary,country,city,area, street,house,long,lat):
        self.name = name
        self.age = age
        self.phone = phone
        self.salary = salary
        self.address = Address(country,city,area, street,house,long,lat)
    def display(self):
        print(self.name,self.age,self.phone,self.salary)
        self.address.display()

class Clint:
    def __init__(self,name,age,phone,email,country,city,area, street,house,long,lat):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.address = Address(country,city,area, street,house,long,lat)
    def display(self):
        print(self.name,self.age,self.phone,self.email)
        self.address.display()

ali = Clint('Ali',22,'00775588','ali@gml.cb','iraq','baghdad','kargh',20,30,40,50)
ali.display()
x = Employee('mujtaba',24,'07844544',1000,'iraq','baghdad','kargh',20,30,40,50)
x.display()

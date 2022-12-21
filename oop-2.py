class Studint:
    def __init__(x , name ,age ,level):#__init__ dunder method بناء للدالة
        x.name = name
        x.age = age
        x.level = level

    def display(x):
        print(x.name,x.age,x.level)

ali = Studint("ali", 22,3)
ali.display()
mujtaba = Studint("mujtaba",24,10)
mujtaba.display()


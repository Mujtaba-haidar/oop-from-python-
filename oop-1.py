# class student:
 
#     def read(self):
#         self.name = input('Enter Name:')
#         self.age = input('Enter Age:')
#         self.level = input('Enter Level:')
    
#     def disply(self):
#         print(self.name,self.age , self.level )

# x = student()
# x.read()
# x.disply()

class Setudent:
    stud = []
    def __init__(self, name,age,level):
        self.name = name
        self.age = age
        self.level = level
        Setudent.stud.append(self)
    def disply(self):
        print(self.name,self.age,self.level)

sutd1 = Setudent('Ahmed',25,6)
sutd2 = Setudent('ali',20,5)
sutd3 = Setudent('nor',19,1)
sutd4 = Setudent('Ahmed',25,6)
sutd5 = Setudent('ali',20,5)
sutd6 = Setudent('nor',19,1)

for e in Setudent.stud:
    e.disply()


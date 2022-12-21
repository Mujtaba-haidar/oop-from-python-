# class Stundent:
#     def __init__(self,*args , **kwargs):
#         self.marks = args
#         self.data = kwargs

#     def display(self):
#         print(self.marks,self.data['name'],self.data['age'])

# ali = Stundent(50,60,70,80,90,name='MUJTABA' ,add='bag', age =24)
# ali.display()

#Encapsolation
class student:
 
    def __init__(self,name,age,level):
        self.__name = name
        self.__age = age
        self.__level = level

    
    def disply(self):
        print(self.__name,self.__age , self.__level )

      #(settings & Gettings)
    def set_name(self,name):
        self.__name = name
    
    def get_name(self):
        return self.__name

x = student('ali', 22 ,5)
x.disply()

x.set_name('mujtaba')
x.disply()

n= x.get_name()
print(n)



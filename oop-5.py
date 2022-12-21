# # # classAttribut classMethods

# # class Employee:
# #     bonus = 200
# #     total = 0
# #     emps = []
# #     def __init__(self, **kwargs):
# #         self.__data = kwargs
# #         Employee.total += 1
# #         Employee.emps.append(self)
# #     def display (self):
# #         print(self.__data['name'] ,self.__data['salary'])

# #     def give_bonus(self):
# #         self.__data['salary'] += Employee.bonus
        
# #     @classmethod
# #     def chang_bon(cls, new_bon):
# #         cls.bonus = new_bon


# # emp1=Employee(name = 'mujtaba' , age =24, salary =1000 ,address = 'baghdad')
# # emp2=Employee(name = 'ali' , age =27, salary =800 ,address = 'basra')
# # emp3=Employee(name = 'nor' , age =33, salary =600 ,address = 'najf')
# # emp4=Employee(name = 'ban' , age =52, salary =500 ,address = 'mousl')
# # emp5=Employee(name = 'jin' , age =30, salary =700 ,address = 'baghdad')

# # Employee.chang_bon(250)#classmethod
# # print(Employee.total)
# # for e in Employee.emps:
# #     e.give_bonus()
# #     e.display()

class Employee:
    bound = 200
    total = 0
    empl = []
    def __init__(self,**kwargs):
        self.__data = kwargs
        Employee.total += 1
        Employee.empl.append(self)
    def display(self):
        print(self.__data['name'],self.__data['salary'])

    def give_bound(self):
        self.__data['salary'] += Employee.bound

emp1=Employee(name = 'mujtaba' , age =24, salary =1000 ,address = 'baghdad')
emp2=Employee(name = 'ali' , age =27, salary =800 ,address = 'basra')
emp3=Employee(name = 'nor' , age =33, salary =600 ,address = 'najf')
emp4=Employee(name = 'ban' , age =52, salary =500 ,address = 'mousl')
emp5=Employee(name = 'jin' , age =30, salary =700 ,address = 'baghdad')

#print( str(Employee.total) + ':' )
print(f": {Employee.total}")
for e in Employee.empl:
    e.give_bound()
    e.display()

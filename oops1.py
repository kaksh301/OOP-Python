# initiate class
class employee:
    
    __user_id = 1
    
    # special func/method / dunder method    -> constructor
    def __init__(self):
        self.__name = "Default User"   # hiding using __
        self.id = employee.__user_id
        self.salary = 50000
        self.designation = "SDE"
        
    # getter id using static method
    @staticmethod
    def get_id():
        return employee.__user_id
    
    # setter id using static method
    @staticmethod
    def set_id(value):
        employee.__user_id = value
        
        
    def getvalue(self):   # getter setter 
        return self.__name
    
    def setvalue(self, value): # getter setter
        self.__name = value
        
    def travel(self,destination):
        print(f"Employess is now travelling to {destination}")
             
e1 = employee()
print(e1.id)
print(e1.salary)
print(e1.designation)

# print(e1.__name)   this will not show name 
print(e1._employee__name)   # this will give name -> using this we can access

e1.travel("mumbai")
print(type(e1))


print("-----"*50)

print(e1.getvalue()) 
e1.setvalue("Agent")
print(e1.getvalue())




# using static method directly from class rather than object
emp = employee()
print(emp.id)
employee.set_id(10)
emp2 = employee()
print(emp2.id)


        
        
    
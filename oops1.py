# initiate class
class employee:
    # special func/method / dunder method    -> constructor
    def __init__(self):
        self.id = 123 
        self.salary = 50000
        self.designation = "SDE"
        
    def travel(self,destination):
        print(f"Employess is now travelling to {destination}")
             
e1 = employee()
print(e1.id)
print(e1.salary)
print(e1.designation)

e1.travel("mumbai")
print(type(e1))
        
        
    
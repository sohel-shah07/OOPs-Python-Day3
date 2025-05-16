#initializing class
class Employee():
    # special method or constructor
    def __init__(self):
        print("Started executing Attribute")
        self.Id = 123
        self.Salary = 50000
        self.designation = "SDE"
        print("Finished executing Attribute")
        
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is travelling to {destination}")
        
        
#creating object of class or instance of class
sam = Employee()
print(type(sam))
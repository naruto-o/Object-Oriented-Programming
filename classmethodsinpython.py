class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):     #it is a constructor
        self.name=aname
        self.role=arole
        self.salary=asalary
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}" 


    @classmethod   
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves



harry = Employee("Harry","$4500","instructor")
larry = Employee("Larry","$450","student")

print(harry.no_of_leaves)
harry.change_leaves(11)
print(harry.no_of_leaves)      # it changes the whole claasss variable
print(larry.no_of_leaves)    # yeh class decorator sirf instance variable ko change nhi krta puri class variable ko change krta h 
Employee.change_leaves(12)
print(harry.no_of_leaves)
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):     #it is a constructor
        self.name=aname
        self.role=arole
        self.salary=asalary
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"    
harry = Employee("Harry","$4500","instructor")
larry = Employee("Larry","$450","student")

# harry=Employee()
# larry=Employee()
                                                            #this is for prin t details function defined above
# harry.name="Harry
# larry.name="Laryy"

# harry.salary="$4500"
# larry.salary="$450"

# harry.role="instructor"
# larry.role="student"

# print(harry.printdetails())
# print(larry.printdetails())
print(harry.salary)
print(larry.role)
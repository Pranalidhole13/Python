class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print(self.role,self.dept,self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",50000)

e1=Employee("Accountant","Finance",60000)
e1.showDetails()

e2=Engineer("Pranali",22)
e2.showDetails()


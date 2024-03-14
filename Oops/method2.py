class Student:
    def __init__(self,name,phy,che,math):
        self.name=name
        self.phy=phy
        self.che=che
        self.math=math

    def Average(self):
        add=self.phy+self.che+self.math
        print("Average is :",add/3)

s1=Student("Pranali",90,91,92)
print(s1.name, s1.phy, s1.che, s1.math)
s1.Average()
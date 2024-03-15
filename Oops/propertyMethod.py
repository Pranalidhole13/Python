class Student:
    def __init__(self,phy,che,math):
        self.phy=phy
        self.che=che
        self.math=math
        # self.Percentage=str((self.phy+self.che+self.math)/3)+"%"

    @property
    def Percentage(self):
        return str((self.phy+self.che+self.math)/3)+"%"

s1=Student(98,78,81)
print(s1.Percentage)
s1.phy=90
print(s1.Percentage)
        
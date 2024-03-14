# init function ==> always executed when class is being initiated

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Constructor")

s1=Student('Arjun',90)
print(s1.name,s1.marks)

s2=Student("Karan",98)
print(s2.name,s2.marks)
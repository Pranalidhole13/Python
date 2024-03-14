class Student:
    def __init__(self,name):
        self.name=name
        print("Init function")
    
    def Welcome(self):
        print("Hii")

s1=Student("Karan")
print(s1.name)
s1.Welcome()
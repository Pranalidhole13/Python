class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def Area(self):
        pi=3.14
        return pi*self.radius*self.radius

    def Perimeter(self):
        return 2*3.14*self.radius
c1=Circle(21)
print(c1.radius)
print(c1.Area())
print(c1.Perimeter())
import math
class Shape:
    def area(slef):
        raise NotImplementedError
class Rectangle(Shape):
      def __init__(self,length,width):
          self.lenght=length
          self.width=width
      def area(self):
           return self.lenght**2
class Circle(Shape):
    def __init__(self,radius):
         self.radius=radius
    def area(self):
            return math.pi*(self.radius*self.radius)


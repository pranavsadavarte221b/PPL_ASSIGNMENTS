from abc import ABC, abstractmethod

class Circle(object):
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius
class Polygon(ABC):
    def noofsides(self):
        pass

class RegularPolygon(object):
    pi = 3.14

    def __init__(self, side = 1):
        self.side = side

    def area(self):
        print("Area of object is")

    def perimeter(self):
        print("Permeter of object is")

    def setSide(self, side):
        self.side = side

    def getSide(self):
        return self.side

class Square(RegularPolygon, Polygon):
    def __init__(self, side = 1):
       RegularPolygon.__init__(self, side)

    def area(self):
        RegularPolygon.area(self)
        print(self.side ** 2)
        return self.side**2

    def perimeter(self):
        RegularPolygon.perimeter(self)
        print(self.side * 4)
        return self.side*4

    def setSide(self, side):
        RegularPolygon.setSide(self)

    def getSide(self):
        RegularPolygon.getSide(self)

    def noofsides(self):
        print("I have 4 sides")

class EquilateralTriangle(RegularPolygon, Polygon):
    def __init__(self, side = 1):
       RegularPolygon.__init__(self, side)

    def area(self):
        RegularPolygon.area(self)
        area = ((3**(1/2))/4) * self.side**2
        print(area)
        return area

    def perimeter(self):
        RegularPolygon.perimeter(self)
        print(self.side * 3)
        return self.side*3

    def setSide(self, side):
        RegularPolygon.setSide(self)

    def getSide(self):
        RegularPolygon.getSide(self)

    def noofsides(self):
        print("I have 3 sides")

class Rhombus(Square, Polygon):
    def __init__(self, diagonal1, diagonal2, side = 1):
        RegularPolygon.__init__(self, side)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        RegularPolygon.area(self)
        Area = 1/2 * self.diagonal1* self.diagonal2
        print(Area)
        return Area

    def perimeter(self):
        RegularPolygon.perimeter(self)
        print(self.side * 4)
        return self.side*4

    def set(self, side, diagonal1, diagonal2):
        RegularPolygon.setSide(self)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2


    def get(self):
        RegularPolygon.getSide(self)
        return  self.diagonal1
        return  self.diagonal2

    def noofsides(self):
        print("I have 4 sides")


class Rectangle( Polygon):
   def __init__(self, length = 1, breadth = 1):
        self.length = length
        self.breadth = breadth

   def area(self):
        Area = self.length * self.breadth
        print("Area of rectangle:", Area)
        return Area

   def perimeter(self):
        Perimeter = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle: ", Perimeter)
        return Perimeter

   def set(self, side, diagonal1, diagonal2):
        self.length = length
        self.breadth = breadth


   def get(self):
        return self.length
        return self.breadth

   def noofsides(self):
        print("I have 4 sides")

class Parallelogram( Polygon):
   def __init__(self, base = 1, heigth = 1, side = 1):
        self.base = base
        self.heigth = heigth
        self.side = side

   def area(self):
        Area = self.base * self.heigth
        print("Area of parallelogram:", Area)
        return Area

   def perimeter(self):
        Perimeter = 2 * (self.base + self.side)
        print("Perimeter of rectangle: ", Perimeter)
        return Perimeter
   def noofsides(self):
        print("I have 4 sides")

class IsoscelesTriangle(object):
   def __init__(self, side = 1, base = 1, height = 1):
        self.base = base
        self.heigth = heigth
        self.side = side

   def  area(self):
        Area = 1/2 * self.base * self.heigth
        print(Area)
        return Area

   def perimeter(self):
        Perimeter = 2*side + base
        print(Perimeter)
        return Perimeter

class ScaleneTriangle(IsoscelesTriangle):
   def __init__(self, side1 = 1,side2 = 1, base = 1, height = 1):
        self.base = base
        self.heigth = heigth
        self.side1 = side1
        self.side2 = side2

   def  area(self):
        IsoscelesTriangle.area(self)

   def perimeter(self):
        Perimeter = side1 + side2 + base
        print(Perimeter)
        return Perimeter

S = Square()
S.area()
S.perimeter()
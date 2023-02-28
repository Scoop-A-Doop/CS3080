'''
Homework 4 Exercise 1
Name: Suleyman Shouib
Date: 3/9/23
Description of your program: This program demonstrates OOP and Inheritence. There is a parent class named Shape and 3
                            other subclasses named Square, Circle and Rectangle. All 3 of the subclasses inherit from
                            super class Shape. Shape has methods that calculate area, diagonal/diameter and perimeters.
                            The rest of the program demonstrates each of these methods for each different subclass.
'''
import math

class Shape:

    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def calculateArea(self):
        if self.radius == 0 and self.width == 0:  # Square
            area = pow(self.length, 2)  # Square Area = Length^2
        elif self.radius == 0:  # Rectangle
            area = self.length * self.width     # Rectangle Area = Length * Width
        else:  # Circle
            area = 3.14 * (pow(self.radius, 2))     # Circle Area = pi*Radius^2
        return area

    def calculateDiagonalOrDiameter(self):
        if self.radius == 0 and self.width == 0:  # Square
            diagonal = math.sqrt(pow(self.length, 2) + pow(self.length, 2))     # Square Diagonal = sqrt(Length^2 + Length^2)
            return diagonal
        elif self.radius == 0:  # Rectangle
            diagonal = math.sqrt(pow(self.length, 2) + pow(self.width, 2))  # Rectangle Diagonal = sqrt(Length^2 + Width^2)
            return diagonal
        else:  # Circle
            diameter = self.radius * 2  # Diameter =Radius*2
            return diameter

    def calculatePerimeter(self):
        if self.radius == 0 and self.width == 0:  # Square
            perimeter = self.length * 4     # Square Perimeter = Length*4
        elif self.radius == 0:  # Rectangle
            perimeter = (2 * self.length) + (2 * self.width)    # Rectangle Perimeter = 2*Length + 2*Width
        else:  # Circle
            perimeter = 2*3.14*self.radius  # Circle Perimeter = 2*pi*Radius
        return perimeter


class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self, length, width, 0)


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, 0, 0, radius)


class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self, length, 0, 0)


print("Rectangle Of Length 10 and Width 5:")
myRectangle = Rectangle(10, 5)
print("Area: "+str(myRectangle.calculateArea()))
print("Diagonal: "+str(myRectangle.calculateDiagonalOrDiameter()))
print("Perimeter: "+str(myRectangle.calculatePerimeter()))

print("-----")

print("Circle Of Radius 5:")
myCircle = Circle(5)
print("Area: "+str(myCircle.calculateArea()))
print("Diagonal: "+str(myCircle.calculateDiagonalOrDiameter()))
print("Perimeter: "+str(myCircle.calculatePerimeter()))

print("-----")

print("Square Of Length 3:")
mySquare = Square(3)
print("Area: "+str(mySquare.calculateArea()))
print("Diagonal: "+str(mySquare.calculateDiagonalOrDiameter()))
print("Perimeter: "+str(mySquare.calculatePerimeter()))

print("-----")

print("Circle with a Radius that's half of the diagonal of a rectangle with a length of 20 and width of 10")
specialRectangle = Rectangle(20, 10)
specialCircle = Circle(specialRectangle.calculateDiagonalOrDiameter())
print("Perimeter: "+str(specialCircle.calculatePerimeter()))

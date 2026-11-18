#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:26:52 2019

@author: kkutten1
"""
import math
class Shape:
    def __init__(self):
        self.name = 'Shape'
    def display(self):
        print("I am a {}".format(self.name))

class Polygon(Shape):
    def __init__(self, sideLengths):
        Shape.__init__(self)
        self.name = "Polygon"
        self.sideLengths = sideLengths
        
    def getPerimeter(self):
        return sum(self.sideLengths)
    def display(self):
        Shape.display(self)
        print("I have {} sides.".format(len(self.sideLengths)))
        print("My perimeter is {}".format(self.getPerimeter()))

class RightTriangle(Polygon):
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.diagonal = math.sqrt(self.width**2 + self.height**2)
        sideLengths = [self.width, self.height, self.diagonal]
        Polygon.__init__(self, sideLengths)
        self.name = 'Right Triangle'
        
    def display(self):
        Polygon.display(self)
        print("My area is {}".format(self.getArea()))

    def getArea(self):
        return self.width*self.height / 2
    
class Rectangle(Polygon):
    def __init__(self, width, height):
        Polygon.__init__(self, [width, width, height, height])
        self.name = "Rectangle"
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height
    
    def display(self):
        Polygon.display(self)
        print("My area is", self.getArea())
        
class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.radius = radius
        self.name = "Circle"
    
    def getArea(self):
        return math.pi * (self.radius**2)
    
    def getCircumference(self):
        return 2 * math.pi * self.radius
    
    def display(self):
        Shape.display(self)
        print("My area is", self.getArea())
        print("My circumference is", self.getCircumference())
        
class Square(Rectangle):
    def __init__(self, width):
        Rectangle.__init__(self, width, width)
        self.name = "Square"
        
def main():
    C = Circle(2)
    C.display()
    print()
    T = RightTriangle(3,4)
    T.display()
    print()
    R = Rectangle(3,4)
    R.display()
    print()
    S = Square(2)
    S.display()

if __name__ == "__main__": main()

import math
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius    
    def getCenter(self):
        return self.center
    def getRadius(self):
        return self.radius
    def setCenter(self, center):
        self.center = center
    def setRadius(self, radius):
        self.radius = radius
    def getArea(self):
        return math.pi * (self.radius**2)
    def getCircumference(self):
        return 2 * math.pi * self.radius
    def isContained(self, other):
        if(other.getCenter().getX()+other.getRadius() < self.getCenter().getX()+self.getRadius() and other.getCenter().getX()-other.getRadius() > self.getCenter().getX()-self.getRadius()):
            return True
        else:
            return False
        
if __name__ == "__main__":
    centerX=int(input("Enter the x coordinate of the first center:\n"))
    centerY=int(input("Enter the y coordinate of the first center:\n"))
    radius = int(input("Enter the radius of the first circle:\n"))
    otherX=int(input("Enter the x coordinate of the first center:\n"))
    otherY=int(input("Enter the y coordinate of the first center:\n"))
    otherradius = int(input("Enter the radius of the first circle:\n"))
    p1 = Point(centerX,centerY)
    p2 = Point(otherX, otherY)
    Blob = Circle(p1, radius)
    Blib = Circle(p2, otherradius)
    print(Blob.getArea())
    print(Blob.getCircumference())
    print(Blob.isContained(Blib))
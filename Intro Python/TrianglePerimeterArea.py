import math
x1 = float(input("Enter x1\n"))
y1 = float(input("Enter y1\n"))
x2 = float(input("Enter x2\n"))
y2 = float(input("Enter y2\n"))
x3 = float(input("Enter x3\n"))
y3 = float(input("Enter y3\n"))
side1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
side2 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
side3 = math.sqrt((x2-x3)**2 + (y2-y3)**2)
perimeter = side1 + side2 + side3
print("The perimeter is", round(perimeter, 2))
d = perimeter / 2
area = math.sqrt(d * (d-side1) * (d-side2) * (d-side3))
print("The area is", round(area, 2))

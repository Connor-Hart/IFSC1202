from math import pi
radius = 0
R = "Radius"
D = "Diameter"
C = "Circumference"
A = "Area"

def diameter(n):
    diameter = radius*2
    return(float(diameter))
def circumference(n):
    circumference = radius*2*pi
    return(float(circumference))
def area(n):
    area = radius**2*pi
    return(float(area))

radiusfile = open("06.01 Radius.txt", "r")
x = radiusfile.readline()
print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius", "Diameter", "Circumference", "Area"))
while x != "":
    radius = float(x)
    a = float(diameter(radius))
    b = float(circumference(radius))
    c = float(area(radius))
    
    print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(radius, a, b, c))
    x = radiusfile.readline()

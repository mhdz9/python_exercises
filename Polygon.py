from math import tan, degrees, radians

sides = input("How many sides does the polygon have?\n")
size = input("What is the size of the sides?\n")
c_angle = 360/sides
dgs = radians(c_angle)

#try:
ap = size / (2 * tan(dgs / 2))
#except ZeroDivisionError:
    #ap = size

perimeter = sides * size
area = abs((perimeter*ap)/2)
print "The perimeter of the polygon is: ", perimeter, " and the area is: ", area
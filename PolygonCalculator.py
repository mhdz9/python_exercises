from math import tan, radians, degrees, sqrt

def square():
    size = int(raw_input("Enter the size of one of the sides"))
    perimeter = size * 4
    area = size * size
    print "The perimeter is: ",perimeter," and the area is: ",area

def rectangle():
    base = int(raw_input("Enter the size of the base"))
    height = int(raw_input("Enter the height"))
    perimeter = (base * 2) + (height * 2)
    area = base * height
    print "The perimeter is: ",perimeter," and the area is: ",area

def triangle():
    size1 = int(raw_input("Enter the size of side 1"))
    size2 = int(raw_input("Enter the size of side 2"))
    size3 = int(raw_input("Enter the size of side 3"))
    
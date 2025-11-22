import math

# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a, b, c):
    s = (a + b + c) / 2 
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# read from keyboard
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

print("The area of the triangle is:", triangle_area(a, b, c))

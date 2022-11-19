import math
# @return the square of a RIGHT triangle
def square_triangle(x, y):
     return x*y*0.5

# @return the square of rectangle
def square_rectangle(d, z, t):
     p = (z+t+d) / 2
     return math.sqrt(p*(p-z)*(p-t)*(p-d))

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
t = float(input("t = "))
d = math.sqrt(x*x+y*y) #diagonal length

print("Resualt = ", square_triangle(x,y) + square_rectangle(d,z,t))

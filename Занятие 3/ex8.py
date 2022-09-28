def checkEqual (x,y,z):
    if x == y == z:
        return 3
    elif (x == y and x != z) or (x == z and x != y) or (y == z and y != x) or (z == y and z!=x):
        return 2
    elif (x != y) and (y != z):
        return 0

a = int(input("Enter the first number to compare:"))
b = int(input("Enter the second number to compare:"))
c = int(input("Enter the third number to compare:"))

print(checkEqual(a,b,c))

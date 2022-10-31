def fun(x,y):
    i = 1
    while x < y:
        x *= 1.1
        i += 1
    return i

a = int(input())
b = int(input())

print(fun(a,b))





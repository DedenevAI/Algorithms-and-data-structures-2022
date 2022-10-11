def fun(x,y):
    if (x < y): 
        for i in range (x, y+1):
             print(i)
    elif ( x > y ):
        for i in range(x, y-1, -1):
            print(i)
    else:
         print("A equal B!")

a = int(input("A = "))
b = int(input("B = "))

print(fun(a,b))
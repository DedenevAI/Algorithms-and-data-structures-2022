def fun(x):
    a = 1
    b = 1
    while(x != 0):
        x1 = int(input())
        if x1 != 0 and x == x1:
            a += 1
        else:
            if a > b:
                b = a
            x = x1
            a = 1
    return b

n = int(input())
print(fun(n))
def fun(x):
    k = 0
    while(x != 0):
            x1 = int(input())
            if x1 != 0 and x < x1:
                k += 1
            x = x1
    return k

n = int(input())
print(fun(n))
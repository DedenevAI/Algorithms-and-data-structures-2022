def fun(x):
    k = 0
    while(x != 0):
        if (x > 0):
            x = int(input())
            k += 1
        else:
            return"The sequence can contain only positive values!"
    return k

n = int(input())
print(fun(n))
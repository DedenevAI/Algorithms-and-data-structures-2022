def fun(x):
    if(x > 0):
        N = x // 2
        i = 1
        k = 0 
        while(i <= N):
            i *= 2
            k += 1
        return i, k 
    else:
        return "Incorrect values!"

n = int(input())
print(fun(n))
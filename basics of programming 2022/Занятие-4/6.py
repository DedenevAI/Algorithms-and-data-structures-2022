def fun(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i
    return(fact)


n = int(input())
print(fun(n))


def fun(x):
    factSum = 0
    previous = 1
    for i in range(1,x+1):
        fact = previous * i
        factSum += fact
        previous = fact
    return(factSum)

n = int(input())
print(fun(n))


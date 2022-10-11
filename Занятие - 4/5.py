def fun(x):
    sum = 0
    for i in range(1,x+1):
        sum += i ** 3
    return(sum)

n = int(input())
print(fun(n))



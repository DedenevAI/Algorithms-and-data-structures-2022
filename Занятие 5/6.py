def fun(x):
    k = 0
    sum = 0
    while(x != 0):
            sum += x
            k += 1
            x = int(input())
    return (sum / k)

n = int(input())
print(fun(n))
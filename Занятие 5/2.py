def minDel(x):
    if (x > 1):
        i = 1
        while i <= x:
            i = i + 1
            if x % i == 0:
                return i
    else:
        return "Incorrect values!"

n = int(input())
print(minDel(n))

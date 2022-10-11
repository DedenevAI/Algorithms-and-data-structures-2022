def fun(x):
    f1 = 1
    f2 = 2
    print(f1)
    print(f2)
    for i in range(3,x+1):
        print(f1+f2)
        b = f1
        f1 = f2
        f2 = b+f1
    print()

n = int(input("Количество членов последовательности: "))
print(fun(n))

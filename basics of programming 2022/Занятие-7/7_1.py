def fun(n):
    x = []
    sum = 0;
    mult = 1;
    for i in range(n):
        print("Enter ", i, "element: ")
        x.append(int(input()))
        if ( i % 2 == 0):
            sum += x[i]
        else:
            mult *= x[i]
    return "Massive: " + str(x) +"\n Sum = " + str(sum) + "\n Mult = " + str(mult)

l = int(input("Enter length of massive: "))
print(fun(l))


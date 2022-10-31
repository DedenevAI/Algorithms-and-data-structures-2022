def fun(n):
    x = []
    res1, res2  = "", ""
    for i in range(n):
            print("Enter ", i, "element: ")
            x.append(int(input()))

    res1 = "Massive before sorting MAX and MIN:" + str(x)
    
    maxIndex, minIndex = x.index(max(x)), x.index(min(x))
    x[maxIndex], x[minIndex] = x[minIndex], x[maxIndex]
    
    res2 = "Massive before sorting MAX and MIN:" + str(x)
    return res1 + "\n" + res2
    

l = int(input("Enter length of massive: "))
print(fun(l))
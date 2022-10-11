def fun(x):
    for i in range( 1, x + 1 ):
        for j in range( 1, i + 1 ):
            print( j, end = "" )
        print("")


n = int(input())
print(fun(n))

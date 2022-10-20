def squareOfTheNumber(x):
    i = 1
    while i ** 2 <= x:
        print(i**2)
        i += 1


n = int(input())
print(squareOfTheNumber(n))
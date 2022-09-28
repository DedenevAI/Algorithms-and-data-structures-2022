def checkEqualColor(x,y,z,w):
    if (x+y+z+w) % 2 == 0:
        return 'YES'
    else:
        return 'NO'

a = int(input("Введите номер столбца для 1 кл.:"))
b = int(input("Введите номер строки для 1 кл.:"))
c = int(input("Введите номер столбца для 2 кл.:"))
d = int(input("Введите номер строки для 2 кл.:"))

print(checkEqualColor(a,b,c,d))

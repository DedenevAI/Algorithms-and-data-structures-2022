def lace_length(x,y,A,B):
    return 2 * A + (2 * B - 1) * x + 2 * (B - 1) * y

a = int(input("Расстояние между рядами:"))
b = int(input("Расстояние между дырочками:"))
L = int(input("Длина свободного конца шнурка:"))
N = int(input("Количество дырочек:"))

print("длина шнурка =", lace_length(a,b,L,N))

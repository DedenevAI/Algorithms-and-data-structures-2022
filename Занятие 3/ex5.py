#Функция сравнивает значения x,y,z между собой и возвращает значение минимального числа
def minimum(x,y,z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    elif z < x and z < y:
        return z

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

print("Min number:", minimum(a,b,c))
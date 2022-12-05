"""Вывести число в обратном порядке"""
#@this function return user's numbers in reverse order
def reverseNumber(x):
    if len(x) == 0:
        return x
    else:
        return reverseNumber(x[1:]) + x[0]

n = str(input('Введите число: '))
print(reverseNumber(n))
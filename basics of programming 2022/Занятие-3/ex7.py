def checkLeapYear(a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return "Да"
    else:
        return "Нет"

x = int(input("Enter the year number:"))

print(checkLeapYear(x))
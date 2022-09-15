import sys 
name = input("Введите Ваш имя:")
if name == "Иван":
    print("Иванов тут не любят")
    sys.exit()
age = int(input("Введите Ваш возраст:"))
if age == 0 or age >= 75:
    print("Некорректно указан возраст")
    sys.exit()
if age >= 16:
        print("Поздравляем вы поступили в ВГУИТ,", name)
else:
    a = 18 - age
    print("Сначала нужно окончить школу! Еще целых:", a, "лет!!")



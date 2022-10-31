def time(x):
    if x > 1440:
        return "Error"
    else:
        t = n % (60*24) // 60
        m = n % 60
        result = str(t) + " hours " + str(m) + " minutes"
        return result

n = int(input("Enter 'n' min number:"))

print("Now is", time(n))



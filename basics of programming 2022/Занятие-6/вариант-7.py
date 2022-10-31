# 7 Вариант
def fun(x):
    n = len(x)
    x = s[:n // 2].replace('п', '*') + s[n // 2:]
    return x

s = "пппппппыфыпппфывфвыпппвыфвфпппппппavottytezhedrugiebukvi"
print(fun(s))


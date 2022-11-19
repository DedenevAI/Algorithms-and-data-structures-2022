# @return an integer in a 10-digit octal code, keeping the leading zeros
def s(n):
    m = ""
    while n != 0:
        m = str(n%8) + m
        n //= 8
    return m

a = int(input("Enter your number = "))
print(s(a))
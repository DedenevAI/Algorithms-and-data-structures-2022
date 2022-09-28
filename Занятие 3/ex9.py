def checkСhocolateBreak(a,b,c):
    if c < a * b and ((c % a == 0) or (c % b == 0)):
        return 'YES'
    else:
        return 'NO'


n = int(input("Enter the first number:"))
m = int(input("Enter the second number:"))
k = int(input("Enter the third number:"))

print(checkСhocolateBreak(n,m,k))
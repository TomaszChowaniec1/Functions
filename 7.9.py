def f(number, even):
    number = abs(number)
    total = 0
    for digit in str(number):
        d = int(digit)
        if even and d % 2 == 0:
            total += d
        if not even and d % 2 == 1:
            total += d
    return total

num = int(input("Enter number"))

if f(num, True):
    print("Sum of even digits:", f(num, True))
if f(num, False):
    print("Sum of odd digits:", f(num, False))

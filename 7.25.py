def f(x, y):
    total = 0
    for n in range(x, y + 1):
        if n % 6 == 0 and n % 4 != 0:
            total += n
    return total

x = int(input("Enter start of range: "))
y = int(input("Enter end of range: "))

print("Sum:", f(x, y))

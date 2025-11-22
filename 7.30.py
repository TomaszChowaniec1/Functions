def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

n = int(input("Enter the end of range: "))

result = sum_natural(n)

print("Sum from 1 to", n, "=", result)

def f(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    return result

n = int(input("Enter n: "))
print(f(n))
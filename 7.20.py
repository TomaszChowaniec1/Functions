def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def f(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if prime(num):
            count += 1

    return num

n = int(input("Enter n: "))
print(f(n))
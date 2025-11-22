def f(expression):
    total = int(expression[0])
    i = 1

    while i < len(expression):
        op = expression[i]
        num = int(expression[i + 1]) 

        if op == '+':
            total += num
        elif op == '-':
            total -= num

        i += 2   # przechodzimy do kolejnego operatora

    return total

num = input("Enter expression: ")
print(f(num))
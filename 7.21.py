def f(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

print(f(number1, number2, number3))
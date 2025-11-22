def f(number1,number2,operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
            return number1 / number2
    else:
        return "Error: Unknown operator"
    
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

print("Result:", f(number1,number2,operator))
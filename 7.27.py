def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    
    a = int(product_code[0])
    b = int(product_code[1])
    c = int(product_code[2])
    control = int(product_code[3])
    
    expected = (a + b + c) % 7
    
    return control == expected

code = input("Enter product code: ")

result = f(code)
print(result)

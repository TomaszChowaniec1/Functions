def f(x, y):                                        #Liczenie liczb ujemnych liczb parzystych w zakresie
    count = 0
    for n in range(x, y + 1):               
        if n < 0 and n % 2 == 0:
            count += 1
    return count

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print("Negative numbers:", f(x,y))
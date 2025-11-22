def f(n1,n2,n3):
    return n1 < 0 or n2 < 0 or n3 < 0

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if f(n1,n2,n3):
        print("True")
else:
    print("False")
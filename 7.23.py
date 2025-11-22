def f(password):
    if len(password) < 6:
        return False
    return len(password) == len(set(password))

password = input("Enter a password: ")
if f(password):
    print("True")
else:
    print("False")

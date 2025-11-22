def f(binary_number):
    for ch in binary_number:
        if ch not in ('0', '1'):
            return False
    return True

dec = int(input("Enter a binary number: "))
if f(str(dec)):
    print('True')
else:
    print('False')


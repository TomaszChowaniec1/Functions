def f(palindrome):
    return palindrome == palindrome[::-1]

palindrome = input("Enter a palindrome: ")
if f(palindrome):
    print('True')
else:
    print('False')
    
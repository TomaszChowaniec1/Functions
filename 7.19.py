def f(number):
    number = str(abs(number))
    counts = {}

    for digit in number:
        counts[digit] = counts.get(digit, 0) + 1

    total = 0
    for digit, count in counts.items():
        if count > 1:
            total += int(digit) * count
    return total

num = int(input("Enter number: "))
print("Sum of repeated digits:", f(num))
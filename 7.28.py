def f(dice):
    max_digit = dice[0]
    max_count = 1
    current_count = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > max_count:
            max_count = current_count
            max_digit = dice[i]

    return int(max_digit)

print(f("5233165554211"))  # wynik: 5
print(f("2133"))           # wynik: 3
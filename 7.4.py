import letter_counter

text = input("Enter a text: ")

print(text)

letter_e = letter_counter.count_letter(text,'e')

print(f"The letter 'e' appears {letter_e} times in the text.")

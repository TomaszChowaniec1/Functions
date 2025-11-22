import hid_number

card_number = input("Enter your credit card number: ")
hidden_card = hid_number.hide(card_number)
print("Hidden credit card number:", hidden_card)
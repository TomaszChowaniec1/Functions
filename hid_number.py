def hide(card_number):
    first_two = card_number[:2]
    last_four = card_number[-4:]
    hidden_section = "*" * (len(card_number) - 6)
    return first_two + hidden_section + last_four

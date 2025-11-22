def f(detector):
    people = 0      
    max_people = 0    

    for change in detector:
        if change == '+':
            people += 1
        elif change == '-':
            people -= 1

        if people > max_people:
            max_people = people

    return max_people >= 3

detector = input("Enter detector string: ")
if f(detector):
    print('True')
else:
    print('False')

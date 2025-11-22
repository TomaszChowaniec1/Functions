import keyboard 


first_name = keyboard.input_string('Enter first name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')


print('\nDATA RECORD')
print('===========')
print('First Name:', first_name)
print('Last Name:', last_name)
print('Age:', age)

# Conditional printing of salary
if not is_salary_hidden:
    print(f'Salary: {salary:.2f}')
else:
    print('Salary: HIDDEN')
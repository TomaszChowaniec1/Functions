def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100
# Convert centimeters to inches
def cm_to_in(n):
    return n / 2.54

# Convert feet + inches to centimeters
def ft_in_to_cm(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches * 2.54

if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'100cm = {cm_to_in(100)} inches')
    print(f'5 feet 7 inches = {ft_in_to_cm(5, 7)} cm')
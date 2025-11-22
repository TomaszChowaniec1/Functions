import range 

x = int(input("A number: "))
y = int(input("Range start: "))
z = int(input("Range end: "))

result = range.in_range(x, y, z)

print(f"Number {x} in the range <{y},{z}>:", "yes" if result else "no")
import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))


d = b**2 - 4*a*c


if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Root are real and values are: ",x1 ,"And", x2)
elif d == 0:
    x = -b / (2*a)
    print(f"Roots are real and value are: {x}")
else:
    print(f"Roots are imaginary")

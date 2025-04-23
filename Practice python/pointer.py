
# x = 42
# print(hex(id(x)))  # prints memory address of x in hexadecimal

a = 10
b = 20

a, b = b, a  # swap

print("a =", a)  # 20
print("b =", b)  # 10

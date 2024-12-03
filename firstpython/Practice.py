# n =2
# while n <= 128 :
#     print(n)
#     n *= 2
    
    
# def calculate_square_and_cube(number):
#     square = number ** 2
#     cube = number ** 3
#     print(square)
#     print(cube)

# # Using the function for numbers 2, 3, and 4
# calculate_square_and_cube(2)
# calculate_square_and_cube(3)
# calculate_square_and_cube(4)    
    
# def compute_value(a, b):
#     # Solution as follows
#     c = a*a + 2*a*b + b*b
#     d = a + b
#     print(c)
#     print(d)

# t = 3
# for _ in range(t):
#     A, B = map(int, input().split())
#     compute_value(A, B)

# num = 1

# while num <= 10 :
#     print(num)
#     num = num + 1
#     if num == 5:
#         continue

# sum = 0

# for i in range(1,11):
#     print("its your number",i)
#     sum += i
    
# print(sum)

# arr = ["Sazid","Khalid","Asif","Ratik"]

# for index , element in enumerate(arr):
#     print(index,element)

# a,b,c = map(int , input().split())

# if a > b and a > c :
#     print("A is largest")
# elif b > a and b > c :
#     print(" B is largest")
# else:
#     print("C is largest")
    
# a = int(input("first"))
# b = int(input("Second"))
# c = int(input("Third"))

# big = max(a,b,c)
# print("The big number is : ",big)

# sum = a + b + c
# print(sum)

# for i in range(39,69):
#     if i % 2 == 1:
#         print(i)



# sum = (91408/10000) % 10
# print(sum)

# def inch_to_cm(inch):
#     cm = inch * 2.54
#     return cm

# a = int(input("Enter your number of inch : "))

# result = inch_to_cm(a)
# print("your cm value :",result)



# for item in l :
#     l.remove(item["if"])
#     print(item)
# a = 23
# b = 23

# if a != b:
#     print("abc")

    
    
# def rem(l,word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n
    
    
# l = ["Sazid","khalid","Ratik","Asif","if"]

# print(rem(l,"if"))


def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i}  = {n*i}")
        
multiply(8)
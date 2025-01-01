# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         return (22/7) *self.radius**2
    
#     def perimeter (self):
#         return 2* (22/7)* self.radius
    
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# t = int(input())
# for i in range(t):
#     n = int(input("Number"))
#     print(f"Your sum {n*2}")

# user = 3 #int(input("Enter your age : "))

# if user < 13 :
#     print("child")
# elif user <= 19 :
#     print("Teenager")
# elif user <= 59:
#     print("Adult")
# else :
#     print("Senior")

# day = input("What Is Today ?")
# age = int(input("Enter Your Age"))

# if age < 18 and day == "Wednesday" :
#     print("$6")
# elif age < 18 :
#     print("$8")
# elif age >=18 and day == "Wednesday":
#     print("$10")
# else :
#     print("$12")
    
# day = "friday" #input("What Is Today? ")
# age = 12  #int(input("Enter Your Age: "))

# if day == "Wednesday":
#     print("$6" if age < 18 else "$10")
# else:
#     print("$8" if age < 18 else "$12")

# day = "wednesda "
# age = 3

# price = 12 if age >=18 else 8

# if day == "wednesday":
#     price -= 2
# print(f"Ticket for you : ${price}")

marks = 40

if marks <= 90:
    print("A")
elif marks <=80 :
    print("B")
elif marks <= 70 :
    print("C")
elif marks <= 60:
    print("d")
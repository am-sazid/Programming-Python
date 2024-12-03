# a = input("Enter first word: ")
# b = input("Enter second word: ")
# print(a, b, sep=" - ")

# def solve(a, b):
#     return a**b
    
# result = solve(2, 4)
# print(result)

# def display_person(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")


# display_person(Name="Amir Khan", Age="45")

# numbers =[7,6,5,3,3,2,1]
# print(numbers[-4])

# numbers =[7,8,5,4,3,2,4]
# print(numbers[::-1])

# numbers =[22,19,19,14,33]
# numbers.sort()
# print(numbers)

# class student :
#     def __init__(self,Fullname):
#         self.name = Fullname
        # print("Your student is :",Fullname)
        # return init(self.name)
    # def __iter__(self):
    #     return iter(self.name)
        
# s1 = student("Sazid")
# s2 = student("sazid")
# print(s2.name)

# for nam in s1:
#     if s1 == __name__:
#         print("hello")
#     else :
#         print("helloo")
#     print(nam)

# class Student:
#     name = "anonymous"
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
# s1 = Student("Sazid",98)
# print(s1.name)
# # print(Student.name)
# s2 = Student.name
# print(f'Your Student name is:',s2)

# class Student :
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("Iam create a staticmethod")
#     def avg(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         print("Hi ",self.name,"Your avg marks is :" ,sum/3)
        
# st = Student("Sazid",[99,98,97])
# st.avg()
# Student.hello()

# # abstraction 
# class car :
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
        
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started...")
# car1 = car()
# car1.start()

class Account:
    
    def __init__ (self,bal,acc):
        self.balance = bal
        self.account = acc
        
    def debit(self,amount):
        self.balance -= amount
        print("BDT",amount,"Was debited..")
        print("Your total balance is :",self.total())
        
    def credit(self,amount):
        self.balance += amount
        print("BDT",amount,"Was credited..")
        print("Your total balance is :",self.total())
        
    def total(self):
        return self.balance
        
        
user1 = Account(10000,"SMSA31")
user1.debit(500)
user1.credit(20500)
class Car :
    brand = "Toyota"
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stop")
    
class Toyota(Car) :
    def __init__(self,name):
        self.name = name
        
car1 = Toyota("Fortune")
print(car1.brand)
print(car1.stop())

# Multi-Level Inheritance
class Car :
    brand = "Toyota"
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stop")
    
class Toyota(Car) :
    def __init__(self,name):
        self.name = name
        
class Fortuner (Toyota):
    def __init__(self,type):
        self.type = type
        
car1 = Fortuner("Diesel")
print(car1.type)
print(car1.start())

# Multiple Inheritance 
class A :
    varA = "Welcome to variable A"
class B :
    varB = "welcome to variable B"
    
class c (A,B):
    varC = "Welcome to variable C"
    
var = c()
print(var.varA)
print(var.varB)
print(var.varC)
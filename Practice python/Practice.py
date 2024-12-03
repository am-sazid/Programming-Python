
# x = memoryview(bytes(5))
# print(x)

# a = 1j
# b = 3j

# print(a + b)

# a = "hello , World!"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# x = "Hello"
# y = False

# print(bool(x))
# print(bool(y))

# x = ["sazid","Khalid","Asif","12","123","343","567"]

# # x[2]= "asif1"
# print(x)
# # print(x[-4:-1])
# print(x.reverse())

# x  = ["sazid","Khalid","Asif","12","123","343","567"]
# x.reverse()
# print(x)



# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         self.speed = 0  # Initial speed is 0 when the car is created

#     def start(self):
#         print(f"{self.color} {self.brand} is starting")

#     def accelerate(self, increase):
#         self.speed += increase
#         print(f"{self.brand} accelerates by {increase} km/h. Current speed: {self.speed} km/h")

#     def brake(self, decrease):
#         self.speed -= decrease
#         if self.speed < 0:
#             self.speed = 0
#         print(f"{self.brand} slows down by {decrease} km/h. Current speed: {self.speed} km/h")

#     def stop(self):
#         self.speed = 0
#         print(f"{self.color} {self.brand} has stopped")

# # Creating an object of Car class
# my_car = Car("Toyota", "Red")

# # Using methods of the Car class
# my_car.start()
# my_car.accelerate(30)
# my_car.accelerate(20)
# my_car.brake(15)
# my_car.stop()


# class Car:
#     Brand = "Toyota"
#     print(Brand)
#     def __init__ (self,Model ,speed):
#         self.Model = Model
        
#         self.speed = speed
#         print("Your Car Started Speed :",self.speed)
        
#     def speed_up(self,u_sp):
#         self.speed += u_sp
#         print("You increace speed ", u_sp)
#         print("Now Your Car Current Speed :",self.speed)
        
#     def spped_less(self,l_sp):
#         self.speed -= l_sp
#         print("You Less Speed ",l_sp)
#         print("Now Your Car Current Speed :",self.speed)
    
#     def total_spd(self):
#         return self.speed
    
# car1 = Car("Fortuner",100)
# car1.speed_up(12)
# car1.spped_less(15)

class Car:
    
    def __init__ (self,Model,color):
        self.Model = Model
        self.color = color
        self.speed = 0
        
    def Start(self):
        print(f"{self.color} {self.Model} is Started ")
        
    def acc(self,acc_up):
        self.speed += acc_up
        print(f"{self.Model} accelerates by {acc_up} km/h. current speed : {self.speed}")
    
    
    def slw(self,slw_dn):
        self.speed -= slw_dn
        if slw_dn < 0 :
            print(f"Your {slw_dn} km/h Slow down is impossible ")
        else:
            print(f"{self.Model} slows down by {slw_dn} km/h. current speed : {self.speed} ")
        
            
    def stop(self):
        print(f"{self.color} {self.Model} has stopped")
        
car1 = Car("Fortuner","Black")
car1.Start()
car1.acc(40)
car1.acc(15)
car1.slw(-120)
car1.stop()
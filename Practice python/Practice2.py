
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
# my_car.brake(-15)
# my_car.stop()


# class student :
    
#     def __init__ (self,name):
#         self.name = name
        
# st = student("Sazid")
# del st.name

# if hasattr(st, 'name') :
#     print(st.name)
# else:
#     print("The name is deleted")
# # print(st.name)

# list = ['mushfik','liton','tamim','rubel']
# list.append('23')
# print(list)

a = 1 

while a<=10 :
    a = a+1
    print(a)
    if a == 5:
        break


# list = ['mushfik','liton','tamim','rubel']
# list1 = {"Sazid",'34','455','56'}
# list.extend(list1)
# list.pop()

# del list[0]
# list.clear()
# print(list)


# for i in range(len(list)):
#     print(i,list)

# for i,j in enumerate(list):
#     print(i,j)
# i = 0
# while i < len (list):
#     print(list[i])
#     i += 1
    
# for i in list :
#     print(i)



class Car :
    
    def __init__ (self,Type):
        self.Type = Type
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stop")
    
class Toyota(Car) :
    def __init__(self,name,Type):
        super().__init__(Type)
        self.name = name
        super().start()
car1 = Toyota("Fortuner","Petrol")
print(car1.Type)

        
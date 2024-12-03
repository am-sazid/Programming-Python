class pen:
    Manufacture = "CM Eshop"
    
    
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price
        
        
my_pen = pen('Sazid','Matador',5)
print(f"Manufacture by : {my_pen.Manufacture},Owner : {my_pen.owner}, Brand : {my_pen.brand},Price : {my_pen.price}")

his_pen = pen('His','Economy',10)
print(f"Manufacture by : {his_pen.Manufacture},Owner : {his_pen.owner}, Brand : {his_pen.brand},Price : {his_pen.price}")
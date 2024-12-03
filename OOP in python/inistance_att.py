class shop:
    Shopping_mall = "Jamuna"
    
    def __init__(self,Buyer):
        self.Buyer = Buyer
        self.cart = []
    def add_to_cart(self,item):
        self.cart.append(item)
    
Sazid = shop('Sazid')
Sazid.add_to_cart('PowerBank')
Sazid.add_to_cart('Smart Watch')
print(f"ShoppingMAll : {Sazid.Shopping_mall} ,Cart : {Sazid.cart}")
She = shop("She")
She.add_to_cart('Bag')
print(f"ShoppingMAll : {She.Shopping_mall} ,Cart : {She.cart}")
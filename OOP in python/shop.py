class Shop:
    cart = []
    
    def __init__(self,buyer):
        self.buyer = buyer
        
    def add_to_cart(self,item):
        self.cart.append(item)
        
        
sazid = Shop('Sazid')
sazid.add_to_cart('Smart Watch')
sazid.add_to_cart('Power Bank')
print(sazid.cart)

She = Shop('She')
She.add_to_cart('Bag')
print(She.cart)

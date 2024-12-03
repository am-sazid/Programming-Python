balance = 5000

def buying(item,price):
    global balance
    print("Previous Balance",balance)
    balance -= price
    print(f"Balance after buying {item}",balance)
    
buying("Smart Watch",3200)

a = 23
b = 20
c = 16

sum = min(a,b,c)
print(sum)
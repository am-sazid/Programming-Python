
user = input("Enter out side weather :")

weather = user.lower()

if weather == "sunny":
    print("GO for walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Buid Snowman")
else:
    print("Your determined weather is not in our memory.")

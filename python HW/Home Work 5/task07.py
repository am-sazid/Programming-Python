x = int(input("Enter the current time: "))

if x < 10:
    greeting = "Good Morning!"
elif x < 12:
    greeting = "soon time for lunch"
elif x < 18:
    greeting = "Good day"
elif x < 22:
    greeting = "Good evening"
else:
    greeting = "Good night!"

print(greeting)

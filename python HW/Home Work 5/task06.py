n = int(input("Enter the marks: "))

if n > 100:
    result = "Don't be over your marks are not above 100"
elif n >= 80:
    result = "You got A+"
elif n >= 70:
    result = "You got A"
elif n >= 60:
    result = "You got A-"
elif n >= 50:
    result = "You got B"
elif n >= 40:
    result = "You got C"
elif n >= 33:
    result = "You got D"
else:
    result = "You are fail, try again to have a better result"

print(result)
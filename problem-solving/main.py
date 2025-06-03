# Calculator 

first = input("Enter first number: ")
second = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = float(first) + float(second)
elif operation == '-':
    result = float(first) - float(second)
elif operation == '*':  
    result = float(first) * float(second)
elif operation == '/':
    if float(second) != 0:
        result = float(first) / float(second)
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"
print("Result:", result)
# This code is a simple calculator that performs basic arithmetic operations
# based on user input. It prompts the user for two numbers and an operation,
# def sum(num1,num2):
#     result = num1 + num2
#     return result

# total = sum(220,110)
# print(total)


# def famous(first,last):
#     name = f"{first}, {last}"
#     return name

# name = famous("Adnan" ,"Hujur")
# print(name)

# def dubble_it(num):
#     result = num * 2
#     # print(result)
#     return result

# All = dubble_it(10)
# # dubble_it(20)
# print(All)

# def sum(num1,num2):
#     result = num1 + num2
#     return result

# total = sum(20,50)
# print(total)

# final = dubble_it(total)
# print("Final result is :",final)

def all_sum(*args):
    sum = 0
    for num in args:
        # print("Your number is : ",num)
        sum += num
    return sum
    
total = all_sum(34,32,23,12,45,21)
print("Total Sum",total)
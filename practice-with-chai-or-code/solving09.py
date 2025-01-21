
# number = 5


# for i in range(1,11):
#     if i == 5 :
#         continue
#     print(number ,"X", i, "=", number*i)
    
text = "Hello"
reversed = ""

# for i in reversed(text):
#     print(i)

for char in text:
    reversed = char + reversed
print(reversed)
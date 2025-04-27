
# a = 127

# a = abs(a)

# sum = 0

# for i in str(a):
#     sum += int(i)
# print(sum)


# word = "madam"

# r_word = word[::-1]

# if r_word == word:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# a = 5

# factrial = 1

# for i in range(1, a + 1):
#     factrial *= i
# print( a ,"x" ,i ,factrial)


# number = 5
# factorial = 1

# for i in range(1, number + 1):
#     print(f"{factorial} × {i} = {factorial * i}")
#     factorial *= i

# print(f"\nFactorial of {number} is: {factorial}")



N ,M= map(int,input().split())

half = N / 2



if M >= half:
    print("Newbie")
else:
    print("Pro")
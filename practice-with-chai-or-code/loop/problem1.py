
# while True:
#     user = int(input("Enter a number 1 -10 :"))
#     if 1 <= user <= 10:
#         print("Your Number: ",user)
#         break
#     print("Wrong input Try again!")
# N = int(input())

# # Read the list of numbers
# numbers = list(map(int, input().split()))

# # Check if the list is in ascending order

# if numbers == sorted(numbers):
#     print("Yes")
# else:
#     print("No")



N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    if A == sorted(A) and N == len(A):
        print("YES")
        break
    else:
        print("NO")
        break


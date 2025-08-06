

t = int(input())
input1 = ""

for i in range(t):
    word = input()
    

    if len(word) > 10 :
        print(f"{word[0]}{len(word)-2}{word[len(word)-1]}")
    else:
        print(word)
        

    # input1.append(word)

# print(input1)
# for item in input1:
#     print(item)

# print(total)

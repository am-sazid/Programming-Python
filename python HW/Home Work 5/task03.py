word = input("Input your word: ")
word = word.casefold()

reversed_word = word[::-1]

if word == reversed_word:
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")


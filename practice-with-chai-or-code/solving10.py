

input_string = "teeterebebeb"


for char in input_string:
    print(char)
    if input_string.count(char) == 1 :
        print("The First Non-Reapeting Charecter " , char)
        break
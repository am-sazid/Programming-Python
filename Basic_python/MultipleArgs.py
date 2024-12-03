# def famous(first,last):
#     name = f"{first}, {last}"
#     return name

# name = famous("Adnan" ,"Hujur")
# print(name)


# def famous_name(first,last,title,religion) :
#     name = f"{title}, {first}, {last}, {religion}"
#     return name
# name = famous_name("Dr.","Zakir","Naiek", "Islam")
# print(name)


def name(**kargs):
    name = kargs
    return name


name2 = name(title="Dr",first="Zakir",last="Naiek",religion="Islam")
print(name2)



a = "dgAaCdeF"

count = 0


for i in a:
    if i.isupper():
        count += 1

if i[0].islower():
    print(count+1)
else:
    print(count)
    
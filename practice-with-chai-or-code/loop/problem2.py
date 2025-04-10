
items = ["apple", "banana","banana", "orange", "mango"]

uniqe_items = set()

for item in items:
    if item in uniqe_items:
        print("Duplicate item found:", item)
        break
    uniqe_items.add(item)




x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

# Different

number = (5,45,23,12,67,56,80,5,45,23,12)

number_set = set(number)

print(number_set)

number_set.remove(5)
print(number_set)
number_set.add(55)
print(number_set)

for x in number_set :
    print(x)
if 23 in number_set :
    print("23 In")
    
    

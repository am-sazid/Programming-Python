numbers = [33,5,45,65,36,98]
numbers.append(100)
print(numbers)

index = numbers.index(98)
print(index)

a = [2,3,4,5]
b = [6,7,8,9,565655]

a.extend(b)
print(a)

numbers.insert(0,47)
print(numbers)
numbers.remove(45)
print(numbers)

numbers.pop()
print(numbers)

numbers.clear()
print(numbers)


if 5 in numbers:
    index = numbers.index(5)
    print(index)

numbers.sort()
print(numbers)

numbers.count(36)
print(numbers)

a = [2,4,4,2,6,2,4,2]
count2 = a.count(2)
print(count2)
numbers.reverse()
print(numbers)

numbers.copy()
print(numbers)

import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
print(a)

A, B = map(int, input().split())

total_boys = A + 1
total_slices = total_boys * 4 + B * 3
pizzas_needed = (total_slices + 7) // 8

print(pizzas_needed)


for i in range(4):
    print("****")
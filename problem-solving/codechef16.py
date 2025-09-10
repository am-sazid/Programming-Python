
R, B = map(int, input().split())

green = min(R, B)

remaining_red = R - green
remaining_blue = B - green

skill = (green * 5) + (remaining_red * 1) + (remaining_blue * 2)
print(skill)

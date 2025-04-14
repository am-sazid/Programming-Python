
t = int(input())

for i in range(t):
    N , M = map(int, input().split())
    bike = N *2
    car = M *4
    print(bike + car)
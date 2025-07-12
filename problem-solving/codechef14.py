t = int(input())            
for i in range(t):          
    A, C = map(int, input().split())
    d = A + C
    B = d // 2
    if d % 2 == 0:
        print(B)
    else:
        print(-1)

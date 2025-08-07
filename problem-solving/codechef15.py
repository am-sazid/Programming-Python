N = input()

LwcN = N.lower() 

reArr = LwcN[::-1]

if len(N) == 3:
    if LwcN == "cat" or LwcN == reArr:
        print("YES")
    else:
        print("NO")
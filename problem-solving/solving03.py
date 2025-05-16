
marks = [67,89,36,78,90,100,53,45]

failmarks = False

for mark in marks:
    if mark < 33:
        failmarks = True
       
        break
        
if failmarks:
    print("You have failed the exam")
else:
    print(sum(marks))
    
        
score = 10

if score >=101:
    print("Please input correct score !!")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 33:
        grade = "D"
    else :
        grade = "F"
        
    print("Your Grade : ",grade)
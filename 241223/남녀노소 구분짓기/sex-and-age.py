gender = int(input())
age = int(input())

if(age >= 19):
    print("WOMAN" if gender else "MAN")
else:
    print("GIRL" if gender else "BOY")
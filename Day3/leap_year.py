# check entered year is leap year or not

year = int(input("Enter a year: "))
leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

print(leap_year)

if leap_year:
    print(f"{year} is a leap year")   
else:
    print(f"{year} is not a leap year")   
     
    
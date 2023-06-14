leap_year = 2020
if not leap_year%4==0:
        print(f"{leap_year} is not leap year")
elif leap_year%100==0:
    if leap_year%400==0:
        print(f" {leap_year} is a leap year ")
    else :
        print(f"{leap_year} is not leap year")
else: 
    print(f"{leap_year} is a leap year")
        
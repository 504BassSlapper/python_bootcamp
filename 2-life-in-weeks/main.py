age = int(input("What is ur current age: \t "))
# assuming a year is 365 days and 52 weeks and 12 months ( not exatly)
years_remaining = 90 - age
months_remaining = years_remaining*12
weeks_remaining = years_remaining*52
days_remaining = years_remaining*365
age_in_month=age*12 
age_in_weeks=age*52
age_in_days=age*365

print(f" ur age is {age_in_days} days {age_in_month} months and {age_in_weeks}")
print(f" ur age is {days_remaining} days {months_remaining} months and {weeks_remaining} weeks ")

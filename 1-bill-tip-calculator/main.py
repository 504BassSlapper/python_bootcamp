print("Welcome to our restaurant \n we hope tha you enjoyed your meal")
bill = float(input("Your bill :"))
person = int(input("Would you want to split the bill ? "))
percent_tip = float(input("tip to giv in percent" ))

bill_and_tip = bill + bill * percent_tip/100
if(person>0):
    splited_bill = bill_and_tip/person
    final_bill = round(splited_bill, 2)
    print(final_bill)



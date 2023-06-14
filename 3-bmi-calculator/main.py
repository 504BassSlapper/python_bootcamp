from termcolor import colored
height= float(input("enter your height in m"))
weight = float(input("enter your weight in kg"))

bmi = round(weight/(height**2)) 

if(bmi<18.5):
    print(colored(f"underweight your bmi is {bmi}", "blue"))
elif bmi<25:
    print(colored(f"your bmi is {bmi} your normal weight ", "green"))
elif bmi < 30:
    print(colored(f"your bmi is {bmi} you are overweight ", "red"))
elif bmi<35:
    print(colored(f"your bmi is {bmi} your are obese  ", "red"))
else:
    print(colored(f"your bmi is {bmi}, you are clinacally obese", "red"))
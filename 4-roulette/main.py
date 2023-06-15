import random

names = input("please provide the names for the game separated whith a coma \n")
splited_names = names.split(",")
print(splited_names)
random_choice = 0
if splited_names:
    random_choice = random.randint(0, len(splited_names) -1)
    print(f"{splited_names[random_choice]} is going to pay today drinks")
else:
    print("no names provided")


    
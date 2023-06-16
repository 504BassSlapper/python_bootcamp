import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
                      '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?']

password_letters = int(input(" password letters "))
password_numbers = int(input(" password numbers "))
password_symbols = int(input(" password symbols "))

password = []

for char in range(1, password_letters +1):
    password += random.choice(letters)

for char in range(1, password_numbers +1):
    password += random.choice(str(numbers))
    
for char in range(1, password_symbols +1):
    password += random.choice(special_characters)

print(password)
random.shuffle(password)
print(password)

final_password = ""
for i in password:
    final_password += i
print(final_password)

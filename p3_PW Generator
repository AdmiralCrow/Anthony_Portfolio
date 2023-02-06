import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

password = ""

#1 in range of # +1 adds those choices to string
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
 
#same as above but symbols
for sym in range(1, nr_symbols + 1):
    password += random.choice(symbols)

#same as above but #'s
for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Your easy password is{password}")

#Hard Level - Order of characters randomised:

#PW List
pw_list=[]
#PW String
hard_pw = ""
#1 in range of # +1 adds those choices to list
for char in range(1, nr_letters + 1):
    pw_list += random.choice(letters)
    
#same as above but symbols
for sym in range(1, nr_symbols + 1):
    pw_list += random.choice(symbols)
    
#same as above but #'s
for num in range(1, nr_numbers + 1):
    pw_list += random.choice(numbers)
#shuffle list    
random.shuffle(pw_list)

#turn list into a string
for x in pw_list:
    hard_pw += '' + x 
    
print(f"Your hard password is{hard_pw}")


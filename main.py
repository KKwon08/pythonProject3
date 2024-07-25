import random

letters = ["a", "b", "c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$',"%",'^','&',"*",'(',')']

print("Welcome to the random password generator")
n_letter = int(input("How many letters would you like in your password?\n:"))
n_number = int(input("How many numbers would you like in your password?\n:"))
n_symbol = int(input("How many symbols would you like in your password?\n:"))

password = ''

for i in range(n_letter):
    password += random.choice(letters)

for i in range(n_number):
    password += random.choice(numbers)

for i in range(n_symbol):
    password += random.choice(symbols)


print(f'your final password is, {password}\n')


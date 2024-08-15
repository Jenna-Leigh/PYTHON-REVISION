import random
letter= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '8', '9']
symbols =['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
print("Welcome to the password generator!")
nr_letters= int(input(" How many letters would you like in your password? ")) #nr_letters: Asks the user for the number of letters they want in their password and converts the input to an integer.
nr_symbols = int(input(" How many symbols would you like in your password? ")) #nr_symbols: Asks the user for the number of symbols they want in their password and converts the input to an integer.
nr_numbers = int(input(" How many numbers would you like in your password? ")) #nr_numbers: Asks the user for the number of numbers they want in their password and converts the input to an integer.
password= ""
for char in range( 1, nr_letters + 1 ): #This loop runs nr_letters times.
    password += random.choice(letter)# random.choice(letter): Selects a random letter from the letter list.
    
for char in range( 1, nr_symbols + 1 ):
    password += random.choice(symbols)
    
for char in range( 1, nr_numbers+ 1 ):
    password += random.choice(numbers)

print(password)


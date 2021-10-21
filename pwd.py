# Password Generator Using Python

print('Random Password Generator\n')

# Importing string module for password character.
import string

# Importing random module for shuffling the password character
import random

# For strong password, I'm using upper & lower case character, including digits and punctuation.
str_1 = string.ascii_lowercase
str_2 = string.ascii_uppercase
str_3 = string.digits
str_4 = string.punctuation

# Taking user input for the password length.
pwd_length = int(input('Enter Password Length in digits: '))

# Creating empty list for password generation
strn = []

# Extending all the string in empty list.
strn.extend(list(str_1))
strn.extend(list(str_2))
strn.extend(list(str_3))
strn.extend(list(str_4))

# Shuffling all the character in the strn.
random.shuffle(strn)

# Printing strong password as per user required.
print(f'\nYour new random password is:\n')
print(''.join(strn[0:pwd_length]))

import random
import string


print("***Password Generator***")

#get password length
temp_length = int(input("Enter password length: "))
valid = False


#validate length
while valid != True:
  if temp_length > 0 and temp_length <16:
    length = temp_length
    valid = True
  else:
    print("Invalid input. Please type a number between 1 and 15")
    temp_length = int(input("Enter password length: "))


#user preference 
want_number = int(input("Enter 1 if you would like numbers in your password: "))
want_symbol = int(input("Enter 1 if you want symbols in your password: "))


#define the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbol = string.punctuation


#Get symbols and numbers based on user preference
if want_number == 1 and want_symbol == 1:
  all = lower + upper + number + symbol
if want_number == 1 and want_symbol != 1:
  all = lower + upper + number
if want_number != 1 and want_symbol != 1:
  all = lower + upper + symbol
else:
  all = lower + upper

#get the randomized password
temp = random.sample(all, length)
password = ''.join(temp)
print(password)

#EX.6-2 Random password generator


#used to generate random values
import random

#this line sets the desired length of the password to 10 characters. You can change this value to create longer or shorter passwords.
password_length  =  10

#these sets will be used to create a mixed character set for the password.
char_alphanumeric = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_punctuation = "!$%&'()*+,-/:;<=>?@[\]^_{|}~"

#provides predefined string constants, such as string.ascii_letters, string.punctuation, and string.digits.
import string

char = string.ascii_letters + string.punctuation + string.digits

# Inside the loop, it generates a random password by:
#Using a list comprehension to choose random characters from the char set, repeating this process 10 times (as specified by the inner loop).
#Joining these randomly chosen characters together using "".join() to form a single string, which represents a part of the password.
for i in range(password_length):
   password = "".join(random.choice(char) for i in range (10))
        
print('New password is: ' , (password))
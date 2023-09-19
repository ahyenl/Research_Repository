#ex1-5 Concatenation of strings

 #This line prompts the user to enter their first name, family name and role.
fname = input("Enter your first name: ")
surname = input("Enter your family name: ")
role = input("Enter your role: ")

 #This line concatenates the first name and the surname to form a full name. The full name is stored in the variable result.
result = fname + " " + surname 

 #result is the full name collected from the user, while ("(" , role , ")") is used to enclose the user's role in parentheses.
print("Result: ", "\033[35m" , result , "(" , role , ")")


#ex.2-3 Programming inspirator

 #This line prompts the user to enter the name of a programming language.
language = input("Enter the programming language: ")

 #This is the beginning of the new "match" statement. It allows you to perform pattern matching based on the value of the language variable.
match language:
    case 'JavaScript':
        print("You can become a Web Developer")
    case 'PHP':
        print("You can become a Backend Developer.")
    case 'Phyton':
        print("You can become a Data Scientist")
    case 'Solidity':
        print("You can become a Blockchain developer")
    case 'Java':
        print("You can become a Mobile App Developer.")

 #After the "match" statement, this line is outside of all the case blocks. It is executed regardless of whether any of the cases matched or not. It prints a general message that highlights the importance of problem-solving skills in programming.
print("The language doesn't matter, what matters is solving problems.")


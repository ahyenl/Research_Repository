#ex.1-1 Console menu
#using print and input commands with coloured text codes

 #This line uses ANSI escape codes to change the text background color to blue (code \033[44m) and print a welcome message with a blue background. The \033[0m at the end resets the text color to the default.
print("\033[44m***** Welcome to ConsoleServe - Your Virtual Console Server Support! *****\033[0m")

 #The next several lines use ANSI escape codes to change the text color. The numbered lines ( 0, 2, 4, 6, etc.) set the text color to red (code \033[31m), and lines ( 1, 3, 5, 7, etc.) set the text color to blue (code \033[34m). These lines display various options for the user to choose from. Each option is labeled with a number (1 to 7) and a description.
print("\033[31m For Technical Support, press '1'")
print("\033[34m For Account Assistance, press '2'")
print("\033[31m For Console Access, press '3'")
print("\033[34m For Network Configuration, press '4'")
print("\033[31m For System Updates, press '5'")
print("\033[34m For Billing and Payments, press '6'")
print("\033[31m For General Inquiries, press '7'")
print("\033[34m For Speaking to a Live Agent, press '0'")

 #This line sets the text color back to the default (code \033[39m) and then prompts the user to enter their choice. 
choice = input("\033[39m Enter your choice: ")

 #The code prints a message indicating the user's choice. It displays "Your choice is" followed by the value stored in the 'choice' variable.
print("Your choice is ", choice)


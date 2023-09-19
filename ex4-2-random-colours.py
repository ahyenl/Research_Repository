#EX.4-2 Random colours

#This line imports the choice function from the random module. The choice function is used to select a random element from a sequence, which will be used to choose a random color code from the colours list.
from random import choice

#This line defines a list called colours that contains various ANSI escape codes for changing text colors. 
colours = ["\033[30m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", 
"\033[35m", "\033[36m", "\033[37m","\033[90m", "\033[91m", 
"\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", 
"\033[97m","\033[49m", "\033[40m", "\033[41m", "\033[42m",
"\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m", 
"\033[100m", "\033[101m", "\033[102m", "\033[103m", "\033[104m", 
"\033[105m", "\033[106m", "\033[107m"]


#The code uses a for loop to generate the messages and apply random colors. The loop iterates 30 times (for i in range(30):), creating 30 "Hello, students!" messages with random colors.
#Inside the loop, the print statement is used to display each message. The message itself is static and is always "Hello, students!".
i = 30
for i in range (30):
    print("Hello, students!", choice(colours))
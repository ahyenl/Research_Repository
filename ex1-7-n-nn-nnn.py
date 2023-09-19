#ex.1-7 n+nn+nnn calculation


 #This line uses ANSI escape codes to change the text color to yellow (code \033[33m) and prints a title for the calculator. The title is enclosed in vertical bars for decoration.
print("\033[33m||||| n + nn + nnn calculator |||||")

  #This line sets the text color back to the default color (code \033[39m) and then prompts the user to enter a digit 'n'. The input is stored as a string in the variable 'n'.
n = input("\033[39mEnter any digit n: ")

    #Since the input is stored as a string, this line converts it to an integer so that mathematical operations can be performed on it.
n = int(n)

 #This line calculates 'nn' by multiplying 'n' by 11. This is equivalent to 'n' repeated twice.
nn = n * 11

 #This line calculates 'nnn' by multiplying 'n' by 111. This is equivalent to 'n' repeated three times.
nnn = n * 111

 #the code calculates the sum of 'n', 'nn', and 'nnn' and stores it in the 'result' variable
result = n + nn + nnn

 #displaying the values of 'n', 'nn', 'nnn', and their sum.
print(f"{n} + {nn} + {nnn} = {result}")





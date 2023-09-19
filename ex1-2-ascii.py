#ex.1-2 ASCII cat


 #The statement prints an ASCII art cat face and the entire cat is enclosed in triple-quoted strings for a multi-line format.
print('''
      (\___/)
      (=*.*=)
      U-----U
      ''')

 #the second ASCII art is displayed in green text, while the first one uses the default text color.

print('''\033[92m
             .-"""-.
            /       \ 
            \       /
     .-"""-.-`.-.-.<  _
    /      _,-\ ()()_/:)
    \     / ,  `      `|
     '-..-| \-.,___,  /
           \ `-.__/  /
            `-.__.-'`
      \033[0m''')
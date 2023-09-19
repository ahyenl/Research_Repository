#EX.4-4 Invitation email

#This line imports the choice function from the random module. The choice function is used to randomly select an element from a list, which will be a student's name in this case.
from random import choice

#It's a list called students that contains the names of various students who are invited to the exhibition.
students = ["Punit", "Graham", "Alex", "Karen", "Van",
 "Falwinder", "Gurpreet", "Jasper", "Lyle", 
 "Nega", "Amandeep", "Pawandeep", "Daman", 
 "Pruthviraj", "Beau", "Thilini", "Jashandeep", 
 "Ritesh", "Sahilpreet", "Onkar", "Sourav",
 "Harkamalpreet", "Talwinder"]

#It uses to print function to display the invitation message. It randomly selected student's name (chosen using choice(students)) in red text (code \033[31m). 

print("Dear \033[31m", choice(students), "\033[39m,")
print('''
\033[39mWe are happy to invite you to our Student Work Exhibition,
happening on \033[31mThursday, 21 September 2023,
\033[39mat the Whitecliffe campus (67 Symonds Street, Auckland)
from \033[31m10:00 AM to 1:00 PM.
\033[39mJoin us in celebrating the remarkable achievements of our students
and the outstanding work they've accomplished this term.
We look forward to seeing you at the exhibition!
      
Best regards,
Ying, Marina, Rashid, John, Pinal''')
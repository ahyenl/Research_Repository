# Grade calculator


 #This line prompts the user to enter an exam mark within the range of 0 to 100.t.
mark = input("Enter your exam mark (0-100): \033[32m")

 #convert into integer
mark= int(mark)


 #The code uses a series of if-elif-else statements to determine the grade based on the value of mark. Each if or elif statement checks the value of mark within a specific range and assigns a grade accordingly. The grade is then printed with a green text color.
if mark >= 100:
     print("\033[31mIncorrect input: the mark must be a number between 0 and 100%")
elif mark >= 90 :
    print("\033[39mYour grade is \033[32mA+")
elif mark >= 80 and mark <90:
    print("\033[39mYour grade is \033[32mA")
elif mark >= 70 and mark <80:
    print("\033[39mYour grade is \033[32mB")
elif mark >= 60 and mark <70:
    print("\033[39mYour grade is \033[32mC")
elif mark >= 50 and mark <60:
    print("\033[39mYour grade is \033[32mD")
elif mark < 50 :
    print("\033[39mYour grade is \033[32mFail")


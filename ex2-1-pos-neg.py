# EX.2-1 Positive or negative


 #This line prompts the user to enter a numeric value and stores the input as a string in the variable number.
number = input("Enter any numeric value: ")

 #Since the input is collected as a string, this line converts it to an integer using the int() function. This conversion allows the program to perform numeric comparisons on the input value.
number = int(number)


 # using if-elif statement , it allows you to check multiple conditions sequentially, and as soon as one condition is true, the corresponding block of code is executed, and the rest of the elif branches are skipped.
if number == 0:
    print("This number is zero")
elif number > 1:
    print("This number is positive")
elif number < 1:
    print("This number is negative")

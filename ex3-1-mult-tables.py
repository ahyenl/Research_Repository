#ex.3-1 Multiplication table
#FOR loop


print("****************************")

 #It will ask the user to enter a whole number and stores the input as an integer in the variable number. The int() function is used to convert the user's input (which is initially a string) into an integer for mathematical operations.
number = int(input("Enter any whole number: "))

 #This line prints a message indicating that the following table is a multiplication table for the number entered by the user.
print("Multiplication Table for " , number )

 #This line sets up a for loop that iterates from 1 to 10. This loop will be used to calculate and print the multiplication table for the entered number.
#Within the for loop, this line calculates and prints each multiplication operation. It displays the multiplication expression as follows: number x i = result, where number is the user-entered number, i is the current value of the loop variable (ranging from 1 to 10), and result is the product of number and i.
for i in range (1,11):
    print (number, 'x' , i , '=' , number * i)

print("****************************")
#EX.2-2 Discount calculator

 #This line prompts the user to enter the total sum of money spent.
sum = input("Enter the total \033[31msum  \033[39mof money spent: ")

 #convert into integer
sum= int(sum)


 #The code uses an if-elif statement to check the value of sum and calculate the discount based on the conditions:
if sum <= 499:
    discount = 0
    print("Discount Applied: \033[31m"  , "\033[39m(", discount, "%" , ")")
    total = sum - discount
    print("\033[39mTotal to Pay after Discount: \033[31m$" , total )
elif sum >= 499:
    discount = 0.9
    print("Discount Applied: \033[31m"  , "\033[39m(", discount, "%" , ")")
    total = sum * discount
    print("\033[39mTotal to Pay after Discount: \033[31m$" , total )
elif sum >= 1000:
    discount = 0.9
    print("Discount Applied: \033[31m"  , "\033[39m(", discount, "%" , ")")
    total = sum * discount
    print("\033[39mTotal to Pay after Discount: \033[31m$" , total )

 #Each branch of the if-elif structure prints the applied discount percentage, the discount amount, and the total amount to pay after the discount. 

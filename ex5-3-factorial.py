#EX.5-3 Factorial


# calculates factorial n!
# parameters: n (any integer number) 
def factorial(n):
    # check if the input is integer
    # exit the function if not
    if not(isinstance(n, int)):    #This line checks if the input n is an integer using the isinstance function. If n is not an integer, it prints "Incorrect input." 
        print("Incorrect input.")
        return -1
    
    f = 1
    for i in range(1, n+1):
        f *= i
    return f;


n = input("\nEnter any whole number: ")

# try to convert the input into integer
try: 
    n = int(n)
except:    #If the conversion to an integer fails, this block will be executed and prints "Incorrect input." to indicate that the input provided is not a valid whole number.
    print("Incorrect input.")
    exit(0)

#prints the factorial expression with the calculated factorial value.
print(f"{n}! = {factorial(n)}\n")
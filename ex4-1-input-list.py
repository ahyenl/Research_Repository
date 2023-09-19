#EX.4-1 From input to list

#It's an empty list called input_list. This list will be used to store the user's inputs.
input_list = list()

#The code uses a for loop to iterate five times (for i in range(5):), which means it will collect five inputs from the user.
#Inside the loop, the program collects user input using the input() function:

for i in range (5):
        user = input("Enter any string or number: ")
        input_list.append(user)

#After the loop has collected all five inputs, the code prints the contents of the input_list using the print() function:
print("My List: " , input_list )




#ex.1-4 Math calculations

 #This line simply prints a message to the console, instructing the user to enter numeric values. 
print("Enter numeric values:") 

 #asking users to input value for x, y, and z
x = int(input("x= "))
y = int(input("y= "))
z = int(input("z= "))

 #calculates the result (res1) based on a mathematical expression. The expression is as follows:
res1= x* (1 + x**2 / y**2)**z + z*y*z

 #displaying the result of calculation
print("result = " , res1)


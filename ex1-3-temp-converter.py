#ex.1-3 Temperature converter

 #this line prints a header message to the console, indicating that it's a Fahrenheit to Celsius converter.
print("|------ Fahrenheit to Celsium converter ------|")

 #This line prompts the user to enter a temperature in Fahrenheit. The input function is used to collect user input as a string, and the entered value is stored in the variable temperatureF.
temperatureF = input("Enter temperature(Fahrenheit) F= ")

 #convert the input to an integer. This conversion allows mathematical operations to be performed on the temperature value.
temperatureF = int(temperatureF)

 #This line calculates the equivalent temperature in Celsius using the Fahrenheit to Celsius conversion formula.
temperatureC = 5/9*(temperatureF - 32)

 #this line prints the converted temperature into Celsius.This formats the output in a user-friendly way.
print(temperatureF , "F" , "=" , temperatureC , "C")

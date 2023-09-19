#EX.4-3 Multiplicator

#This line imports the random module, which provides functions for generating random numbers.
import random

#This line imports the statistics module, which contains functions for performing statistical operations on data, such as calculating the mean, minimum, and maximum.
import statistics

#This line initializes an empty list called num_list. This list will be used to store a series of random numbers.
num_list = []
for i in range (10):  #iterates 10 times.
        num_list.append(round(random.uniform(0, 10), 2)) #generates a random floating-point number between 0 and 10 using random.uniform() and rounds it to two decimal places using round(). The generated number is then appended to num_list.

print("List: " , num_list)
mult = 1 #This line initializes a variable mult with the value 1. This variable will be used to store the result of multiplying all the numbers in num_list.
for element in num_list: #iterates through each element in num_list.
        mult *= element  #multiplies each element by the current value of mult. This accumulates the product of all elements in the list.
print("Result of Multiplication = ", mult)
print("Avg = ", statistics.mean(num_list))
print("Min = ", min(num_list))
print("Max = ", max(num_list))



#ex.3-3 Bingo card
#random

#This line imports the random module, which provides functions for generating random numbers.
import random

 #The code uses a for loop to generate random numbers and store them in ten variables (rnd_bing1 to rnd_bing10). The loop iterates five times (for i in range(0,5):), so it generates a new set of random numbers five times.
for i in range (0,5):
    rnd_bing1 = random.randint(1,10)
    rnd_bing2 = random.randint(11,20)
    rnd_bing3 = random.randint(21,30)
    rnd_bing4 = random.randint(31,40)
    rnd_bing5 = random.randint(41,50)
    rnd_bing6 = random.randint(51,60)
    rnd_bing7 = random.randint(61,70)
    rnd_bing8 = random.randint(71,80)
    rnd_bing9 = random.randint(81,90)
    rnd_bing10 = random.randint(91,100)


print("--------------------------")
print("|" , rnd_bing1 , "" , "|" , rnd_bing3 , "|" , rnd_bing5 , "|" , rnd_bing7 , "|" , rnd_bing9)
print("|" , rnd_bing2  , "|" , rnd_bing4 , "|" , rnd_bing6 , "|" , rnd_bing8 , "|" , rnd_bing10)
print("--------------------------")

#In summary, the code generates random numbers and arranges them in a 2x5 grid, similar to a bingo card. Each column of numbers corresponds to a range of ten consecutive integers. The grid is printed with separators at the top and bottom to make it visually appealing.
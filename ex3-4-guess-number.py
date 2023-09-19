#EX.3-4 “Guess the number” game

#It imports the random module, which is used to generate random numbers.
import random

#The following print statements display a welcome message for the game, informing the player about the rules and the range of numbers to guess from. ANSI escape codes are used to change text colors:

print("*************************************")
print("\033[32mWelcome to the Guess the Number game!\033[39m")
print("*************************************")

print("I have chosen a number between \033[32m 1 \033[39m and \033[32m 20. \033[39m Can you guess it?")

#This line generates a random integer between 1 and 20 and assigns it to the variable rnd_guess. This is the number that the player needs to guess.
rnd_guess = random.randint(1,20)

#It initializes the guess variable with an invalid value (-1) to ensure that the while loop runs at least once.
guess = -1

#It initializes the counter variable to keep track of the number of attempts the player makes.
counter = 0

#loop is an infinite loop that continues until the player correctly guesses the number and breaks out of the loop using the break statement.
while True:
    guess = input("Enter your guess (between 1 and 20): ")
    guess = int(guess)

    counter += 1

#The if statement checks if the player's guess (guess) is equal to the randomly selected number (rnd_guess). If they match, it prints a congratulatory message with the number of attempts and exits the loop using break.

    if guess == rnd_guess:
        print("\033[32mCongratulations! You guessed the number " , rnd_guess , "in" , counter , "attempts\033[39m")

        break

#The two elif statements check if the guess is too low or too high compared to the rnd_guess, and it provides feedback to the player accordingly.

    elif guess < rnd_guess:
            print("\033[31mToo low! Try again\033[39m")
    elif guess > rnd_guess:
            print("\033[31mToo high! Try again\033[39m")

print("\n")


#The game loop continues until the player guesses the correct number. Once the player guesses correctly, a message is displayed, indicating the number of attempts it took to guess correctly.
#The code concludes with a newline character (\n) to create space after the game has finished.

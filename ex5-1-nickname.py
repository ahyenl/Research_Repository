#EX.5-1 From input to list


#This line imports the choice function from the random module, which will be used to randomly select elements from lists.
from random import choice


#The elements from list1 and list2 are chosen to form the main part of the nickname, while the element from list3 is added as a title or suffix to the nickname.
#The return result statement returns the generated nickname as a string.

list1 = ["Geeky", "Nerdy", "Tech-savvy", "Cyber", "Innovative", "Digital", 
"Caffeinated", "Screaming", "Techoholic", "Gigabit", "Futuristic", 
"Cloudy", "Wireless", "Pixelated", "Robotronic", "Artificial", 
"Viral", "Quantum", "Epic", "Databionic"]

list2 = ["Banana", "Penguin", "Noodle", "Cupcake", "Bumblebee", "Pickle", 
"Flamingo", "Pancake", "Snickerdoodle", "Cucumber", 
"Wombat", "Marshmallow", "Llama", "Gummy Bear", "Muffin", "Koala", 
"Panda", "Popcorn", "Jigsaw", "Raindrop"]

list3 = ["Master of Memes", "Pixel Picasso", "Code Wizard", "Digital Dynamo", 
"Tech Ninja", "Byte Buccaneer", "Debugging Diva", "Chief Emoji"
"Officer", "Virtual Virtuoso", "Data Jedi", "Wi-Fi Whisperer", "Chief"
"Troubleshooting Titan", "Byte-sized Comedian", "Pixel Puncher", "Algorithm"
"Alchemist", "Digital Doodle Dandy", "Error Eradicator", "Byte Blaster", 
"Techie Tinkerer", "Chief of Laughter Loops"]

def nickname():
    result = choice(list1) + " " + choice(list2) + " " + "," + " " + choice(list3)
    return result


print("Best nickname for you is \033[35m", nickname())
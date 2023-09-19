
#This line imports the Cat class from a module or file named Cat
from Cat import Cat

#It checks if the script is being run as the main program (not imported as a module into another script). 
#If it is the main program, it executes the code inside the block.

if __name__ == "__main__":
    # #blue
    # cat1 = Cat("Coco", 5, "blue")
    # cat1.display()
    # cat1.sound()

    #  #magenta
    # cat2 = Cat("Melon", 5, "magenta")
    # cat2.display()
    # cat2.sound()

    #green
    cat1 = Cat("Rosie", 5, "green")
    cat1.display()
    cat1.sound()
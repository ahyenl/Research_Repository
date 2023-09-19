#EX.6-1 Class “Cat”

#This line imports the Beep sound from winsound 
from winsound import Beep

class Cat:
    #attributes
    name: None
    age: None
    color: None

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    #displays information about the cat, including its name, age, and a cat face in color.
    def display(self):
        print('***Cat: ' , self.name,  '***' , '\nage: ' , self.age , '\ncolor: ' , self.color )
        RESET = "\033[0m"
        if self.color == "blue":
            color_code = "\033[34m"
        elif self.color == "magenta":
            color_code = "\033[35m"
        elif self.color == "green":
            color_code = "\033[32m"   
        print(color_code + '''(\___/)
(=*.*=)
U-----U'''+RESET)
        

#The sound method uses the Beep function from the winsound library to make a sound.
    def sound(self):
        Beep(1000, 500)


#calling the function
cat1 = Cat("Coco", 5, "blue")
cat1.display()
cat1.sound()

cat2 = Cat("Melon", 5, "magenta")
cat2.display()
cat2.sound()

cat1 = Cat("Rosie", 5, "green")
cat1.display()
cat1.sound()





# another way 

# import random
# from winsound import Beep

# colors = ["\033[32mgreen", "\033[34mblue" , "\033[35mmagenta" , "\033[39mdefault"]


# class Cat:
#     def __init__(pussycat, name, age, color, avatar, sound):
#         pussycat.name=name
#         pussycat.age=age
#         pussycat.color=color
#         pussycat.avatar=avatar
#         pussycat.sound=sound

#     def displayData(display):
#         print('***Cat: ' , display.name,  '***' , '\nage: ' , display.age , '\ncolor: ' , display.color  , '\n', display.avatar, '\n' , '\n' , display.sound)

# cat1 = Cat('Coco', 5 , (random.choice(colors)),  '''(\___/)
#  (=*.*=)
#  U-----U''' , winsound.Beep(1000, 500) )
          
# cat1.displayData()



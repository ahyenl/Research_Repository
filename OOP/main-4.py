#(OOP - inheritance)
# Online Store Inheritance


#imports the Product, Electronics, Clothing, Books from file named Product.
from Product import Product, Electronics, Clothing, Books


#it executes the code inside the block
if __name__ == "__main__":
    p1 = Product("Apple" , 5.000 , 2 )
    p1.display()

    #Electronics
    e1 = Electronics("Monitor", 300, 3, "LG")
    e1.display()

     #Clothing
    c1 = Clothing("Tshirt", 150, 2, "H&M")
    c1.display()

     #Books
    b1 = Books("Thriller", 250, 3, "Alex")
    b1.display()
#(OOP - inheritance)
# Online Store Inheritance

class Product:
    # name: None
    # price: None
    # quantity: None
    

    def __init__(self, name, price, quantity ):
        self.name = name
        self.price = round(price , 2)
        self.quantity = quantity
        

    def display(self):
        print("***Product***")
        print("name: " , self.name)
        print("price: " , self.price)
        print("quantity: " , self.quantity)
        print(f"cost: ${self.total()}")

    def total(self):
        return round(self.quantity * self.price, 2)
        
#Electronics

class Electronics(Product):
    brand: None

    def __init__(self, name, price, quantity, brand):
         super().__init__(name, price, quantity)
         self.brand = brand

    def display(self):
        super().display()
        print("brand: ", self.brand)

#Clothing

class Clothing(Product):
    size: None

    def __init__(self, name, price, quantity, size):
         super().__init__(name, price, quantity)
         self.size = size

    def display(self):
        super().display()
        print("size: ", self.size)

#Books

class Books(Product):
    author: None

    def __init__(self, name, price, quantity, author):
         super().__init__(name, price, quantity)
         self.author = author

    def display(self):
        super().display()
        print("author: ", self.author)


p1 = Product("Apple" , 5.000 , 2 )
p1.display()
e1 = Electronics("Monitor", 300.00, 3, "LG")
e1.display()
c1 = Clothing("Tshirt", 150.00, 2, "H&M")
c1.display()
b1 = Books("Thriller", 250.00, 3, "Alex")
b1.display()



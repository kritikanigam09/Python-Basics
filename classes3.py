class ShoppingCart:
    #Creates shopping cart objects for users of our fine website

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}
    
    def add_item(self, product, price):
        #Add product to the cart
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print("{} is added".format(product))
        else:
            print("{} is already in the cart.".format(product))

    def remove_item(self, product):
        #Removes product from the cart
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print("{} is removed".format(product))
        else:
            print("{} is not in the cart.".format(product))

my_cart = ShoppingCart("Eric")
my_cart.add_item("Kitkat", 12)

#Welcome to the world of Inheritance

class Customer: # Produces objects that represent customers
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer): # For the customers of the repeat variety

    def display_order_history(self):
        print("I'm a string that stands for your order history!")

monty_python = ReturningCustomer("ID : 12345")
monty_python.display_cart()
monty_python.display_order_history()





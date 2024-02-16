# This is a program which calculates the total value of stock in a caffe.


# List of menu items.
menu = ["pizza", "latte", "water", "coke"]

# Setting up dictionaries for stock values and prices.
stock = {'pizza': 25,
         'latte': 26,
         'water': 27,
         'coke' : 28,}

price = {'pizza': 4.00,
         'latte': 2.50,
         'water': 2.00,
         'coke' : 3.00,}

""" Method for user entering stock and price values.
stock = {}
price = {}

for elements in menu:
    stock[elements] = int(input("please enter the amount of stock for " + elements + ": "))
    price[elements] = float(input("please enter the price for " + elements + ": "))"""

# Loop that calculates the total value of the stock
total_stock = 0
for elements in menu:
    total_stock = total_stock + price[elements] * stock[elements]
     
print( "The total value of the cafes stock is: £" + str(total_stock))
# This is a program to calculate the cost of a holiday.
# Below is a method for the task that uses a dictionary for the flights, hotel and car rental cost.
# This prevents the use of multiple if and elif statements in the "plane_cost" function.
# It also allows for the price of hotels and car rentals to be changed to reflect local prices.

# Dictionary with available cities and price for flights and hotels.
dest_dict = {'Tokyo': {'flight':462.00, 'hotel': 150.00, 'car': 30.00},
             'New York': {'flight':308.00, 'hotel': 200.00, 'car': 20.00},
             'Venice': {'flight':26.00, 'hotel': 125.00, 'car': 10.00},
             'Accra': {'flight':600.00, 'hotel': 75.00, 'car': 40.00}}

#Printing out the users options
print("Below are the places you can go:")
print("------------------------------")
for elements in dest_dict:
     print("    - " + elements)
print("------------------------------")
print()

# User inputs and validation
while True:
    city_flight = input("What city are you flying to?: ")
    if city_flight in dest_dict:
        print("You have selected " + city_flight + ".")
        print()
        break
    else:
        print("please enter a valid city")
        
while True:
    try:
        num_night = int(input("how many nights will you be staying?: "))
    except ValueError:
        print("Please enter a valid number of night")
    else:
        print()
        break

while True:
    try:
        rental_days = int(input("How many days will you be hiring a car?: "))
    except ValueError:
        print("Please enter a valid number of rental days")
    else:
        print()
        break

# User defined functions to calculate the cost of: flights, hotels and car rentals as well as the total.
# User defined functions would be different without the dictionary, for instance 'hotel_cost' and 'car_rental would only have argument.
# Examples with these discrepancies are shown in docstrings below each function where there are no docstrings there is no difference.
def hotel_cost(num_night, cost):
    x = num_night * cost
    print("Hotel cost:      £" + str(x))
    return x
'''
def hotel_cost(num_nights):
     x = num_nights * 150.00
     print("Hotel cost: £" + str(x))
     return x'''

def plane_cost(cost):
    y = cost * 2
    print("Flight cost:     £" + str(y))
    return y
'''
def plane_cost(city_flight):
    if city_flight == "Tokyo":
           y = 462.00 * 2

    elif city_flight == 'New York':
           y = 308.00 * 2
     
    elif city_flight == 'Venice':
           y = 26.00 * 2

    elif city_flight == 'Accra':
          y = 600.00 * 2
    print("Flight cost: £" + str(y))
    return y'''

def car_rental(rental_days, cost):
    z = rental_days * cost
    print("Car rental cost: £" + str(z))
    return z
'''
def car_rental(rental_days):
     z = rental_days * 15.00
     print("Car rental cost: £" + str(z))
     return z'''

def holiday(x, y, z):
    total = x + y + z
    print("Total cost:      £" + str(total))
    return


# Using the user defined functions. Note one method is for use with the functions which dont need a dictionary.
print("For a " + str(num_night) + " night stay and " + str(rental_days) + " days car rental in " + city_flight + ":")
print("------------------------------")
#holiday( hotel_cost(num_night), plane_cost(city_flight), car_rental(rental_days))
holiday( hotel_cost(num_night, dest_dict[city_flight]['hotel']), plane_cost(dest_dict[city_flight]['flight']), car_rental(rental_days, dest_dict[city_flight]['car']))
print("------------------------------")


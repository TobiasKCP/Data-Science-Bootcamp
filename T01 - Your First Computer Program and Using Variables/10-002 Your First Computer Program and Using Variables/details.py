#Ask the user to input ther Name, Age, House number, and street name
#Save these as strings in the variables "user_name", "user_age", etc
#print a sentance with all the variables

#----- SOLUTION SAVING MULTIPULE INPUTS IN A SINGLE LINE -----

user_name, user_age, user_house, user_street = input("please enter your name, age, house number, and street name (seperate your entries with a comma for example: James,20,50,street street): ").split(",")

#----- SOLUTION SAVING INPUTS ON INDIVIDUAL LINES -----

#user_name = input("Please enter your name: ")
#user_age =  input("Please enter your age: ")
#user_house = input("Please enter your house number or name: ")
#user_street = input("Please enter your street name: ")

print("This is " + user_name + " they are " + user_age + " years old and live at the house " + user_house + " on " + user_street)

# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #Syntax error print function requires brackets.
print ("\n") #Syntax error print function requires brackets and erroneous indentation.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24 years old" #Syntax error erroneous indentation, Runtime error variable wasn't properly assigned
age = int(age_str[0:2]) #Syntax error erroneous indentation variable, Runtime incorrect data type, 
print("I'm " + str(age) + " years old.") #Syntax error print function requires brackets and erroneous indentation, logic error would have printed "I'm24years old"

# Variables declaring additional years and printing the total years of age
years_from_now = 3 #Syntax error erroneous indentation, Runtime error incorrect data type,
total_years = age + years_from_now #Syntax error erroneous indentation

print ("The total number of years:" + "answer_years")

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6 #Runtime error misspelt variable, logic need to add an additional 6 months
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") #Syntax error print function requires brackets, runtime incorrect data type

#HINT, 330 months is the correct answer


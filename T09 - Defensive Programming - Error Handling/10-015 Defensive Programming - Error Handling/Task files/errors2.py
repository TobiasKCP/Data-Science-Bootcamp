# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #Runtime error string must have speech marks
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a " + animal + ". It is a " + animal_type + " and it has " + str(number_of_teeth) + " teeth" #Logic error variables added to new string incorrectly and "animal_type" and "number_of_teeth" were swapped, Runtime "number_of_teeth"  needed to be casted to str.

print (full_spec) #syntax error print function requires brackets


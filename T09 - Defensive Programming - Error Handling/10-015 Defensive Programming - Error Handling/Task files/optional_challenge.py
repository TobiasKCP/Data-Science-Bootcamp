# This is task 7 with intentional errors
# This is a program that takes user inputs and averages them. 

user_num = 0
total = 0
count = 0 # Count should start from -1 to account for the input of a negative user input (Logic error)

while user_num != -1:
user_num = int(input("Please type in a number: ")) # Missing indentation (compilation error)
    total = total + user_num
    count = count + 1

print("You entered " + str(count) + " numbers" # Missing closed brackets (Compilation error)

total = total + 1
Print("the sum total of your entries is " + str(total)) # incorrect capitalization of print statement means its calling a function which doesn't exist (Runtime error)

avg = total / (count - 1)
print("The average is: " + str(round(avg,2)))
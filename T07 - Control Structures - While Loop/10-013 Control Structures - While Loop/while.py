#This is a program that takes user inputs and averages them. 

user_num = 0
total = 0
count = -1

while user_num != -1:
    user_num = int(input("Please type in a number: "))
    total = total + user_num
    count = count + 1

print("You entered " + str(count) + " numbers")

total = total + 1
print("the sum total of your entries is " + str(total))

avg = total / (count - 1)
print("The average is: " + str(round(avg,2)))
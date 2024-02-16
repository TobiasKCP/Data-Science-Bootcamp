
#Using if, elif and else statments check criteira in decending age so oldest criteria first
#Youngest last

user_age = int(input("What is your age?: "))

if user_age >= 100:
    print("Sorry, you're dead!!!")

elif user_age >= 65:
    print("Enjoy your retirement!")

elif user_age >= 40:
    print("Your over the hill.")

elif user_age == 21:
    print("congrats on your 21st!!!")

elif user_age < 13:
    print("You qualify for the kiddie discount.")

else:
    print("age is but a number.")


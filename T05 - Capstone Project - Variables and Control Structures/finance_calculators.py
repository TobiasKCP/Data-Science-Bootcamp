#The following python program allows a user to calculate ether money earned from an investment or a monthly bond repayment.
#Initially it does this by allowing the user to input "investment" or "bond" compares the length of the string.
#This to decided which the user wants and to account for spelling mistakes.
#The same method is applied when the user chooses simple or compound interest.
#Following this the appropriate user inputs are save depending on the selected method.
#Finally the calculations are done and the results printed.

import math

#User input for choosing 'investment' or 'bond' method
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond - to calculate the amount you'll have to pay on a home loan.")
print("")

user_choice =  str(input("Please enter either 'investment or 'bond' from the menu above to proceed: ")).lower().strip()

print("")

#This is a if statement containing the method for calculating investment.
if user_choice == "investment":
    print("You have selected investment. Please follow the following steps.")
    print("")

    #User inputs for investment.
    user_invst = float(input("How much would you like to invest?: "))
    interest_rate = float(input("Please enter the interest rate as a percentage: "))
    years_invst = int(input("For how many years would you like to invest?: "))
    interest = str(input("Would you like 'compound' or 'simple' interest? Please type out the which you would like: ")).lower().strip()
    print("")

    #These are if statements determining which type of interest to use plus calculations and outputs for the interest.
    if interest == "simple":
        print("You have chosen simple interest.")

        money_made = user_invst * (1 + interest_rate * 0.01 * years_invst)

        print("______________________________________")
        print("")
        print("Initial investment:    £" + str(user_invst))
        print("Interest rate:         " + str(interest_rate) + " %")
        print("Period of investment:  " + str(years_invst) + " Years")
        print("Investment value:      £" + str(round(money_made,2)))
        print("______________________________________")

    
    elif interest == "compound":
        print("You have chosen compound interest.")

        money_made = user_invst * math.pow((1 + interest_rate * 0.01),years_invst)

        print("______________________________________")
        print("")
        print("Initial investment:    £" + str(user_invst))
        print("Interest rate:         " + str(interest_rate) + " %")
        print("Period of investment:  " + str(years_invst) + " Years")
        print("investment value:      £" + str(round(money_made,2)))
        print("______________________________________")


    else:
        print("Sorry but your input was invalid.")
        print("Please make sure you inputted the text correctly")
    

#This is a elif statement containing the method for calculating monthly bond repayments.
#This contains variables saving user inputs to calculate the repayments, the calculation itself and the outputs.
elif user_choice == "bond" :
    print("You have selected bond. Please follow the following steps.")
    print("")

    house_val = float(input("What is the present value of the house?: "))
    interest_rate = float(input("Please enter the interest rate as a percentage: "))
    months_to_repay = int(input("How many months do you plan to take to pay?: "))

    repayment = (((interest_rate * 0.01)/12) * house_val) / (1 - (1 + interest_rate  * 0.01/12) ** (-months_to_repay))
    print("______________________________________")
    print("")
    print("Value of your house: £" + str(house_val))
    print("Interest rate:       " + str(interest_rate) + " %")
    print("Time to repay:       " + str(months_to_repay) + " Months")
    print("Monthly repayment:   £" + str(round(repayment,2)))
    print("______________________________________")

else:
    print("Sorry but your input was invalid.")
    
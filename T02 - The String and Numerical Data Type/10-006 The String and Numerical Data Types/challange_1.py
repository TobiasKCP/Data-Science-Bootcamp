#PSUEDOCODE
#Ask the user for the valuse for a three sided tringle storing the values as floats
#Calculate the semi perimeter "s" and area "area"
#Rounding the area to two decimal places

import math

#SAVING THE USER INPUTS

side1 = float(input("please enter the length of a side of your triangle:"))
side2 = float(input("please enter the length of a side of your triangle:"))
side3 = float(input("please enter the length of a side of your triangle:"))

#CALCULATING THE SEMI-PERIMETER "s"

s = (side1 + side2 + side3)/2
print(s)

#CALCULATING THE AREA "area"

area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
area = round(area, 2)
print(area)

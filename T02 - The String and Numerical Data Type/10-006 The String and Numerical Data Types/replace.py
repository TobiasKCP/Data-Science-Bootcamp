#PSUEDOCODE
#Save the text "The!quick!brown!fox!jumps!over!the!lazy!dog." in a variable
#Use the replace function to replace "!" with " " and print
#Use the upper function to change all characters to uppercase and print
#Print the variable contianing the string backwards using slicing


#SAVING THE STRING

string_to_modify = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(string_to_modify)

#REPLACING ! MARKS WITH SPACES

string_to_modify = string_to_modify.replace("!"," ")
print(string_to_modify)

#COVERTING THE STRING TO UPPERCASE LETTERS

string_to_modify = string_to_modify.upper()
print(string_to_modify)

#PRINTING THE SENTANCE IN REVERSE

#---- method using a for loop ----
#to_replace = len(string_to_modify)
#string_list = list(string_to_modify)
#for x in string_to_modify:
    #to_replace = to_replace - 1
    #string_list[to_replace] = x
#reverse_string = "".join(string_list)
#print(reverse_string)

#---- what your supposed to do ----
print(string_to_modify[::-1])
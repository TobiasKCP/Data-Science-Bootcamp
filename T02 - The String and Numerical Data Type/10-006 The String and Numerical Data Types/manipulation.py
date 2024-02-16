
#PSUEDOCODE
#Save the users input as a str in "str_manip"
#Save the length of the string "str_manip" in "manip_length" and print it
#Create a variable "last_chara_index" to save the index of the final character of "str_manip":
    #To do this minus 1 from "manip_length"
#If statment to check for characters for fullstops, exclimation marks, and question marks:
    #If true minus 1 from "last_chara_index" and use it in the replace function to replace every instance of the letter at that index with @ in "str_manip"
#else use "last_chara_index" to replace the letter without minusing 1 from it
#print the last 3 characters backwards using the "last_chara_index-3" and slicing
#create a new variable "new_word" using slicing to take the fist three and last two characters of the string "str_manip"


#SAVING USER INPUT

str_manip = str(input("please input a sentance: "))

#FINDING AND PRINTING THE LENGTH OF THE USERS STRING

manip_length = len(str_manip)
print(manip_length)

#REPLACING EVERY INSTANCE OF THE LAST LETTER WITH @

last_chara_index = manip_length-1
print(last_chara_index)
print(str_manip[last_chara_index])

#if statment checking for fullstops question marks and exclamation marks
if str_manip[last_chara_index] == "." or str_manip[last_chara_index] == "?" or str_manip[last_chara_index] == "!":  
    last_chara_index = last_chara_index-1
    replaced_string = str_manip.replace(str_manip[last_chara_index],"@")
    print(replaced_string)

else:
    replaced_string = str_manip.replace(str_manip[last_chara_index],"@")
    print(replaced_string)

#PRINTING THE LAST 3 CHARACTER BACKWARDS

print(str_manip[last_chara_index:last_chara_index-3:-1])

#CREATING A FIVE LETTER WORD MADE OF THE FIRST THREE AND LAST TWO CHARACTERS OF THE STRING

new_word = str_manip[0:3] + str_manip[last_chara_index-1:]
print(new_word)
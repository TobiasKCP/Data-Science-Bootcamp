# This is a program that takes a string and alternates upper and lower case.


user_string = str(input("Please input a sentence: "))
alt_chara_string = []
alt_word_string = user_string.split(" ")

# Method for alternating upper and lower case characters.
# Loop the iterates through the string saving each character in a list as upper or lower case.
for y in range(0, len(user_string)):
    
    if (y % 2) == 0:
        alt_chara_string.append(user_string[y].upper())
    
    else:
        alt_chara_string.append(user_string[y].lower())

alt_chara_string = "".join(alt_chara_string)
print(alt_chara_string)

# Method for alternating upper and lower case words.
# Loop that iterates through the list alternating changing words to upper and lower case.
for i in range(0,len(alt_word_string)):
    
    if (i % 2) == 0:
        alt_word_string[i] = alt_word_string[i].upper()
    
    else:
        alt_word_string[i] = alt_word_string[i].lower()

alt_word_string = " ".join(alt_word_string)
print(alt_word_string)
    


pattern_line = "*"
pattern_size = 5
act_pattern_size = pattern_size * 2 - 1

#A for loop that prints a line of the pattern,
#then adds or subtracts from the string which holds the pattern.

for y in range(0,act_pattern_size):
    print(pattern_line)

    #If and else statements which check to see if the line is at the midpoint of the pattern.

    if y < (pattern_size-1):
        pattern_line = pattern_line + "*"
    
    else:
        pattern_line = pattern_line[:0] + pattern_line[1:]
    


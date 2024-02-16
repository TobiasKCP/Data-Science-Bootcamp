# This is code from task 8 which is supposed to output a pattern as shown below:
# *
# **
# ***
# ****
# *****
# **** 
# ***
# **
# *
# On line 22 the variable "y" needs to be checked against "pattern_size - 1" as the loop starts from zero
# Hence, will be equal to 4 not 5 when the pattern is at its midpoint.

pattern_line = "*"
pattern_size = 5
act_pattern_size = pattern_size * 2 - 1


for y in range(0,act_pattern_size):
    print(pattern_line)

    if y < (pattern_size): 
        pattern_line = pattern_line + "*"
    
    else:
        pattern_line = pattern_line[:0] + pattern_line[1:]
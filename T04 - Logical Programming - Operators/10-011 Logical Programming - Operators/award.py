#PSUEDOCODE
#Create three varaible to store the times for swiming, cycling and running
#Add the times together to find the total time the particpant has taken
#Using if statments apply the criteria from task 4 to the total time

#VARIABLES STORING THE PARTICAPANTS TIMES

swim_time = int(input("Please enter the particpants swiming time: "))
cycle_time = int(input("Please enter the particpants cycling time: "))
run_time = int(input("Please enter the particpants running time: "))

#FINDING THE TOTAL TIME

total_time = swim_time + cycle_time + run_time

#APPLYING THE CRITERIA

if 0 <= total_time <= 100:
    print("congratulations you were within the qualifing time and have achived Provincial Colours")

elif 101 <= total_time <= 105:
    print("congratulations you were within 5 minutes of the qualifing time and have achived Provincial Half Colours")

elif 105 <= total_time <= 110:
    print("congratulations you were within 10 minuets of the qualifing time and have achived Provincial Scroll")

else:
    print("sorry you did not achive an award")
    

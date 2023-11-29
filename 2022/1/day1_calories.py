file1 = open('elves.txt', 'r')
Lines = file1.readlines()
 

max_calories = 0 
loc_calories = 0
# Strips the newline character
for line in Lines:
    
    if line == "\n":
        if loc_calories > max_calories:
            max_calories = loc_calories
            
        loc_calories = 0
    else:
    
        loc_calories = loc_calories + int(line.replace("\n", ""))
    
print (max_calories)
    
instruction = input()
while (int(instruction) != 99999) :
    if ((int(instruction[0])+int(instruction[1])) != 0):
        if ((int(instruction[0])+int(instruction[1]))%2 == 0):
            direction_temp = 'right'
            direction = direction_temp
        else:
            direction_temp = 'left'
            direction = direction_temp
    else:
            direction = direction_temp  
    print(direction + " " + instruction[2] + instruction[3] + instruction[4] )
    instruction = input()


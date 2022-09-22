instruction = input()
output = ""
for x in range (len(instruction)):
    if (instruction[x] == '+'):
        output += " tighten ".replace("\n","")
    elif (instruction[x] == '-'):
        output += " loosen ".replace("\n","")
    elif (instruction[x].isdigit()):
        output +=(instruction[x])
    else: 
        if (instruction[x-1].isdigit()):
            output += "\n"
            output += instruction[x]
        else:
            output += instruction[x]
            
print(output)
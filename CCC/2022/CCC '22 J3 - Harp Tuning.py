import re
instruction = input()
instruction_new = instruction.replace("+"," tighten ").replace("-"," loosen ")
instruction_new_split = re.split('(\d+)', instruction_new)
for i in range(0, len(instruction_new_split)-1, 2) :
    print(instruction_new_split[i] + instruction_new_split[i+1])  

# instruction_new_split = {'abc': 'def', 'ddd': 23}
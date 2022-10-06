text_input = input()
cyclic_shift = input()
list = []
#print(string_input[3:]) # print characters from the position after 3, which is from position 4 to the end
#print(string_input[:3]) # print characters from beginning to position 3
for x in range(len(cyclic_shift)):
    list.append(cyclic_shift[x:]+cyclic_shift[:x])
string_in_text = False
for string in list:
    if string in text_input:
        string_in_text = True
        break
if string_in_text == False:
    print("no")
else:
    print("yes") 

    

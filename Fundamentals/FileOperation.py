with open("file.txt", "a") as w_file: #w_file = variable name
    # "a" append; "w" can run only once
    w_file.write("Hellow World!\n")
    w_file.write("Hello World!")

with open("file.txt", "r") as r_file:
    # Method 1
    #for line in r_file :
        #print(line)
        #code How to remove one new line
    
    # Method 2 - Only read the first line of the file
    # one_line = r_file.readline()
    # print(one_line)

    # Method 3
    all_lines = r_file.readlines()
    print(all_lines)




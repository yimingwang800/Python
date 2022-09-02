def method_1():
    with open("Sample/song.txt", "r") as w_file: # "\": Windows "/": Linux & Mac OS
        for line in w_file: 
            print(line.strip())   #  strip(): remove all spaces from the front and the end
            # lstrip(), rstrip(), remove "white space"
            #print(line.replace("\n", ""))

def method_2():
    with open("song.txt", "r") as r_file: 
        while True:
            line = r_file.readline()
            if line:
                print(line.strip())
            else:
                break;

def method_3():
    with open("song.txt", "r") as r_file: 
        all_lines = r_file.readlines()
        for line in all_lines: 
            print(line.strip())
        # for i in range(len(all_lines)):
        #     print(all_lines[i].replace("\n", " "))


#method_1()
# method_2()
method_3()

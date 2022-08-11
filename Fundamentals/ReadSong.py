with open("song.txt", "r") as r_file:
    # Method 1
    for line in r_file :
        print(line.replace("\n", ""))
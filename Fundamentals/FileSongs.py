with open("song.txt", "w") as w_file: 
    #song = input()
    # while(song != "end") :
    #     w_file.write("{}\n".format(song))
    #     song = input()
    for x in range(1, 11) : 
        w_file.write("Song {}\n".format(x))

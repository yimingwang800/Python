print("Enter a song or enter 'end' when your finished addding songs (Enter 'queue' if you want to view your playlist): ")
song = input()
playlist = []

while(song != "end") :
    if(song == "queue"):
        print("This is your playlist: ")
        for x in range(len(playlist)):
            #print(x+1, ".", playlist[x])
            print("{}, {}".format(x+1, playlist[x]) )
        print("Continue entering a song or enter 'end' when your finished addding songs (Enter 'queue' if you want to view your playlist): ")
        song = input() 
    else:
        playlist.append(song)    
        song = input()
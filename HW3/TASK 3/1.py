
song = [
    "Well, my friends, the time has come"
    "\nTo raise the roof and have some fun"
    "\nThrow away the work to be done"
    "\nLet the music play on (play on, play on, play on...) "
    "\nEverybody sing, everybody dance"
    "\nLose yourself in wild romance"
    "\nWe're going to Party, Karamu, Fiesta, forever"
    "\nCome on and sing along! "
    "\nAll night long (all night), All night (all night) "
    "\nAll night long (all night), All night (all night) "
    "\nAll night long (all night), All night (all night) "
    "\nAll night long! (all night), Ooh, yeah (all night) "
    "\nPeople dancing all in the street "
    "\nSee the rhythm all in their feet "
    "\nLife is good, wild and sweet "
    "\nLet the music play on...(Play on, play on, play on...) "
    "\nFeel it in your heart and feel it in your soul "
    "\nLet the music take control "
    "\nWe're going to Party, Liming, Fiesta, forever "
    "\nCome on and sing along "
    "\nWe're going to Party, Liming, Fiesta, forever"
    "\nCome on and sing my song! "
]

with open("song.txt", "w")as file:
    file.writelines(song)

with open("song.txt", 'r') as file:
    for line in file:
        line = line.strip()
        words = line.split()
        # print(words)
        for word in words:
            if(word.strip(",") == 'sing'):
                print(line)


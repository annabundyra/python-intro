

file = open('text_file.txt', 'r')
print(file)

#content = file.read()
#print(content)

#content2 = file.readline()
#print(content2)

content = file.readlines()
print(content)

#import pprintpp as pp
#pp(content)


file.close()

file2 = open('new_file.txt', 'a')
file2.write("Frankly, my dear, I don't give a damn. (GONE WITH THE WIND")
#file2.close()

movie_quotes = [
    "\nI'm gonna make him offfer a he can't refuse (THE GODFATHER)",
    "\nMay the Force be with you. (STAR WARS)",
    "\nThere's no place like home. (THE WIZARD OF OZ",
]

file2.writelines(movie_quotes)
file2.close()
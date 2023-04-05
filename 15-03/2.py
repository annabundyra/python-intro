

movie_quotes = [
    "\nI'm gonna make him offfer a he can't refuse (THE GODFATHER)",
    "\nMay the Force be with you. (STAR WARS)",
    "\nThere's no place like home. (THE WIZARD OF OZ",
]

with open('new_file2.txt', 'a') as file:
    file.writelines(movie_quotes)

print('done')
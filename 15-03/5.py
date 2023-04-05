import csv
search_word = input("Give a word: ")
count = 0
with open ("text_file.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.lower()
        words = line.split()

        for word in words:
            if (word == search_word):
                count += 1
print(count)
print(words)



new_list = []
for number in range(5):
    new_list.append(number)

print(new_list)

new_list2 = [number for number in range(5)]
print(new_list2)

words = ['cat', 'dog', 'rat', 'cow']
new_words = []

for word in words:
    if word != 'rat':
        new_words.append(word)

print(new_words)

new_words2 = [word for word in words if word != 'rat']
print(new_words2)

even_numbers = []

for number in range(5):
    if number%2 == 0:
        even_numbers.append(number)

print(even_numbers)
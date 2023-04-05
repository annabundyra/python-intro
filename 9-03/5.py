word = 'YES'
result = ''
for char in word:
    encoded = 'xyz{}abc'.format(char)
    result = result + encoded

print(result)
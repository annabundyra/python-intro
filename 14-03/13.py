
# SET

my_set = {1, 2, 3, 4, 5, 6, 'tak', 6}

my_set.add('3')
my_set.add('3')
my_set.add(7)
my_set.add(8)
print(my_set)

#convert a list to a set to remove duplicates
words = ['hi', 'potatoe','car', 'hi', 'hi', 'car']
results = set(words)
print(type(results))
word_results = list(results)
print(word_results)

nums = [1,2]
nums[2] = 3


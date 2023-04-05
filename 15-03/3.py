
a = input("Put new to do item: ")
a = a + '\n'
with open("to-do.txt", 'r') as file:
    read = file.readlines()
    print(f"Current to do items: {read}")

if a not in read:
    with open("to-do.txt", 'a') as file:
        file.write('\n' + a)
else:
    print("You've already logged that in your list ")

#if a in read:
#    read.remove(a)
#   with open("to-do.txt", 'a') as file:
#        file.write('\n' + a)
#else:
#    print("You've already logged that in your list ")


with open("to-do.txt", 'r') as file:
    read2 = file.readlines()
    print(f"Eddited to do items: {read2}")
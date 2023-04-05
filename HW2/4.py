
x = input("Give a string: ")

def upper(string):
    return string.upper()
def lower(string):
    return string.lower()
def whether_same_letters(string):
    if(string[0] == string[-1]):
        return "The word starts with the same letter as the last letter"
    else:
        return "The word DO NOT starts with the same letter as the last letter"

def replaced(string):
    final_string = ""
    for i in range (len(string)):
        if(string[i] == string[0]):
            final_string += "[REDACTED]"
        else:
            final_string += string[i]
    return final_string

print(upper(x))
print(lower(x))
print(whether_same_letters(x))
print(replaced(x))
import re

my_str = "Nano degree is fun"

regex = "ano\s\w+s"

matched = re.match(regex, my_str)
print(matched)
print(matched.span())
print(matched.group())
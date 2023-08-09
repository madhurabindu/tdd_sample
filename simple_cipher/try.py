import re
str = "always act artifact"
print(str)
str = re.sub('[a]', '@', str)
print(str)
str = re.sub('[e]', '*', str)
print(str)
str = re.sub('[i]', '#', str)
print(str)
str = re.sub('[o]', '%', str)
print(str)
str = re.sub('[u]', '+', str)
print(str)

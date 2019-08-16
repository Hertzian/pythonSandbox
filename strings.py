# Strings in python are surrounded by either single or double quotation marks.

name = 'Lalo'
age = 36

# Concatenate
print('Hello I am ' + name + 'and I am ' + str(age))

# String formatting


# Argi,emts ny position
# print('{},{},{}'.format('a','b','c'))
print('{1},{2},{0}'.format('a','b','c'))

# Argument by name
print('My name is {name} and I am {age}'.format(name='Lalo',age='37'))
print('My name is {name} and I am {age}'.format(name=name,age=age))

# F-strings (only in > 3.6)
print(f'My name is {name} and I am {age}')

# String methods
s = 'hello there world'

# Capitalize first letter
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world','everyone'))

# Count 
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

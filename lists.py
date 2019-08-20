# A list is a collection which is ordered and changeable. Allows duplicate members.

# Create list
# numbers = [1,2,3,4,5]

# type
# print(type(numbers))

# Using constructor
numbers = list((1,2,3,4,5))

fruits = ['Apples','Oranges','Grapes','Pears',12]

# Get value
print(fruits[1])

# get len
print(len(fruits))

# append to list
fruits.append('Mangos')

# remove from list
fruits.remove(12)

# Insert into position
fruits.insert(2,'Strawberries')

# Remove from position 
fruits.pop(3)

# reverse list
fruits.reverse()

# sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)
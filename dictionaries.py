# a dictionary is a collection which is unordered, changeable and indexed. No duplicate members

# simple dictionary
person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'age': 30
}

# using constructor
# person = dict(
#     firstName = 'John',
#     lastName = 'Doe',
#     age = 30
# )

# access value
print(person['firstName'])
print(person.get('lastName'))

# add key/value
person['phone'] = '123456789'

# get keys
print(person.keys())

# get items
print(person.items())

# make copy
person2 = person.copy()
person2['city'] = 'Boston'

# remove item
del(person['age'])
person.pop('phone')

# clear
person.clear()

# get length
print(len(person2))

print(person)

# list of dictionary
people = [
    {'name':'Martha','age':40},
    {'name':'Bob','age':20},
]

print(people[1]['name'])
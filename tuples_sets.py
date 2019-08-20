# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# siple tuple
fruit_tuple = ('Apple','Orange','Mango')
# using constructor
# fruit_tuple = tuple(('Apple','Orange','Mango'))

# get single value
# print(fruit_tuple[1])

# fruit_tuple[1] = 'Grape'

# tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

del fruit_tuple_2

# print(len(fruit_tuple_2))



# A set is a collection which is unordered and unindexed. No duplicate members

fruit_set = {'Apple','Orange','Mango'}

# check if in set
print('Apples' in fruit_set)

# add to set
fruit_set.add('Grape')

# remove to set
fruit_set.remove('Grape')

# clear set
fruit_set.clear()

# delete set
del fruit_set

print(fruit_set)

# Sets
fruits = set(['apple', 'grapes', 'banana', 'cherry'])
print(fruits)

# >> {'grapes', 'banana', 'apple', 'cherry'}

# 1. Adding an element
fruits.add('orange')
print(fruits)

# >> {'grapes', 'banana', 'orange', 'apple', 'cherry'}

# 2. Removing an element
fruits.remove('banana')
print(fruits)

# >> {'grapes', 'orange', 'apple', 'cherry'}

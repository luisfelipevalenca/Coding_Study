fruits = ['apple', 'banana', 'cherry']


# Acessing list elements
print(fruits[0]) # >> apple
print(fruits[1]) # >> banana
print(fruits[2]) # >> cherry
# print(fruits[3]) # >> IndexError: list index out of range

print(fruits[0:3])
# >> ['apple', 'banana', 'cherry']


# Modifying list elements
fruits[1] = 'blueberry'
print(fruits)
# >> ['apple', 'blueberry', 'cherry']

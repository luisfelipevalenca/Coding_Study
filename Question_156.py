# Removing Elements
fruits = ['apple', 'banana', 'cherry', 'grape']


# 1. Using the method .remove()
fruits.remove('grape')
print(fruits)
# >> ['apple', 'banana', 'cherry']

# 2. Using .pop()
# fruits.pop() # >> ['apple', 'banana'] (takes the last element)
fruits.pop(1) 
print(fruits)
# >> ['apple', 'cherry'] (takes the element with index 1)

# 3. Using .clear()
fruits.clear()
print(fruits)
# >> []


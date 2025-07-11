# Adding Elements
fruits = ['apple', 'banana', 'cherry']

# 1. Using the method .append()
fruits.append("orange")
print(fruits)
# >> ['apple', 'banana', 'cherry', 'orange']


# 2. Using insert()
fruits.insert(1, 'grape')
print(fruits)
# >> ['apple', 'grape', 'banana', 'cherry', 'orange']

# 3. Using extend()
add_fruits = ['pear', 'pineapple']
fruits.extend(add_fruits)
print(fruits)
# >> ['apple', 'grape', 'banana', 'cherry', 'orange', 'pear', 'pineapple']



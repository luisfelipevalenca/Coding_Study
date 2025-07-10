fruits = ['apple', 'banana', 'cherry']

# Addingg elements through different methods

# 1. Using .append()
fruits.append('orange')
print(fruits)
# >> ['apple', 'banana', 'cherry', 'orange']

# 2. Using .insert()
fruits.insert(1, 'grape')
print(fruits)
# >> ['apple', 'grape', 'banana', 'cherry', 'orange']

# 3. Using extend()
more_fruits = ['pear', 'pineapple']
fruits.extend(more_fruits)
print(fruits)
# >> ['apple', 'grape', 'banana', 'cherry', 'orange', 'pear', 'pineapple']


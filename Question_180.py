# Dictionary

student = {'name': 'Alice', 'age': 21, 'grades':[85, 90,92]}

# 1. Acessing dictionary values
print(student['name'])
print(student['age'])
print(student['grades'])

# >> Alice
# >> 21
# >> [85, 90,92]

# 2. Modifying dictionary values
student['name'] = 'Sarah'
print(student)

# >> {'name': 'Sarah', 'age': 21, 'grades': [85, 90, 92]}

student['age'] = 22
print(student)

# >> {'name': 'Sarah', 'age': 22, 'grades': [85, 90, 92]}

# 3. Adding element on the dictionary

student['major'] = 'Maths'
print(student)

# >> {'name': 'Sarah', 'age': 22, 'grades': [85, 90, 92], 'major': 'Maths'}

# 4. Removing key-values

del student['grades']
print(student)

# >> {'name': 'Sarah', 'age': 22, 'major': 'Maths'}


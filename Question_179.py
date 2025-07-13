# Dictionary Methods
employee = {'name': 'John', 'position': 'Manager', 'salary': 50000}

# 1. Getting all keys
keys = employee.keys()
print(keys)

# >> dict_keys(['name', 'position', 'salary'])

# 2. Getting all values
values = employee.values()
print(values)

# >> dict_values(['John', 'Manager', 50000])

# 3. Getting all key-values pairs

items = employee.items()
print(items)

# >> dict_items([('name', 'John'), ('position', 'Manager'), ('salary', 50000)])

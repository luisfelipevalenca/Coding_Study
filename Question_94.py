data = {'1':'0', '0':'1'}

for d in data.vals(): # o formato correto seria pelo método '.values()', o output seria: 0 1
    print(d, end=" ")

# This code is erroneous
# >> AttributeError: 'dict' object has no attribute 'vals'

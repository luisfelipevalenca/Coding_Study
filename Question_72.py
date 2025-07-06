data = [1, 2, 3, None, (), [], ]
print(len(data))

for i in data: # imprime cada tipo de dado presente lista 'data'
  print(type(i))

# >> 6
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'NoneType'>
# <class 'tuple'>
# <class 'list'>

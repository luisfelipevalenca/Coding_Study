a = dict ({1: 'Web', 2:'Java', 3: 'DB', 4: 'Ruby'})

# maneiras distintas de imprimir chaves e valores do mesmo dicionário
for i, j in a.items():
     print(i, ' ', j)

print('-' * 12) # Separador

for i in a:
  print(i, ' ', a[i])

"""
1   Web
2   Java
3   DB
4   Ruby
------------
1   Web
2   Java
3   DB
4   Ruby
"""

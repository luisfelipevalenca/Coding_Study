dictionary = {} # cria uma dicionário vazio

my_list = ['a', 'b', 'c', 'd'] # cria uma lista composta por strings

for i in range(len(my_list) - 1): # para cada elemento presente no range do tamanho da lista 'my_list' decrementando o um.
    dictionary[my_list[i]] = (my_list[i], ) # dictionary = {'a':('a',), 'b':('b',), 'c':('c',)}

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])

# >> a
# >> b
# >> c

data = ['abc','def', 'abcde', 'efg'] # cria uma lista 'data' que contém strings de [0, 3].
print(max(data)) # A função max() passa a lista 'data' como argumento. Ela vai comparar as strings
                 # elemento a elemento, com base em seus valores Unicode(ou ASCII). 
                 # Ou seja, vai indicar a string que possuir maior ordem alfabética (ou seja, lexograficamente maior).
                 # A comparação começa com o primeiro caractere de cada string.
                 # Neste caso, comparando os primeiros caracteres: 'a', 'd', 'a', 'e'. 'e' tem o maior valor.

# >> efg

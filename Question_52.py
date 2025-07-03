def string_lengths(strings):
  return [len(s) for s in strings] # vai retornar uma lista contendo o tamanho de cada string [5, 6, 6, 4]

words = ['apple', 'banana', 'orange', 'kiwi'] # cria uma lista de strings
lengths = string_lengths(words) # 'lengths' vai faz referencia a função 'string_lengths' que tem como parametro a lista 'words'
print(lengths)

# >> [5, 6, 6, 4]

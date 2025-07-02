a = 'Python'

# string_name[start_index:end_index: step]

print(a[1:4:1]) # a[]: string, start_index:1, end_index:4, step: 1
print(a[1:4]) # ambos os comandos irão apresentar o a mesma resposta pois o valor de step padrão é 1.
print(a[1:]) # o end_index e step foram omitidos, então será impresso toda a string após o start_index
print(a[:4]) # o start_index e step foram omitidos, então será impresso toda a string antes do end_index
print(a[:4:2]) # o end_index é 4 com step 2 (o start_index padrão é 0 -> P) então, esperamos essa estrutura: P_ _t 

# >> yth
# >> yth
# >> ython
# >> Pyth
# >> Pt

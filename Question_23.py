data = (1, ) * 3
data[0] = 2 # tuplas são imutáveis, então não se pode prosseguir com essa ação num índice específico
print(data)

# The code is erroneous
# >> TypeError: 'tuple' object does not support item assignment

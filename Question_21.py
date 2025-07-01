data = () # cria uma tupla vazia
print(data.__len__()) # o método __len__ é do tipo'dunder' (double underscore). Neste caso ele é equivalente função len(). Ou seja, 0.

# >> 0

# independente de como a for chamda (seja por um método, ou função), ela vai apontar para o mesmo local na memória
# print(id(len(data))) -> 10757704
# print(id(data.__len__())) -> 10757704

List1 = [1, 2, 3, 4, 5]
# print(id(List1)) >> 139607558652864
List2 = List1[:] # cria uma nova lista que contém os mesmos elementos que List1,
                 # mas estão alocados em pontos diferentes na memória. Ou seja, modificar List2, não influi em List1
                 
# print(id(List2)) >> 139607562886464

List2.append(6)

print(List1)
print(List2)

# print(id(List1)) >> 139607558652864
# print(id(List2)) >> 139607562886464


# >> [1, 2, 3, 4, 5]
# >> [1, 2, 3, 4, 5, 6]

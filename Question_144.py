# Usando a função list()
list_1 = [10, 20, 30]
list_2 = list(list_1)

print("Lista  de Origem (list()):", list_1)
print("Lista Cópia (list()):", list_2)
print("ID da Lista de origem (list()):", id(list_1))
print("ID da Lista Cópia (list()):", id(list_2))

print("-" * 20) # Separador

# Usando o método copy()
list_3 = [100, 200, 300]
list_4 = original_list_copy_method.copy()

print("Lista  de Origem (copy()):", list_3)
print("Lista Cópia (copy()):", list_4)
print("ID da Lista de origem (copy()):", id(list_3))
print("ID da Lista Cópia (copy()):", id(list_4))

print("-" * 20) # Separador

# Usando slicing
list_5 = [1000, 2000, 3000]
list_6 = list_5[:]

print("Lista  de Origem (slicing):", list_5)
print("Lista Cópia (slicing):", list_6)
print("ID da Lista de origem (slicing):", id(list_5))
print("ID da Lista Cópia (slicing):", id(list_6))

print("-" * 20) # Separador

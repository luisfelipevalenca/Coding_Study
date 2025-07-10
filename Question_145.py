list_1 = [10, 20, 30]
list_2 = list_1

print("Lista  de Origem:", list_1)
print("Lista Cópia:", list_2)
print("ID da Lista de origem:", id(list_1))
print("ID da Lista Cópia:", id(list_2))

print('-' * 20)

# Usando o método .append() para adicionar um novo elemento ao final da Lista de Origem

list_1.append(40)

print("Lista  de Origem:", list_1)
print("Lista Cópia:", list_2)
print("ID da Lista de origem:", id(list_1))
print("ID da Lista Cópia:", id(list_2))

print('-' * 20)

print(bool(list_1 == list_2)) # >> True

"""Lista  de Origem: [10, 20, 30]
Lista Cópia: [10, 20, 30]
ID da Lista de origem: 138317434259584
ID da Lista Cópia: 138317434259584
--------------------
Lista  de Origem: [10, 20, 30, 40]
Lista Cópia: [10, 20, 30, 40]
ID da Lista de origem: 138317434259584
ID da Lista Cópia: 138317434259584
--------------------
True"""

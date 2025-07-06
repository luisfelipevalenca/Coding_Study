data = {'name': 'Peter', 'age': 30}
person = data.copy() # faz uma shallow copy do dicionário 'data'. Sendo assim, é criado um novo objeto, mas com os mesmos elementos presentes no dicionário de referência

print(id(data) == id(person)) # verifica as condições (se estão no alocadas no mesmo local na memória), como não, retornará 'False'.

print(person) # {'name': 'Peter', 'age': 30}
print(type(data)) # <class 'dict'>
print(type(person)) # <class 'dict'>
print(id(data)) # 140001324976896
print(id(person)) # 140001324976896


# >> False


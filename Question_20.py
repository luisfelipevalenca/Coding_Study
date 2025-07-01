t1 = (1, 4, 9)
# print(id(t1)) >> 138231467424960
t2 = ('A', 'D', 'Z')
# print(id(t2)) >> 138231326486016
t3 = (True, False, None)
t4 = (5.0, 7.5, 9.9)

# print(type(t4))    >> <class 'tuple'> (verifica o tipo que estrutura o dado, ou seja, uma tupla)
# print(type(t4[0])) >> <class 'float'> (verifica que o tipo de dado que está inserido no index 0, ou seja, um numero flutuante (float))

t1, t3 = t2, t4 # faz a para onde as tuplas t1 e t3 irão apontar na memória

# print(id(t1)) >> 138231326486016
# print(id(t2)) >> 138231326486016
# após a troca, t1 passou a apontar para o mesmo local onde t2 estava alocando memória. 

print(t1)

# >> ('A', 'D', 'Z')

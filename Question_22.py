fruits1 = ['Apple', 'Pear', 'Banana']
# print(id(fruits1)) -> 138230412740480 (verificando onde fruits1 está alocado)
fruits2 = fruits1 # fruits2 e fruits1 apontam para o mesmo objeto
fruits3 = fruits1[:] # cria uma nova lista que é uma cópia vazia de fruits1, ou seja, ['Apple', 'Pear', 'Banana']. Ou seja, uma nova lista com os mesmos elementos em fruits1, mas em local distinto de fruits1 e fruits2.

# print(id(fruits1)) -> 138230412740480 
# print(id(fruits2)) -> 138230412740480 

fruits2[0] = 'Cherry'
fruits3[1] = 'Orange'

res = 0

for i in (fruits1, fruits2, fruits3):
    if i[0] == 'Cherry':
        res += 1 # res = res + 1
    if i[1] == 'Orange':
        res += 10 # res =  res + 10

print (res)

# >> 12

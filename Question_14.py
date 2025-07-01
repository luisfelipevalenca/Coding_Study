w = [7, 3, 23, 42] # lista composta por elementos que representam números inteiros
x = w[1:] # [3, 23, 42] cria uma lsita que fatia do segundo elemento ao último
y = w[1:] # [3, 23, 42] cria uma lsita que fatia do segundo elemento ao último
z = w     # [7, 3, 23, 42] faz uma referência a mesma lista de objetos presentes em w. z e w apontam para a mesma lista na memória RAM.
          # Ou seja, qualquer mudança operacionalizada em z, será feita em w.

# print(id(w)) >> 137006873758080
# print(id(x)) >> 137006873767936
# print(id(z)) >> 137006873758080

y[0] = 10 # [10, 23, 42]
z[1] = 20 # [7, 20, 23, 42]

print(w)

# >> [7, 20, 23, 42]

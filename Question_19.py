nums = [1, 2, 3] # lista composta por números inteiros de tamanho 3
print(nums[::-1])
data = ('Peter',) * (len(nums) - nums[::-1][0]) # cria uma tupla 'data'
                 # len(nums): calcula o tamanho da lista 'nums', ou seja, 3
                 # nums[::-1]: cria uma cópia da lista 'nums', só que invertida, ou seja, [3, 2, 1]
                 # nums[::-1][0]: pega o elemento no índice 3 desta lista invertida, i[0] = 3.
# data = ('Peter',) * (3 - 3) -> 0, resultando numa tupla vazia '()'


# >> ()

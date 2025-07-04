numbers = [1, 2, 3, 4, 5] # cria uma lista composta por numeros inteiros de 1 a 5
new_numbers = [x ** 2 for x in numbers if x % 2 == 0] # eleva ao quadrado os numeros pares
print (new_numbers) # new_numbers = [2**2,4**2], ou seja, [4,16]

# >> [4, 16]

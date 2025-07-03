def factorial (n): # cria uma função chamada factorial. 
    if n == 0 or n == 1: # bloco de analisa a condição do parâmetro ser 1 ou 0
       return 1 
    else: # caso não satisfazer o critério anterior, realiza a operação matemática
      return n * factorial (n - 1)

result = factorial (5) # chama a função factorial (5) -> 120
print("factorial is", result)

# >> factorial is 120

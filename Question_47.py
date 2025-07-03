def check_even_odd(number):
  if number % 2 == 0: # verifica se o módulo de 2 do numero é igual a zero
      return "Even"
  else:
      return "Odd" # como não é o caso, ele o resultado esperado será "Odd", caindo nesta condição

print(check_even_odd(7)) 

# >> Odd

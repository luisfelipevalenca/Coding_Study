i = 0

while i != 0:
  i //= 2
  print("**", end="")

# como i = 0, ele não passa pela primeira parte do código, vindo diretamente para a condição 'else'
else:
  print("*")

# >> *

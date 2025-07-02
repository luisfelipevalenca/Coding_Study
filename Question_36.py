x = 20

def func():
  global x # x vai referir-se a variável global
  x += 10 # x = 20 + 10 = 30
  print(10 + x) # 10 + 30 = 40

print(x) # imprime a variável global 
func()   # imprime o valor retornado pela função
print(x) # imprime o valor da variável x após o valor da variável dinâmica

# >> 20
# >> 40
# >> 30

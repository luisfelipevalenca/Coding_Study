computers_RAM = {"server1": 12, "server2": 16, "server3":24}
for computer in computers_RAM.values(): # o laço vai iterar para cadar valor do dicionário (12, 16, 24)
  print(str(computer)[0], end="") # converte o valor numerico da string, acessando o primeiro index de cada uma e printando na mesma linha, ou seja, 112

# >> 112 
  

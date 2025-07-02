k = 1 

for i in range(1,2): # <seq de numero tipo int: 1>
  for j in range(-1,2): # <seq de numeros tipo int: -1, 0, 1>
      if i == j: # essa condição não será executada pois i != j
           k += 1
      else:
         break 

print(k)


# >> 1   

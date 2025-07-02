names = (True, False, True, False)
newnames = names[2:] # newnames = (True, False)

i = 0
for name in newnames[-1:]:
  # newnames[-1:] = (False,)
  if name: # não entra na condição pois a condição não é satisfeita
    i += 1 

print(i) # vai printar o valor inicia de i, ou seja 0.

# >> 0

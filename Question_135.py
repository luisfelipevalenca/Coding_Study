x = True
y = False
z = False

if not x or y: # False or False 
    print(1) # False (não entra nesse bloco)
elif not x or not y and z: # (False or True) and False
    print(2) # False (não entra nesse bloco)
elif not x or y or not y and x: # (False or False) or (True and True) == True or True == True
    print(3) # imprime esse bloco
else:
    print(4)

# >> 3

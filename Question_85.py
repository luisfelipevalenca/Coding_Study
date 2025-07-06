data = {1: 0, 2: 1, 3: 2, 0: 1}
x = 0

for _ in range(len(data)): # para cada valor até o range (4)
    x = data [x] # data [0] = 0 (index 0 do dicionário é: key 1: value 0)...; data[1] = 0 
print(x)
 
# >> 0 

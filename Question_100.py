data = [1, 2, 3, 4, 5, 6]
        
for i in range(1, 6):
    data[i - 1] = data[i] # data[1 - 1] = data[0], data [2 - 1] = data [1], ...
    # data =  [2, 3, 4, 5, 6]; i[0] = 2, i[1] = 3, ..., 6

for i in range(0, 6):
    print(data[i], end = ' ') # imprime os 5 primeiros elementos presentes em data, com um espaço entre eles.

# >> 2 3 4 5 6  

data = {} # cria uma dicionário vazio
data['2'] = [1, 2] # o index zero tem key-values '2': [1, 2]
data['1'] = [3, 4] # o index um tem key-values '1': [3, 4]

# print (data) >> {'2': [1, 2], '1': [3, 4]}

for i in data.keys():
    print(data[i][1], end =" ") # dentro de cada key pertencente ao dicionário, vai rodar um loop e printar os valores de index 1
                                # após isso, vai pritar os valores dandoum espaço entre eles pois temos o operador 'end=" "'
                                # data [0] = '2': [1,2]
                                # data [1] = '1': [3,4]
                                # em i = 0 -> data[0][1] = 2
                                # em i = 1 -> data[1][1] = 4

# >> 2 4 

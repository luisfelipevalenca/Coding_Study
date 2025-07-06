data1 = '1' + '2' # concatena as strings '1' e '2', retornando >> 12
print (type(data1))
data2 = ('3', '4') # ('3','4')
print(data2)

print(data1 + data2) # erro, não se pode concatenar operandos de sequências diferetentes (neste caso, uma sting e uma tupla)

# >> TypeError: can only concatenate str (not "tuple") to str

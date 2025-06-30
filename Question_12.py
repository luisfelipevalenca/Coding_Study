d = {}
d[1] = 1
d['1'] = 2 
d[1] +=1

# d = {1: 2, '1': 2}

sum = 0

for k in d:
    sum += d[k]
 
print (sum)

# >> 4

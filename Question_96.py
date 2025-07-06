data = [
    [1, 2, 3, 4],          # data[0]
    [5, 6, 7, 8],          # data[1]
    [9, 10, 11, 12],       # data[2]
    [13, 14, 15, 16]       # data[3]
]

for i in range(0, 4):
    print(data[i].pop(), end = ' ') # assim os elementos retirados de cada suconjunto data[0] = 4, data[1] = 8, data[2] = 12, data[3] = 16

# >> 4 8 12 16

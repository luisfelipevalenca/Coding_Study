data = [[0, 1, 2, 3] for i in range(2)]
# data = [[0, 1, 2, 3], [0, 1, 2, 3]] -> data [0] = [0, 1, 2, 3]; data [1] = [0, 1, 2, 3]; data [2] = error

print(data[2][0])

# The code is erroneous
# >> IndexError: list index out of range

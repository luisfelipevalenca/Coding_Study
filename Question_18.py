my_list = [0, 1, 2, 3]

x = 1 # valor inicial de x 
for elem in my_list:
    x *= elem # ele será interado seguindo essa lógica -> x = x * elem

    # x = 1 * 0, então x é 0.
    # x = 0 * 1, então x é 0.
    # x = 0 * 2, então x é 0.
    # x = 0 * 3, finalmente, x é 0.
    
print(x)

# >> 0

def square_numbers(lst): # calcula apenas o quadrado dos numeros positivos e não-zero
    return [x ** 2 for x in lst if x > 0]

print(square_numbers([-1, 0, 1, 2, 3]))

# >> [1, 4, 9]

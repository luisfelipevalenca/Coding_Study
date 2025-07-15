# 2. Using lambda function with built-in functions (lambda functions are often used with map() functions)

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# >> [1, 4, 9, 16, 25]

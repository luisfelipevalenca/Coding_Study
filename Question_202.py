# 3. Using lambda function with built-in functions (lambda functions are often used with map() and filter () functions)

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_nums = list(filter(lambda x: x % 2 == 0, numbers))

print(squared_numbers)
print(even_nums)

# >> [1, 4, 9, 16, 25]
# >> [2, 4]

# 4. Using lambda function with built-in functions (lambda functions are often used with map() and filter () and sorted() functions)

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
points = [(3, 4), (1, 2), (5, 6)]
sorted_points = sorted(points, key = lambda x: x[0] + x[1])

print(squared_numbers)
print(even_nums)
print(sorted_points)

# >> [1, 4, 9, 16, 25]
# >> [2, 4]
# >> [(1, 2), (3, 4), (5, 6)]

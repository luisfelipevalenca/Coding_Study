numbers = list(range(1,10))
print(numbers)

# 1. Couting occurences
count_of_five = numbers.count(5)
print(count_of_five) 
# >> 1

# 2. Sorting the list
numbers.sort()
print(numbers)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Reversing the list
numbers.reverse()
print(numbers)
# >> [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 4. Copyin the list
numbers_copy = numbers.copy()
print(numbers_copy)
# >> [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 5. Clearing the list
numbers.clear()
print(numbers)
# >> []

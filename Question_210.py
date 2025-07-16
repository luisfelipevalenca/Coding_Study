# 2.1 Catching specific exceptions

try:
 number = int(input('Enter a number:'))
 result = 10/number
 print('Result:', result)
except ZeroDivisionError:
  print('Error: Division by zero.')
except ValueError:
  print('Error: Invalid input. Please enter a valid number.')

# >> Enter a number:0
# >> Error: Division by zero.

# >> Enter a number:50
# >> Result: 0.2

# >> Enter a number:a
# >> Error: Invalid input. Please enter a valid number.

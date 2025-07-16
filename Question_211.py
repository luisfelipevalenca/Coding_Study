# Using else and finally clauses
try: 
  number = int(input('Enter a number:'))
  result = 10/number

except (ZeroDivisionError, ValueError) as e:
  print(f'Error: {e}')  
else:
  print('Result:', result)
finally:
  print('Program execution completed')

# >>  Enter a number:sdasd
# >>> Error: invalid literal for int() with base 10: 'sdasd'

# >> Enter a number:1
# >> Enter a number:2
# >> Result: 5.0
# >> Program execution completed

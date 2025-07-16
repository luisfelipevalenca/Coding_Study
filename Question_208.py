# 1.1 Basic try except block (handling a division by zero error)
try:
    result = 10/0
except ZeroDivisionError:
    print('Error: Division by zero')  

# >> Error: Division by zero


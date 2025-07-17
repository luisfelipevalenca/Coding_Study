def calculator():
  try:
    num1 = float(input('Enter the first number:'))
    operator = input('Enter the operator (+, -, *, /):')
    num2 = float(input('Enter the second number:')) 

    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      result = num1 / num2
    else:
      raise ValueError('Invalid operator')
  except ValueError as e:
    print(f'Error: {e}')
  else:
    print('Result:', result)

calculator()

"""Enter the first number:80
Enter the operator (+, -, *, /):+
Enter the second number:2
Result: 82.0"""

def get_interger_input(prompt):
    while True:
      try:
        value = int(input(prompt))
        return value
      except ValueError:
        print('Invalid input. Please enter an integer.')

number = get_interger_input('Enter an integer:')
print('You entered:', number)

"""Enter an integer:sadsad
Invalid input. Please enter an integer.
Enter an integer:252sds.
Invalid input. Please enter an integer.
Enter an integer:25
You entered: 25"""

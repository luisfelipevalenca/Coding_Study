def function_with_args(*args, **kwargs):
    print(args)
    print(kwargs)

function_with_args(1, 2, three = '3', four = '4')

# >> (1, 2)
# >> {'three': '3', 'four': '4'}

"""
 1. The output will be (1, 2) and {'three': '3', 'four': '4'}
 2. *args allows for variable numbers of positional arguments
 3. **kwargs allows for variable numbers of keyword arguments
 4. Both *args and **kwargs can be used in the same function"""

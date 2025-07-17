# mymodule.py

def greet(name):
    return f"Helo, {name}!"

def add(a,b):
    return a + b

# main.py
import mymodule

# Using functions form the custom module
message = mymodule.greet('Alice')
sum_result = mymodule(5,7)
print(message)
print(sum_result)

# 2. Global Variables (variables defined outside any funciton are global and can be accesssed anywhere in the code)


message = 'Hello, world!'

def greet ():
    print(message)

greet()
print(message)

# >> Hello, world!
# >> Hello, world!

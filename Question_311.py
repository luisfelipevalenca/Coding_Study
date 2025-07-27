name = 'john'

def scope_test():
    print(name)
    global x
    x = 123

scope_test()
print(x)

# >> john
# >> 123

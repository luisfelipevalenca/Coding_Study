# 3. Modifying Global variables (use the global variables to modify a global variable inside a function)

counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)

# >> 1

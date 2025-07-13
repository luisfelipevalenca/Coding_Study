def velocity (x - 10): # só aceita parametros, não expressões
    return speed * x

speed = 10
new_speed = velocity()
new_speed = velocity(new_speed)


print(new_speed)


# >> This code is erroneous.
# >> SyntaxError: invalid syntax

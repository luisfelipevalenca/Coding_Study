def func(x):
    if x >= 0:
      return x
    else:
      return func(-x)

print(func(-5))

# >> 5

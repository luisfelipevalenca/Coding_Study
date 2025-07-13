def traverse(stop):
    if stop == 0:
        return 0
    else:
        return stop * traverse (stop - 1) # 0 * traverse (2 - 1) = 0

print(traverse(2))

# >> 0


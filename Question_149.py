rates = (1.2, 1.4, 1.0)

new = rates [3:]
for rate in rates [-2:]:
    new += (rate,)

print(new)
print(len(new))

# >> (1.4, 1.0)
# >> 2

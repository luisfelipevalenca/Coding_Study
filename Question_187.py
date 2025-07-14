# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union
union_set = set_a.union(set_b)
print(union_set)

# >> {1, 2, 3, 4, 5, 6}

# intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)

# >> {3, 4}

# difference
difference_set = set_a.difference(set_b)
print(difference_set)

# >> {1, 2}

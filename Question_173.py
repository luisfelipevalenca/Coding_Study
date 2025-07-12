def merge_dicts(dict1, dict2):
    return {**dict1, **dict2} # ** aka 'unpacking' or 'splat' operator unpacks the key-value pairs form both dicts
                              # the value 'b' from dict2 will overwrite the vlaue from dict1 if values overlaps
                              # which is the case

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}

print(merge_dicts(dict_a, dict_b))

# >> {'a': 1, 'b': 3, 'c': 4}

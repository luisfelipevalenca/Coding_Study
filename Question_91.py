my_list = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]

def fun(lst):
    del lst[lst[2]] # lst[2] = 4, lst[lst[2]] = lst[4] = 16. Ao realizar a operação del lst[lst[2]], tira-se o elemento presente no index 4
    return lst # [0, 1, 4, 9]

print(fun(my_list))

# >> [0, 1, 4, 9]

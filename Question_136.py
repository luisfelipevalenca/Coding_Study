x = [[[1,2], [3,4]],[[5,6], [7,8]]]

def func(data):
    res = data[0][0] # 1

    for da in data: 
        # print(da) # [1, 2]
        for d in da:
            # print(d) # 1
            if res < d:
                res = d
    return res

print(func(x[0])) # 4

# >> 4 

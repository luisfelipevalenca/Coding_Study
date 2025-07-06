list = ['Peter','Paul', 'Mary']

def list(data):
    del data[1] 
    data[1] = 'Jane' 
    return data

print(list(list))

# This code is errouneous
# >> TypeError: 'function' object does not support item deletion
                                

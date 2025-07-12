def is_palindrome (s):
    return s == s[::-1] # verifica se a string s é a mesma quando de trás para frente

print(is_palindrome('racecar'))

# >> True

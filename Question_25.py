nums = [1, 2, 3]
vals = nums # Esta linha atribui a variável vals ao mesmo objeto de lista que 'nums' está referenciando no momento. 'vals'
            # agora é um alias para a lista para a qual nums aponta. 
            # Ambas as variáveis ​​se referem exatamente ao mesmo local na memória.

print(id(nums)) # 138230382026560
print(id(vals)) # 138230382026560
print(type(nums)) # <class 'list'>
print(type(vals)) # <class 'list'>
print(nums) # [1, 2, 3]
print(vals) # [1, 2, 3]

# nums and vals are different names of the same list
# nums and vals have the same length

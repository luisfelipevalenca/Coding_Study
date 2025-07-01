nums = [] # cria uma lista vazia
vals = nums # assinala 'vals' aos memos objetos cuja lista 'nums' referencia. Ou seja, num e vals apontam para a mesma lista na memória RAM.
vals.append(1) # indroduz o número inteiro 1 a lista 'vals'. Consequentemente, também em 'nums'
print(vals) # >> [1]
print(nums) # >> [1]

print(len(nums)) # 1
print(len(vals)) # 1

# nums and vals are of the same length

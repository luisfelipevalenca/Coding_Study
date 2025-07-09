w = bool(23) # quando a função bool quando recebe qualquer número (positivo ou negativo), não zero, é considerado verdadeiro.
print(w) # True

x = bool('') # string vazia é considerada falsa, então imprime False
print(x) # False

y = bool(' ') # a string contém espaço, então é verdadeira
print(y) # True

z = bool([False]) 
print(z) # True

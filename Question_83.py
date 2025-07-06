my_list_1 = [1, 2, 3]
my_list_2 = []

for v in my_list_1:
    my_list_2.insert(0, v) # 0 é o index onde o elemento será inserido, v é o elmento a ser inserido proveniente de my_list_1
    print(f"Inserindo elemento {v}, my_list_2 fica: {my_list_2}")
print(my_list_2)

# >> Inserindo elemento 1, my_list_2 fica: [1]
# >> Inserindo elemento 2, my_list_2 fica: [2, 1]
# >> Inserindo elemento 3, my_list_2 fica: [3, 2, 1]
# >> [3, 2, 1]


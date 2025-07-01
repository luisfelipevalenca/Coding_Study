vals =[0, 1, 2]
vals[0], vals[1] = vals[1], vals[2]
# o i[0] = 1, i[1] = 2 e i[3] = não muda

print(vals)
print(len(vals))
# [1, 2, 2]
# 3
# doesn't change the list's length

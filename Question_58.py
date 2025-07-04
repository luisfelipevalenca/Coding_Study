a = 5
b = 10
c = (a + b) / a # (5 + 10) / 5 = 3
d = a + b/a     # 5 + 10/5 = 5 + 2 = 7

# 1) c < d = True
# 2) b > c AND b > d = True
# 3) a in [c, d] = 5 nao está presente na lista [3, 7] False

print(bool(c < d))
print(bool(b > c and b > d))
print((a in [c, d]))

# >> True
# >> True
# >> False

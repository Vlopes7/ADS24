c = 0
v = 0

for c in range(1067, 3627 + 1):
    if (c % 2 == 0) and (c % 7 == 0):
        v = v + 1
    else:
        continue
print(v)

import random
l1 = list()
l2 = list()
l3 = list()

for c in range(1,21):
    t = random.randint(1,100)
    if c <= 10:
        l1.append(t)
    else:
        l2.append(t)

for k in range(0,10):
    l3.append(l1[k])
    l3.append(l2[k])

print(l1)
print(l2)
print(l3)


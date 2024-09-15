import random
par = list()
impar = list()
l = list()

c = 0

for c in range(0,20):
    t = random.randint(0,100)
    l.append(t)

    if t % 2 == 0:
        par.append(t)
    else:
        impar.append(t)

print(f"Lista Geral: {l}")
print(f"Pares:{par}")
print(f"Ímpares:{impar}")



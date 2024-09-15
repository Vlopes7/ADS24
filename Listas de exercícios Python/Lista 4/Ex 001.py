import random
maior = 0
menor = 0
l = list()

for c in range(0,10):
    t = random.randint(0,100)
    l.append(t)

    if c == 0:
        maior = t
        menor = t
    if(t > maior):
        maior = t
    if(t < menor):
        menor = t

print(l)
print(f"O maior valor gerado na lista é {maior}, e o menor é {menor}")



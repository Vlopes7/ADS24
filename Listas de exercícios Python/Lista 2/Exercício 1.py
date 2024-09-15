maior = 0
a = int(input("Digite a medida do lado A:"))
b = int(input("Digite a medida do lado B:"))
c = int(input("Digite a medida do lado C:"))


if (a > b) or (a > c):
    maior = a

if (c > b) or (c > a):
    maior = c

if (b > a) or (b > c):
    maior = b

if (maior == 0):
    print(f"Usando os valores {a},{b} e {c}, forma-se um triângulo equilátero")

else:

    if (a == b) or (a == c):
        print(f"Usando os valores {a}, {b} e {c}, forma-se um triângulo isósceles")

    elif (a != b) and (a != c):
        print(f"Usando os valores {a}, {b} e {c}, forma-se um triângulo escaleno")
    
    

    

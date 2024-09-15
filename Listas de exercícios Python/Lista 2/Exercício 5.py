maior = 0
menor = 0
a = int(input("Digite o valor A:"))
b = int(input("Digite o valor B:"))
c = int(input("Digite o valor C:"))

menor = c

if (a > b) and (a > c):
    maior = a

elif (a < menor):
    menor = a

if (c > b) and (c > a):
    maior = c

elif (c < menor):
    menor = c

if (b > a) and (b > c):
    maior = b

elif (b < menor):
    menor = b

if (maior == 0):
    print("Não há um número maior ou menor entre os valores digitados.")

else:
    print(f"O maior valor digitado foi o número {maior} e o menor foi {menor}")




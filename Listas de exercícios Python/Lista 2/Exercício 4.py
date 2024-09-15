maior = 0
a = int(input("Digite o valor A:"))
b = int(input("Digite o valor B:"))
c = int(input("Digite o valor C:"))

if (a > b) and (a > c):
    maior = a

if (c > b) and (c > a):
    maior = c

if (b > a) and (b > c):
    maior = b

if (maior == 0):
    print("Não há um número maior entre os valores digitados.")

else:
    print(f"O maior valor digitado foi o número {maior}")




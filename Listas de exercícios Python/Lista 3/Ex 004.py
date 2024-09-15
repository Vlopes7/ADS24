# 1, 1, 2, 3, 5, 8, 13, 21, 34, 5

n = int(input("Digite um número:"))

f1 = 1
f2 = 1
f3 = 0
contador = 0

print(f"{f1},{f2}", end = ",")

while (f3 < n):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    contador = contador + 1

    print(f"{f3}", end = ",")
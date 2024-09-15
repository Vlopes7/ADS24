# a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00

a = float(input("Digite a quantidade de metros quadrados que irão ser pintados:"))

x = a / 3

print(f"Serão necessárias \033[35m{x} litros de tinta\033[m")

if (x <= 18):
    print("Será necessária \033[35m1 lata de tinta\033[m, com o custo de 80 reais")

else:
    t = x / 18
    c = t * 80

    print("Serão necessárias \033[35m{} latas de tinta\033[m com o custo de \033[32m{:.2f} reais\033[m".format(round(t), c))
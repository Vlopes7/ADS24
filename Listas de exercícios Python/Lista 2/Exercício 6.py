s = float(input("Digite quanto você ganha por hora:"))
h = int(input("Digite a quantidade de horas trabalhadas no mês:"))

s = s  * h

# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato

bruto = s

IR = 0.11 * bruto

inss = 0.08 * bruto

sind = 0.05 * bruto

li = bruto - IR - inss - sind

print(f"\nSalário bruto: \033[32m{bruto} reais\033[m")
print(f"Imposto de renda: \033[32m{IR} reais\033[m")
print(f"INSS: \033[32m{inss} reais\033[m")
print("Sindicato: \033[32m{:.2f} reais\033[m".format(sind))
print("\nO valor do salário líquido é: \033[32m{} reais\033[m".format(li))



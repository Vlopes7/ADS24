f = 0

salario = float(input("Digite o valor do salário:"))
p = float(input("Digite quantos porcento foi o aumento do salário:"))

p = (p + 100) / 100

f = salario * p

print("O salário irá de {} reais para {} reais;".format(salario, f))

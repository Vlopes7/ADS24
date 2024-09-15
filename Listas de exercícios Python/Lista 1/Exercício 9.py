km = int(input("Digite a quantidade de km percorrido:"))
d = int(input("Digite a quantidade de dias que o carro foi usado:"))

p = (60 * d) + (0.15 * km)

print("O preço final que deve ser pago é de {} reais".format(p))

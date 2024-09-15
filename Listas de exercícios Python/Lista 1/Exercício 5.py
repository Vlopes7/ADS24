preço = float(input("Digite o preço do produto:"))
p = int(input("Digite a porcentagem do desconto:"))

p = (100 - p) / 100

f = preço * p

d = preço - f

print("O valor deve ser pago é de {} reais e o valor descontado foi de {} reais".format(f, d))


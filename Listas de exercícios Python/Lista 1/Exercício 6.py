d = float(input("Digite a distância do percurso (km) da viagem:"))
v = float(input("Digite a velocidade média (km / h) do veiculo:"))

t = d / v

print("O tempo que a viagem durará é de {} horas".format(t))

t = t * 60

print("O tempo que a viagem durará é de {} minutos".format(t))

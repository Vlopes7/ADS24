c = int(input("Digite a quantidade de cigarros fumados por dia:"))
a = int(input("Digite há quantos anos fuma:"))

a = a * 365 #Converte anos em dias

t = 10 * c #Tempo perdido por dia, em minutos

t = a * t #Tempo em minutos, necessário converter para dias

f = t / 1440

print("\nO tempo de vida perdido pelo fumante é de {} dias(arredondado);".format(round(f)))


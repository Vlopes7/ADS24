a = 80000
b = 200000

contador = 0

while a <= b:
    a += a * 0.03
    b += b * 0.015
    contador = contador + 1

print(f"Número de anos necessários para que a população do país A ultrapasse ou iguale a do país B: {contador} anos")
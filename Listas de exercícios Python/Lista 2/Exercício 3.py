peso = float(input("Digite o peso total dos peixes:"))

if (peso > 50):
    excesso = peso - 50
    multa = 4 * excesso

    print(f"O pescador deve pagar uma múlta de {multa} reais")

else:
    print("O pescador não deverá pagar multa por excesso de peso")

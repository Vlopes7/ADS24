def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = mdc(num1, num2)
print(f"O MDC entre {num1} e {num2} é: {resultado}")

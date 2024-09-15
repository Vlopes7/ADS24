n = 11
while n < 0 or n > 10:
    n = float(input("\nDigite uma nota:"))

    if n > 10 or n < 0:
        print("Nota inválida!")
    else:
        print("Nota válida!")



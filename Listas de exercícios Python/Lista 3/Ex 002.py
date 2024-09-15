a = str(input("/nDigite o nome de usuário:").lower().strip())
b = str(input("Digite a senha:").lower().strip())

while a == b:
    print("Usuário e senha inválidos")
    a = str(input("/nDigite o nome de usuário:").lower().strip())
    b = str(input("Digite a senha:").lower().strip())

print("Senha válida!")


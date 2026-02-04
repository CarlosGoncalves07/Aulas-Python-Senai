nome = input("Digite o nome:\n")
email = input("Digite o e-mail:\n")
senha = input("Digite a senha:\n")
with open("./pessoa.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome} | E-mail: {email} | Senha: {senha}\n")
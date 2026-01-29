def validar_senha():
    if len(senha)>=8:
        print("Senha válida")
        return True
    else:
        print("Senha inválida")
        return False
def cadastro_terminal():
    usuario = input("Digite o nome do usuario:\n")
    senha = input("Digite a senha:\n")
    while not validar_senha(senha):
        senha = input("Digite uma senha de 8 digitos ou mais:")
        print("Cadastro realizado com sucesso!")

cadastro_terminal()
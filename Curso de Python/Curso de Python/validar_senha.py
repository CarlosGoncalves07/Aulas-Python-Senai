def validar_senha(senha):
    return len(senha) >= 8
def cadastro_terminal():
    usuario = input("Digite o nome do usuario:\n")
    senha = input("Digite a senha:\n")
    while not validar_senha(senha):
        senha = input("Digite uma senha de 8 digitos ou mais:")
    print("Senha válida")
    print("Cadastro realizado com sucesso!")



cadastro_terminal()
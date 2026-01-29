from soma import somar
from funcao_eh_par import eh_par
print("Escolha uma opção:\n")


def menu():
    opcao = input("[1] - Somar\n[2 - Verificar Par\n[0] - Sair\n").upper()
    if opcao == "1":
        valor1 = int(input("Digite o primeiro valor\n"))
        valor2 = int(input("Digite o segundo valor\n"))
        print(somar(valor1,valor2))
        
    elif opcao == "2":
        valor1 = int(input("Digite o primeiro valor\n"))
        valor2 = int(input("Digite o segundo valor\n"))
        print(eh_par(valor1,valor2))
    elif opcao == "0":
        print("Sair")
    else:
        print("Opção invalida")


menu()


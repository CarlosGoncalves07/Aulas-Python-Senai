print("Hello, World!")
print("Bem Vindo(a) ao NovoTech Soluções em Software!")
print("Digite os números que deseja realizar a operação matematica e em seguida escolha a função:")

def somar(a,b):
    return(a+b)

def subtrair(a,b):
    return(a-b)

def multiplicar(a,b):
    return(a*b)

def dividir(a,b):
    return(a/b)


a = int(input("Digite o primeiro número:\n"))
b = int(input("Digite o segundo número:\n"))

opcao = int(input("[1] - Somar\n[2 - Subtrair\n[3] - Multiplicar\n[4] - Dividir\n[0 - Voltar ao Menu]\n"))


if opcao == 1:
    print(somar(a,b))
elif opcao == 2:
    print(subtrair(a,b))
elif opcao == 3:
    print(multiplicar(a,b))
elif opcao == 4:
       print(dividir(a,b))
elif "0":
    print("Escolha a operação: 1-Somar/2-Subtrair/3-Multiplicar/4-Dividir/0-Voltar ao menu anterior")
else:
    print("Opção inválida!")

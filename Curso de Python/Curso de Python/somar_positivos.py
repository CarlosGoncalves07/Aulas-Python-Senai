def validar_inteiro():
    while True:
        input_usuario = input("Digite um número para somar [0 - Sair]:\n ")
        try:
            numero = int(input_usuario)
            return numero
        except:
            print("Entrada inválida. Por favor digite um número:\n")
def somar_positivos():
    acumulador = 0
    valor_usuario = -1
    while valor_usuario != 0:
        valor_usuario = validar_inteiro()
        if valor_usuario > 0:
            acumulador += valor_usuario
    return acumulador

total_da_soma = somar_positivos()
print("O total da soma é" ,total_da_soma)
#_____________________________________________________________________________________
def somar(a,b):
    while True:
        input_usuario = input("Digite um número para somar [0 - Sair]:\n")
        try:
            numero = int(input_usuario)
            return numero
        except:
            print("Entrada inválida. Por favor digite um número:\n")
    return(a+b)
a = int(input("Digite o primeiro número:\n"))
b = int(input("Digite o segundo número:\n  "))
resultado = somar(a,b)
print(somar(resultado))

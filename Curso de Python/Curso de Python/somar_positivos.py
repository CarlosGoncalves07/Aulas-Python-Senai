def somar_positivos():
    acumulador = 0
    valor_usuario = -1
    while valor_usuario != 0:
        valor_usuario = int(input("Digite um valor para somar(0 - Parar):"))
    if valor_usuario > 0:
        acumulador += valor_usuario
    return acumulador

total_da_soma = somar_positivos()
print("O total da soma é" ,total_da_soma)
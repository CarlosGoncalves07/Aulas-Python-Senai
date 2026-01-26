#Soma acumulada
#Leia números inteiros até o usuário digitar 0. Ao final, mostre a soma
numero = int(input("Digite um numero:\n"))

acumulador = 0
while numero != 0:
    acumulador = numero + acumulador
    numero = int(input("Digite um numero:\n"))
print(f"A soma dos numero é: {acumulador}")




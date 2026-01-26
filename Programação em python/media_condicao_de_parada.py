# Média com condição de parada
#Leia números até digitar -1. Mostre a média dos valores digitados

numero = int(input("Digite um numero:\n"))

while numero != -1:
    media = numero / 2
    numero = int(input("Digite um numero:\n"))
print(f"A media dos valores é: {media}")
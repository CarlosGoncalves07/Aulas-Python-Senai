#Faça um programa que peça uma nota, entre zero e dez. Mostre uma
#mensagem caso o valor seja inválido e continue pedindo até que o usuário
#informe um valor válido.

#numeros = [0,1,2,3,4,5,6,7,8,9,10]
#numero = int(input("Digite um numero de 0 a 10:\n"))
numero=int(input("Digite um numero de 0 a 10:\n"))
while numero < 0 or numero > 10:
    print("Valor invalido")
    numero = int(input("Digite um numero de 0 a 10:\n"))
print("Valor válido")

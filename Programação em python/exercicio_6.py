print("Hello World! ")
#Faça um Programa que leia três números e mostre o maior deles.

numero_01 = float(input("Digite o primeiro numero:\n"))
numero_02 = float(input("Digite o segundo numero\n"))
numero_03 = float(input("Digite o terceiro numero\n"))

if numero_01 > numero_02:
    maior = numero_01
else:
    maior = numero_02
if numero_03 > maior:
    maior = numero_03

print(f"O maior numero é o {maior}")
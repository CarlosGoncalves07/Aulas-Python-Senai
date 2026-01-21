#Faça um Programa que leia três números e mostre-os em ordem decrescente.
print("Hello World")

numero_01 = float(input("Digite o primeiro numero\n"))
numero_02 = float(input("Digite o segundo numero\n"))
numero_03 = float(input("Digite o terceiro numero\n"))

maior = numero_01 if numero_01 > numero_02 else mumero_02
maior = numero_03 if numero_03 < maior else maior


menor = numero_01 if numero_01 < numero_02 else numero_02
menor = numero_03 if mumero_03 < menor else menor

if numero_01 != maior and numero_01 != menor:
    meio = numero_01
if numero_02 != maior and numero_02 != menor:
    meio = numero_02
if numero_03 != maior and numero_03 != menor:
    meio = numero_03

print(f"{maior} | {meio} | {menor}")
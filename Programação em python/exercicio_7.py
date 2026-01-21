#Faça um Programa que leia três números e mostre o maior e o menor deles.
print("Hello World")

numero_01 = float(input("Digite o primeiro numero\n"))
numero_02 = float(input("Digite o segundo numero\n"))
numero_03 = float(input("Digite o terceiro numero\n"))

if numero_01 > numero_02:
    maior = numero_01
else:
    maior = numero_02
if numero_03 > maior:
    maior = numero_03

if numero_01 < numero_02:
    menor = numero_01
else:
    menor = numero_02
if numero_03 < menor:
    menor = numero_03

print(f"O maior numero é o {maior}")
print(f"O menor numero é o {menor}")

    
#maior = numero_01 if numero_01 > numero_02 else mumero_02
#maior = numero_03 if numero_03 < menor else menor
#menor = numero_01 if numero_01 < numero_02 else numero_02
#menor = numero_03 if mumero_03 < else menor


print("Hello World! ")
#Faça um Programa que peça dois números e imprima o maior deles.


numero_01 = float(input("Digite o primeiro numero\n"))
numero_02 = float(input("Digite o segundo numero\n"))
if numero_01 > numero_02:
    print(numero_01)

elif numero_02 > numero_01:
    print(numero_02)

else:
    print(f"Os dois números são iguais {numero_01}")
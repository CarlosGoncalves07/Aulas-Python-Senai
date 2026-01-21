#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
#letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print("Hello World! ")
letra = input("Digite a letra: (F-feminino / M-masculino)\n").upper()
if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")
else:
    print("Sexo invalida")
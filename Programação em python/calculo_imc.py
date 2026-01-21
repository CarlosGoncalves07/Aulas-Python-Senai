print("Hello World! ")

peso = float(input("Dogite seu peso: \n"))
altura = float(input("Digite sua altura: \n"))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso! ")
elif imc <= 24.9:
    print("Peso normal! ")
elif imc <= 29.9:
    print("Sobrepeso! ")
elif imc <= 34.9:
    print("Obesidade Grau I ")
    print("Cuidado com a saude! ")
elif imc <= 39.9:
    print("Obesidade Grau II ")
    print("Cuidado com a saude! ")
else:
    print("Obesidade Grau III (Mórbida)! ")
    print("Cuidado com a saude! ")


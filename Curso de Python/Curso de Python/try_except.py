num1 = input("Digite o primeiro numero:\n")
num2 = input("Digite o segundo numero:\n")

try:
    num1 = int(num1)
    num2 = int(num2)

    print(f"A soma dos numeros é: {num1 + num2}")
except:
    print("Digite um numero correto!")
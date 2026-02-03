num1 = input("Digite o primeiro numero:\n")
num2 = input("Digite o segundo numero:\n")
# Sempre que usar o try eu preciso usar o except
try:
    num1 = int(num1)
    num2 = int(num2)

    print(f"A soma dos numeros é: {num1 + num2}")
except:
    print("Digite um numero correto!")

try:
    valor1 = float(input("Digite um número:\n"))
    print(5/0)
except Exception as erro:
    print("Ocorreu um erro:",erro )
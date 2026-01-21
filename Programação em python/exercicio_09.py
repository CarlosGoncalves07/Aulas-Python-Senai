#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
#mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)

print("Hello World")

valor_f = float(input("Digite o valor da temperatura em graus F: "))
valor_c = ((valor_f-32) / 9) * 5
print(f"A temperatura em Celsius é: {valor_c:.2f}°C")
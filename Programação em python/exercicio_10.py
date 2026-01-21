#Faça um Programa que peça a temperatura em graus Celsius, transforme e
#mostre em graus Fahrenheit.

print("Hello World! ")

valor_graus_celsius = float(input("Digite a temperatura em graus celsius: "))
valor_graus_fahrenheit = (valor_graus_celsius * 9/5) + 32
print(f"O valor de graus em Fahrnheit é: {valor_graus_fahrenheit:.2f}°F")